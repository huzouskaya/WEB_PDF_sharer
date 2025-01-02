from django.db import models

class Presentation(models.Model):
    title = models.CharField(max_length=255)
    pdf_file = models.FileField(upload_to='presentations/')
    created_at = models.DateTimeField(auto_now_add=True)

class Drawing(models.Model):
    presentation = models.ForeignKey(Presentation, on_delete=models.CASCADE)
    user = models.CharField(max_length=255)
    drawing_data = models.JSONField()  # Храните данные о рисовании
    created_at = models.DateTimeField(auto_now_add=True)