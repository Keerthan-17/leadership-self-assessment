from django.db import models

# Create your models here.
class Question(models.Model):
  
  DIMENSIONS = [
    ('Decision Making', 'Decision Making'),
    ('Team Communication', 'Team Communication'),
    ('Strategic Thinking', 'Strategic Thinking'),
    ]

  question_text = models.TextField()

  dimension = models.CharField(
    max_length = 100,
    choices = DIMENSIONS
    )

  def __str__(self):
      return self.question_text


class Participant(models.Model):

  name = models.CharField(max_length=100)
  email = models.EmailField()

  submitted_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
      return self.name


class Response(models.Model):

  OPTIONS = [
      (1, 'Strongly Disagree'),
      (2, 'Disagree'),
      (3, 'Neutral'),
      (4, 'Agree'),
      (5, 'Strongly Agree'),
  ]

  participant = models.ForeignKey(
      Participant,
      on_delete=models.CASCADE
  )

  question = models.ForeignKey(
      Question,
      on_delete=models.CASCADE
  )

  selected_option = models.IntegerField(
      choices=OPTIONS
  )

  def __str__(self):
      return f"{self.participant.name} - {self.question.id}"