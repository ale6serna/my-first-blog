from django.db import models
from django.utils import timezone

class Post(models.Model): #Esta línea define nuesttro modelo (objeto)
    author=models.ForeignKey('auth.User', on_delete=models.CASCADE) #Relación link con otro objeto
    title=models.CharField(max_length=200) #Se define un texto con un número limitado de caracteres
    text=models.TextField() #texto sin límite
    created_date=models.DateTimeField(blank=True, null=True) #Fecha y hora

    def publish(self):
        self.published_date=timezone.now()
        self.save()
    
    def __str__(self):
        return self.title
