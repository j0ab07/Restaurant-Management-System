from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Order

@receiver(post_save, sender=Order)
def notify_staff(sender, instance, **kwargs):
    # Simulation (need database to be implemented for data)
    print(f"Order {instance.order_id} status updated to {instance.status}")