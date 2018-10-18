from django.db import models

from django.contrib.auth.models import User

from django.db.models.signals import post_save

from django.dispatch import receiver


# Create your models here.

class Neighbourhood(models.Model):
    """
    class for creating neighbourhood
    """
    name = models.CharField(max_length=2000)
    location = models.CharField(max_length=2000)

    def create_neighbourhood(self):
        """
        method to save project images
        :return:
        """
        self.save()

    @classmethod
    def find_neighbourhood(cls, neighbourhood_id):
        """
        method to get image by id
        :return:
        """
        projects = cls.objects.filter(id=neighbourhood_id)
        return projects

    def delete_neighbourhood(self):
        """
        method to delete image
        :return:
        """
        self.delete()


class User(models.Model):
    """
    class for user profile
    """
    avatar = models.ImageField(upload_to='media/', null=True)
    name = models.CharField(max_length=2000)
    id = models.IntegerField()
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user')
    email = models.CharField(max_length=2000)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user")
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE, related_name='design', null=True)

    # sender is source of signal
    @receiver(post_save, sender=User)
    def create_profile(sender, instance, created, **kwargs):
        """
        method to create profile
        :return:
        """
        if created:
            User.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        """
        method to save profile
        :return:
        """
        instance.user.save()


class Business(models.Model):
    """
    class for creating businesses
    """
