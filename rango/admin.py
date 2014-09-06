from django.contrib import admin

from rango.models import Page, Category

# Register your models here.
class PageAdmin(admin.ModelAdmin):
	list_display = ('title','category','url')

admin.site.register(Page,PageAdmin)
admin.site.register(Category)