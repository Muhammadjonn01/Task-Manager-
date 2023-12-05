from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    priority = models.PositiveSmallIntegerField(default=1)
    is_done = models.BooleanField(default=False)
    created_at = models.DateField(auto_now=True)
    due_date = models.DateField(null=True)
    title = models.CharField(max_length=30)
    description = models.TextField()


    def __str__(self):
        return f"{self.user}: {self.title} ({self.due_date}) {self.description} {self.priority} {self.created_at} {self.is_done} "  

    def get_absolute_url(self):
        return "/tasks/%i/" % self.id