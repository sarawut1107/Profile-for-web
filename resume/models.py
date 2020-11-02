from django.db import models

# Create your models here.
class resume(models.Model):
    title = models.CharField(max_length=500)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class comment(models.Model):
    title = models.CharField(max_length=500)
    comment = models.TextField()
    date_created = models.DateField(auto_now=True)
    resume = models.ForeignKey(resume, on_delete=models.CASCADE, default=2)

    def __str__(self):
        return self.title