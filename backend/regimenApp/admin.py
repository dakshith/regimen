from django.contrib import admin
from .models import *
# Register your models to admin site, then you can add, edit, delete and search your models in Django admin site.

class QuestionMasterAdmin(admin.ModelAdmin):
    # a list of displayed columns name.
    list_display = ['question', 'shortName']

class OptionMasterAdmin(admin.ModelAdmin):
    # a list of displayed columns name.
    list_display = ['questionId', 'option', 'optionWeight']

class ResponseDataAdmin(admin.ModelAdmin):
    # a list of displayed columns name.
    list_display = ['confidence', 'penetration', 'intercourse', 'completion', 'satisfaction', 'score', 'avgScore']

admin.site.register(QuestionMaster, QuestionMasterAdmin)
admin.site.register(OptionMaster, OptionMasterAdmin)
admin.site.register(ResponseData, ResponseDataAdmin)
