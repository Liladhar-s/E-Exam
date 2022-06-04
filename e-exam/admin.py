Skip to content
Search or jump to…
Pull requests
Issues
Marketplace
Explore
 
@Liladhar-s 
vitorfs
/
code-exam
Public
Code
Issues
Pull requests
Actions
Projects
Wiki
Security
Insights
code-exam/exams/admin.py /
@vitorfs
vitorfs changed encoding
Latest commit 9f127c8 on Feb 8, 2013
 History
 1 contributor
35 lines (30 sloc)  1.33 KB
   
﻿# -*- coding: utf-8 -*-
from exams.models import Exam, Question, Answer, ExamSubject, QuestionSubject, QuestionDificulty, UserExam
from django.contrib import admin

class AnswerInline(admin.TabularInline):
    model = Answer
    fields = ['letter', 'answer', 'correct']
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question','subject','type','dificulty','active']
    list_filter = ['type','dificulty','active']
    inlines = [AnswerInline]
    search_fields = ['question', 'subject__subject']

class UserExamAdmin(admin.ModelAdmin):
    fields = ['user', 'exam', 'expire_date']
    list_display = ['id', 'user', 'exam', 'expire_date', 'get_status', 'has_finished', 'has_expired']
    list_filter = ['expire_date']
    date_hierarchy = 'expire_date'
    search_fields = ['user__username', 'user__first_name', 'user__last_name', 'exam__name']

class ExamAdmin(admin.ModelAdmin):
    filter_horizontal = ['questions']
    list_display = ['name', 'expire_date', 'subject', 'duration']
    date_hierarchy = 'expire_date'
    search_fields = ['name']
    list_filter = ['expire_date', 'subject']

admin.site.register(Exam, ExamAdmin)
admin.site.register(ExamSubject)
admin.site.register(Question, QuestionAdmin)
admin.site.register(QuestionSubject)
admin.site.register(QuestionDificulty)
admin.site.register(UserExam, UserExamAdmin)
© 2022 GitHub, Inc.
Terms
Privacy
Security
Status
Docs
Contact GitHub
Pricing
API
Training
Blog
About
Loading complete
