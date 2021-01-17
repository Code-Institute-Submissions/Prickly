from django.contrib import admin
from .models import DeliveryType, Order, OrderLine


@admin.register(DeliveryType)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'limit', 'const', 'rate')


class OrederLineAdminInLine(admin.StackedInline):
    model = OrderLine
    readonly_fields = ('line_total',)
    extra = 1
    min_num = 1


class OrderAdmin(admin.ModelAdmin):
    inlines = [OrederLineAdminInLine]
    readonly_fields = (
        'order_number',
        'order_date',
        'phone_regex',
        'full_name',
        'est_dispatch_dte',
        'est_deliery_dte',
        'delivery_cost',
        'subtotal',
        'total',
    )

    fieldsets = [
        ('', {'fields': ['order_number']}),
        ('Personal Details',
            {'fields': ['first_name',
                        'last_name',
                        'phone_number',
                        'email',
                        'address_line_1',
                        'address_line_2',
                        'city',
                        'region',
                        'country',
                        'postcode'
                        ]}),
        ('Order Detail', {'fields': ['delivery_type']})
    ]

    list_display = (
        'order_number',
        'full_name',
        'order_date',
        'delivery_type',
        'total',
    )

    date_hierarchy = 'order_date'


admin.site.register(Order, OrderAdmin)
