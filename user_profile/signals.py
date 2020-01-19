from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Student_Detail, Student_Education


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Student_Detail.objects.create(user=instance)
        Student_Education.objects.create(user= instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.student_detail.save()
    instance.student_education.save(force_insert = False)
