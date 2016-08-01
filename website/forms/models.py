from django.db import models
from django.forms import ModelForm

# Create your models here.

class Message(models.Model):
    id = models.AutoField(primary_key=True)
    subject = models.CharField(max_length=100)
    email = models.EmailField(max_length=30, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject

class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['subject', 'email', 'message']

    def clean_message(self):
        message = self.cleaned_data['message']
        num_words = len(message.split())
        if num_words < 4:
            raise forms.ValidationError("Not enough words! You have to leave at least 4 words!")
        return message
