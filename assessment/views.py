from django.shortcuts import render
from .models import Question, Participant, Response
import json

# Create your views here.
def index(request):
  questions = Question.objects.all()

  if request.method == "POST":

    name = request.POST.get('name')
    email = request.POST.get('email')

    participant = Participant.objects.create(
      name = name,
      email = email
    )
    for question in questions:

      answer = int(request.POST.get(f'question_{question.id}'))

      if answer:

        Response.objects.create(
          participant = participant,
          question = question,
          selected_option = answer
        )
    

    overall_score = request.POST.get('overall_score')

    dimension_results = json.loads(
        request.POST.get('dimension_results')
    )

    return render(request, 'result.html', {
      'participant': participant,
      'overall_score': overall_score,
      'dimension_results': dimension_results
    })

  return render(request, 'index.html', {
      'questions': questions
  })

def result(request):
  return render(request, 'result.html')