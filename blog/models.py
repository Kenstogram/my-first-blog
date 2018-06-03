from django.db import models
from django.utils import timezone

<<<<<<< HEAD

=======
>>>>>>> 37c99181c9a6b95433d60f8c8ef9af5731096435
class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
<<<<<<< HEAD
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
=======
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
>>>>>>> 37c99181c9a6b95433d60f8c8ef9af5731096435

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
