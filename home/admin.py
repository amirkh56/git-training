from django.contrib import admin
from .models import Person, Answer, Question

admin.site.register(Person)
admin.site.register(Question)
admin.site.register(Answer)