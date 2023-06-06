from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=25)
    password = models.CharField(max_length=16)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.username


class Session(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.user.username} | {self.start_date} | {self.end_date}'





