from django.contrib import admin
from about.models import Aboutme
from django_summernote.admin import SummernoteModelAdmin    
# Register your models here.
@admin.register(Aboutme)
class AboutmeAdmin(SummernoteModelAdmin):

    summernote_fields = ('content',)