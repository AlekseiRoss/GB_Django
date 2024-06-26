from django.contrib import admin
from .models import Order


class OrderAdmin(admin.ModelAdmin):
    list_display = ["order_date", "total_amount"]


admin.site.register(Order, OrderAdmin)
