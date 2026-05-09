from django.contrib import admin
from .models import Question, Participant, Response

# Register your models here.
admin.site.register(Question)
admin.site.register(Participant)
admin.site.register(Response)