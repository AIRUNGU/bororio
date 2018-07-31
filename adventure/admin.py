from django.contrib import admin
from adventure import models as a_models

class AdvReportsAdmin(admin.ModelAdmin):
	list_display = ['title','body','price','created','modified']


admin.site.register(a_models.AdvReports,AdvReportsAdmin)
admin.site.register(a_models.Category)
admin.site.register(a_models.Safaris)