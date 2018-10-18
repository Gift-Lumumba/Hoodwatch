from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Neighbourhood(models.Model):
  '''
  class that contains Neighbourhood properties
  '''
  name = models.CharField(max_length=30,null=True,blank=True)
  location = models.CharField(max_length=30,null=True,blank=True)
  occupants_count = models.PositiveIntegerField()
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def save_neighbourhood(self):
    self.save()

  def update_neighbourhood(self):
    self.update()

  def update_occupants(self):
    self.update()

  def delete_neighbourhood(self):
    self.delete()

  @classmethod
  def get_neighbourhoods(cls):
    neighbourhoods = Neighbourhood.objects.all()
    return neighbourhoods

  @classmethod
  def find_neighbourhood_by_id(cls,id):
    neighbourhood = Neighbourhood.objects.get(neighbourhood_id=id)
    return neighbourhood

  



class Profile(models.Model):
  '''
  class that contains User properties
  '''
  name = models.CharField(max_length=30,null=True,blank=True)
  email = models.EmailField()
  neighbourhood = models.ForeignKey(Neighbourhood,on_delete=models.CASCADE,blank=True,null=True)
  user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

  def __str__(self):
    return self.name

  @receiver(post_save, sender=User)
  def create_user_profile(sender, instance, created, **kwargs):
          if created:
                  Profile.objects.create(user=instance)

  @receiver(post_save, sender=User)
  def save_user_profile(sender, instance, **kwargs):
          instance.profile.save()

  post_save.connect(save_user_profile, sender=User)

  @classmethod
  def get_profile(cls):
    profile = Profile.objects.all()
    return profile

  @classmethod
  def get_profile_by_id(cls,id):
    user_profile = Profile.objects.get(user=id)
    return user_profile


class Business(models.Model):
  name = models.CharField(max_length=30)
  email = models.EmailField()
  user = models.ForeignKey(User)
  neighbourhood = models.ForeignKey(Neighbourhood)

  def __str__(self):
    self.name

  def save_business(self):
    self.save

  def delete_business(self):
    self.delete

  def update_business(self):
    self.update

  @classmethod
  def find_business(cls,id):
    business = Business.object.get(id=id)
    return business

  @classmethod
  def search_by_title(cls,search_term):
    business = cls.objects.filter(title__icontains=search_term)
    return business