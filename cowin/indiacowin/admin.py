from django.contrib import admin

# Register your models here.

from .models import CowinData


class CowinDataAdmin(admin.ModelAdmin):
    list_display = [
        'center_id', 'name', 'state', 'pincode', 'fee_type', 'fee',
    ]


admin.site.register(CowinData, CowinDataAdmin)
