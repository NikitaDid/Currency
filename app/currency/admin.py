from django.contrib import admin
from app.currency.models import Rate, ContactUs, Source


@admin.register(Rate)
class RateAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'buy',
        'sell',
        'change_type',
        'source',
        'created',
    )
    list_filter = (
        'change_type',
        'created',
        'source',
    )
    search_fields = (
        'buy',
        'sell',
        'source',
    )
    readonly_fields = (
        'buy',
        'sell',
    )

    def has_delete_permission(self, request, obj=None):
        return True

    def has_add_permission(self, request):
        return True

    def has_change_permission(self, request, obj=None):
        return True


@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'email',
        'subject',
        'message',
    )
    list_filter = (
        'email',
    )
    search_fields = (
        'email',
        'subject',
        'message',
    )

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False


@admin.register(Source)
class SourceAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'source_url',
        'source_name',
        'created',
    )
    list_filter = (
        'source_url',
        'source_name',
    )
    search_fields = (
        'source_url',
        'source_name',
    )

    def has_delete_permission(self, request, obj=None):
        return True

    def has_add_permission(self, request):
        return True

    def has_change_permission(self, request, obj=None):
        return True
