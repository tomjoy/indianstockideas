from django.contrib import admin

from .models import NSESetting, MutualFundHolding, ScreenerSetting,MoneyControlMapping, IndianStockIdeasAction,FeaturedStock,ScreenerData, NseData
from .views import executescript
import datetime
def fetchData(modeladmin, request, queryset):
    queryset.update(executed_date=datetime.datetime.now().date())
    executescript(queryset[0].action)
fetchData.short_description = "Run Selected Job"
  
class IndianStockIdeasActionAdmin(admin.ModelAdmin):
    list_display = ('action','status', 'executed_date')
    actions = [fetchData]

class MoneyControlMappingAdmin(admin.ModelAdmin):
    list_display = ('stockname','stockurl', 'sector','urlsplit1','urlsplit2','urlsplit3')
    
class MutualFundHoldingAdmin(admin.ModelAdmin):
    list_display = ('symbol','quarter_mf', 'quarter_1_mf','quarter_2_mf','quarter_3_mf','quarter_4_mf','bought','sold')
  
admin.site.register(NSESetting)
admin.site.register(FeaturedStock)
admin.site.register(ScreenerSetting)
admin.site.register(ScreenerData)
admin.site.register(NseData)
admin.site.register(PublishedData)
admin.site.register(MutualFundHolding,MutualFundHoldingAdmin)
admin.site.register(MoneyControlMapping,MoneyControlMappingAdmin)
admin.site.register(IndianStockIdeasAction, IndianStockIdeasActionAdmin)