import threading
import base64
from django.template.loader import render_to_string
from django.conf import settings
from .utils import get_feedback
from weasyprint import HTML
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException


def send_assessment_email(participant, overall_score, dimension_results):

    context = {
        'participant': participant,
        'overall_score': overall_score,
        'dimension_results': dimension_results
    }

    for dimension, data in dimension_results.items():
        data['feedback'] = get_feedback(data['band'])

    html_content = render_to_string(
        'emails/report_email.html',
        context
    )

    pdf_file = HTML(string=html_content).write_pdf()
    pdf_base64 = base64.b64encode(pdf_file).decode('utf-8')

    def _send():
        try:
            configuration = sib_api_v3_sdk.Configuration()
            configuration.api_key['api-key'] = settings.BREVO_API_KEY

            api_instance = sib_api_v3_sdk.TransactionalEmailsApi(
                sib_api_v3_sdk.ApiClient(configuration)
            )

            email = sib_api_v3_sdk.SendSmtpEmail(
                to=[{"email": participant.email}],
                sender={
                    "email": "leadershipassessment2026@gmail.com",
                    "name": "Leadership Assessment"
                },
                subject="Leadership Assessment Report",
                html_content=html_content,
                attachment=[{
                    "content": pdf_base64,
                    "name": "Assessment_Report.pdf"
                }]
            )

            api_instance.send_transac_email(email)
            print(f"Email sent successfully to: {participant.email}")

        except ApiException as e:
            print(f"Email Error: {e}")

    thread = threading.Thread(target=_send)
    thread.daemon = True
    thread.start()

    return True