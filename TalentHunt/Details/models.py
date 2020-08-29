from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Skills(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialization = models.TextField()
    pastexp = models.TextField()
    workexpec = models.TextField()
    bio = models.TextField()
    rating = models.IntegerField(default=0)

class SkillSet(models.Model):
    skills = models.ForeignKey(
        Skills,
        on_delete= models.CASCADE,
        related_name= 'skillset'
    )
    description = models.CharField(max_length=50)
    
class Teams(models.Model):
    teamname = models.CharField(max_length = 50)
    def __str__(self):
        return self.teamname
    
    def addMember(self,user):
        self.members.create(self, user)
        self.members.save()

    def removeMember(self,user):
        self.members.filter(team=self, user=user)[0].delete()
        if self.members.all().length == 0:
            self.delete()
    
class TeamMembers(models.Model):
    team = models.ForeignKey(
        Teams,
        on_delete= models.CASCADE,
        related_name= "members"
    )
    user = models.ForeignKey(
        User,
        on_delete= models.CASCADE,
        related_name= "users"
    )

class TeamDesc(models.Model):
    team = models.OneToOneField(
        Teams,
        on_delete= models.CASCADE
    )
    teamdescription = models.TextField()
    teammotive = models.TextField()
    