from django.contrib import admin

from app_token_auth.models import AuthToken


@admin.register(AuthToken)
class AuthTokenAdmin(admin.ModelAdmin):
    list_display = ('digest', 'account_type', 'user', 'created', 'expiry',)
    fields = ()
    # raw_id_fields = ('user',)
