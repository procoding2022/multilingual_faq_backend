from django.contrib import admin
from .models import FAQ

class FAQAdmin(admin.ModelAdmin):
    list_display = ('question',)
    search_fields = ('question',)

admin.site.register(FAQ, FAQAdmin)
