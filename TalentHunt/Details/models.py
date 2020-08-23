from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class IndividualSkills(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialization = models.TextField()
    pastexp = models.TextField()
    workexpec = models.TextField()
    bio = models.TextField()
    rating = models.IntegerField(default=0)

class IndividualSkillSet(models.Model):
    indiskills = models.ForeignKey(
        IndividualSkills,
        on_delete= models.CASCADE,
        related_name= 'skillset'
    )
    description = models.CharField(max_length=50)
    
