from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import OrderLineItem
@receiver(post_save, sender=OrderLineItem)
def Update_On_Save(sender, instance, created, **kwargs):
    """
    Update order total on lineitem update
    """
    instance.order.update_total()

@receiver(post_delete, sender=OrderLineItem)
def Delete_On_Save(sender, instance, **kwargs):
    """
    Update order total on lineitem delete
    """
    instance.order.update_total()