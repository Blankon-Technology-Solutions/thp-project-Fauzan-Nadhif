from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.db import models
from django.dispatch import receiver
from django.utils import timezone
from django.db.models.signals import post_save, post_delete

class Todo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    owner = models.ForeignKey('users.User', related_name='todos', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    def _build_message(self, message_type):
        return {
            "type": "recieve_todo",
            "message": {
                "action": message_type,
                "data": {
                    "id": str(self.id),
                    "title": self.title,
                    "description": self.description,
                    "owner_id": str(self.owner.id)
                },
            },
        }

    def _send_message(self, group_name, message):
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(group_name, message)

@receiver(post_save, sender=Todo)
def notify_on_save(sender, instance, created, **kwargs):
    action = "update"
    if created:
        action = "create"

    message = instance._build_message(action)

    instance._send_message(str(instance.owner.id), message)

@receiver(post_delete, sender=Todo)
def notify_on_delete(sender, instance, *args, **kwargs):
    message = instance._build_message("delete")
    instance._send_message(str(instance.owner.id), message)
