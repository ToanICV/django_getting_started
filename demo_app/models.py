from django.db import models

# Create your models here.
class Responser(models.Model):
    context     = models.CharField(max_length=128,primary_key=True)
    object      = models.CharField(max_length=512)
    app_name    = models.CharField(max_length=64)
    created_at  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.context} {self.object} {self.app_name}'