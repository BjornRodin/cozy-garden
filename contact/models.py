from django.db import models


class ContactModel(models.Model):
    """ Model for contact form """
    class Meta:
        verbose_name = 'Contact'

    CATEGORY_CHOICES = [
        ('General Question', 'General Question'),
        ('Stock Suggestion', 'Stock Suggestion'),
        ('Feedback', 'Feedback'),
        ('Other', 'Other')
    ]

    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES, default='General Question', null=False, blank=False)
    name = models.CharField(max_length=80, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    subject = models.CharField(max_length=50, null=False, blank=False)
    message = models.TextField(max_length=1000, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
