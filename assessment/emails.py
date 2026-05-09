from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from .utils import get_feedback


def send_assessment_email(
  participant,
  overall_score,
  dimension_results
):

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

  email = EmailMessage(
    subject='Leadership Assessment Report',
    body=html_content,
    to=[participant.email]
  )

  email.content_subtype = 'html'

  email.send()