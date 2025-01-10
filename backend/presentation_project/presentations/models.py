from django.db import models
from django.contrib.auth.models import User

class PDF(models.Model):
    file = models.FileField(upload_to='pdfs/')

class Annotation(models.Model):
    pdf = models.ForeignKey(PDF, related_name='annotations', on_delete=models.CASCADE)
    x = models.FloatField()
    y = models.FloatField()
    text = models.TextField()

class Presentation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Связь с пользователем
    title = models.CharField(max_length=255)
    pdf_file = models.FileField(upload_to='presentations/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Drawing(models.Model):
    presentation = models.ForeignKey(Presentation, on_delete=models.CASCADE)
    user = models.CharField(max_length=255)
    drawing_data = models.JSONField()  # Храните данные о рисовании
    created_at = models.DateTimeField(auto_now_add=True)