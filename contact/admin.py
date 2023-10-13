from django.contrib import admin
from .models import Contact


admin.site.register(Contact)

#class ContactFormAdmin(admin.ModelAdmin):
    
#    list_display = [
#        'name',
#        'email',
#       'subject',
#        'created_at'
#    ]
#
#    search_fields = [
#        'name',
#        'email',
#        'subject'
#    ]
#
#    list_filter = [
#        'category',
#        'created_at'
#    ]
#
#
#admin.site.register(ContactModel, ContactFormAdmin)
