import logging
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Reputation


logger = logging.getLogger("audit")

@receiver([post_save, post_delete], sender=Reputation)
def log_reputation_change(sender, instance, **kwargs):
    action = "created/updated" if kwargs.get("created", False) else "deleted"
    logger.info(f"Reputation {action} for user {instance.user.id}, score={instance.score}")

