from django.db import models

class Article(models.Model):
    author = models.ForeignKey(
    'auth.user' ,
     on_delete=models.CASCADE ,
    )
    title = models.CharField(max_length = 200)
    text = models.TextField()


    def __str__(self):
        return self.title
