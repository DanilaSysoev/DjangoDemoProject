from django.db import models

class Wish(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.TextField(max_length=1024, null=False)
    using_count = \
        models.PositiveIntegerField(null=False, default=0)
    
    def __str__(self):
        return self.text
