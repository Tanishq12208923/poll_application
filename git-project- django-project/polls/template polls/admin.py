from django.contrib import admin
from .models import Question, Choice

class ChoiceInLine(admin.TabularInline):
	model = Choice
	extra = 3

class QuestionAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,		{'fields': ['question_text']}),
		('Date Information', {'fields': ['pub_date']})
	]
	inlines = [ChoiceInLine]
	list_filter = ['question_text']
	search_fields = ['question_text']
	list_display = ('question_text', 'pub_date', 'was_published_recently')

admin.site.register(Question, QuestionAdmin)
