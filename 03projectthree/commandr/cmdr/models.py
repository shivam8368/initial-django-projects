from django.db import models


class cmdr(models.Model):
    text = models.TextField(default = '' )

    def __str__(self):
        return self.text
