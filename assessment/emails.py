import threading
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from .utils import get_feedback
from weasyprint import HTML


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

    def _send():
        try:
            email = EmailMessage(
                subject='Leadership Assessment Report',
                body=html_content,
                to=[participant.email]
            )
            email.content_subtype = 'html'
            email.attach(
                "Assessment_Report.pdf",
                pdf_file,
                "application/pdf"
            )
            email.send()
            print("Email sent successfully to:", participant.email)

        except Exception as e:
            print("Email Error:", e)

    thread = threading.Thread(target=_send)
    thread.daemon = True
    thread.start()

    return True