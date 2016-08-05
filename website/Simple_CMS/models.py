# -*- coding: utf-8 -*-
from django.db import models
from django.forms import ModelForm
import re

# Create your models here.

class Article(models.Model):
    id = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=100)
    Content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Title

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['Title', 'Content']

    def clean_message(self):
        content = self.cleaned_data['Content']

        if re.match("[\u4e00-\u9fa5]+", message):
            num_words = len(message)
        else :
            num_words = len(message.split())

        if num_words < 4:
            raise forms.ValidationError("Not enough words! You have to leave at least 4 words!")
        return content
