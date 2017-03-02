from django.contrib import admin

from .models import NSESetting,ScreenerSetting,IndianStockIdeasAction,FeaturedStock,ScreenerData
from .views import executescript
import datetime
def fetchData(modeladmin, request, queryset):
    queryset.update(executed_date=datetime.datetime.now().date())
    executescript(queryset[0].action)
fetchData.short_description = "Run Selected Job"
  
class IndianStockIdeasActionAdmin(admin.ModelAdmin):
    list_display = ('action', 'executed_date')
    actions = [fetchData]
  
admin.site.register(NSESetting)
admin.site.register(FeaturedStock)
admin.site.register(ScreenerSetting)
admin.site.register(ScreenerData)
admin.site.register(IndianStockIdeasAction, IndianStockIdeasActionAdmin)