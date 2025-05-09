from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Order

# Signal to notify staff on order status update
@receiver(post_save, sender=Order)
def notify_staff(sender, instance, **kwargs):
    print(f"Order {instance.order_id} status updated to {instance.status}")