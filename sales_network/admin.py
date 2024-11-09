from django.contrib import admin

from sales_network.models import Product, NetworkObject


# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """ Admin interface for accessing the product models. """

    list_display = ('id', 'name', 'model')
    search_fields = ('name', 'model')
    list_filter = ('name', 'model')


@admin.register(NetworkObject)
class NetworkObjectAdmin(admin.ModelAdmin):
    """ Admin interface for network object models."""

    list_display = ('id', 'name', 'supplier',)
    list_display_links = ("name",)
    search_fields = ('name',)
    list_filter = ('supplier', 'city',)
    actions = ("pay_off_debt",)

    def pay_off_debt(self, request, queryset):
        """ Method for paying off the debt to the supplier. """

        queryset.update(debt=0)

    pay_off_debt.short_description = "Списать задолженность"
