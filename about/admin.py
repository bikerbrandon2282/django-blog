from django.contrib import admin
from about.models import Aboutme
from django_summernote.admin import SummernoteModelAdmin    
# Register your models here.
@admin.register(Aboutme)
class AboutmeAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'updated_on')
    search_fields = ['title', 'content']
    list_filter = (('updated_on'),)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)