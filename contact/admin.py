from django.contrib import admin
from .models import ContactModel
from .forms import ContactForm


class ContactFormAdmin(admin.ModelAdmin):
    
    list_display = [
        'name',
        'email',
        'subject',
        'created_at'
    ]

    search_fields = [
        'name',
        'email',
        'subject'
    ]

    list_filter = [
        'category',
        'created_at'
    ]


admin.site.register(ContactModel, ContactFormAdmin)
