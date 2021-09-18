from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import Restaurant
from apps.plans.models import Plan
from apps.kitchens.models import Kitchen


# POST INIT SLUG
@receiver(pre_save, sender=Restaurant)
def createFreshSlug(sender, instance, **kwargs):
    instance.create_slug()


# CREATE PLAN
@receiver(post_save, sender=Restaurant)
def createRestaurantPlan(sender, instance, created, **kwargs):
    if created:
        Plan.objects.create(
            owner=instance.owner,
            restaurant=instance,
        )
        Kitchen.objects.create(
            restaurant=instance,
        )
