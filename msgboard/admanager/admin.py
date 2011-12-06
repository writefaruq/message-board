from django.contrib import admin

from msgboard.admanager.models import Client, Ad, Transaction

admin.site.register(Client)
admin.site.register(Ad)
admin.site.register(Transaction)
    