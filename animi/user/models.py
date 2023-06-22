from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


# Создание модели профиля пользователя
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(null=True, blank=True, upload_to="images/")
    profile_banner = models.ImageField(null=True, blank=True, upload_to="images/")
    profile_bio = models.CharField(null=True, blank=True, max_length=200)

    def __str__(self):
        return self.user.username


# Создание профиля при регистрации нового пользователя
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()


post_save.connect(create_profile, sender=User)
