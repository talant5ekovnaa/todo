from django.db import models


class ToDo(models.Model):
    text = models.CharField(max_length=100)
    created_at = modele.DataField(auto_now_add=True)