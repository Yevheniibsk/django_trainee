from django.db import models

class Blogpost(models.Model):
    # title = models.
    text = models.CharField(max_length=200) 
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

class Entry(models.Model):
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    title = models.ForeignKey (Blogpost, on_delete=models.CASCADE)

    class Meta: 
        verbose_name_plural = 'entries'

    def __str__(self):
            if len(self.text)<50:
                return self.text 
            else:  
                return f"{self.text[:50]}..."        