from django.contrib import admin
from .models import Question, Participant, Response, AssessmentResult

# Register your models here.
admin.site.register(Question)
admin.site.register(Participant)
admin.site.register(Response)
admin.site.register(AssessmentResult)