
    from django.db import models
    from django.contrib.auth.models import AbstractUser

    class CustomUser(AbstractUser):
        pass

    class Group(models.Model):
        name = models.CharField(max_length=100)
        users = models.ManyToManyField(CustomUser, related_name='groups')

        def __str__(self):
            return self.name

    class Message(models.Model):
        content = models.TextField()
        sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='sent_messages')
        group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='messages')
        timestamp = models.DateTimeField(auto_now_add=True)

        def __str__(self):
            return f'Message from {self.sender} in {self.group}'
  </boltAction