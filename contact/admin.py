from django.contrib import admin
from .models import Contact


class ContactFormAdmin(admin.ModelAdmin):
    
    list_display = [
        'email',
        'subject',
        'message',
        'created_at',
    ]

    search_fields = [
        'email',
        'created_at',
    ]

    list_filter = ('email', 'created_at')


admin.site.register(Contact, ContactFormAdmin)
