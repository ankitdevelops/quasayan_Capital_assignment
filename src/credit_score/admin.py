from django.contrib import admin

from .models import Answer, CreditScore, Question, UserResponse

admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(UserResponse)
admin.site.register(CreditScore)
