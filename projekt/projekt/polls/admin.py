from django.contrib import admin

from .models import Question, Choice, Post, Comment

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Post)
admin.site.register(Comment)
