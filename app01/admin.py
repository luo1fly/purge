from django.contrib import admin
from app01 import models
# Register your models here.

class HistoryAdmin(admin.ModelAdmin):
    list_display = ('sku','pic_url','cleaned_status','cleaned_by','cleaned_at',)
    list_filter = ('cleaned_at',)
    search_fields = ('sku','cleaned_status','cleaned_by__user__username',)

admin.site.register(models.History,HistoryAdmin)
admin.site.register(models.OptUser)