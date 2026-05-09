from django.shortcuts import render
from .models import Question, Participant, Response

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

    total_score = 0
    dimension_scores = {'Decision Making': 0, 'Team Communication': 0,'Strategic Thinking': 0,}

    for question in questions:

      answer = int(request.POST.get(f'question_{question.id}'))

      if answer:

        Response.objects.create(
          participant = participant,
          question = question,
          selected_option = answer
        )

        total_score += answer
        dimension_scores[question.dimension] += answer
    
    def get_band(score):

      if score <= 7:
        return "Low"
      elif score <= 11:
        return "Medium"
      else:
        return "High"
    
    dimension_results = {}

    for dimension, score in dimension_scores.items():

      dimension_results[dimension] = {
          'score': score,
          'band': get_band(score)
      }

    return render(request, 'result.html', {
      'participant': participant,
      'overall_score': total_score,
      'dimension_results': dimension_results
    })

  return render(request, 'index.html', {
      'questions': questions
  })

def result(request):
  return render(request, 'result.html')