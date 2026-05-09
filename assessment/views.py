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

    for question in questions:

      answer = request.POST.get(f'question_{question.id}')

      if answer:

        Response.objects.create(
          participant = participant,
          question = question,
          selected_option = int(answer)
        )

        total_score += int(answer)

    return render(request, 'result.html', {
        'score': total_score,
        'participant': participant
    })

  return render(request, 'index.html', {
      'questions': questions
  })

def result(request):
  return render(request, 'result.html')