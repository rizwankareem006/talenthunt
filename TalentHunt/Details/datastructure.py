from django.contrib.auth.models import User
class CardDetails:
    def __init__(self, user, sks, skset):
        self.username = user.username
        self.fullname = user.get_full_name()
        self.skillset = list(skset)
        self.workexpec = sks.workexpec
        self.rating = sks.rating
    
class PageNumber:
    def __init__(self, currentPage):
        self.current_page = currentPage
    
    @property
    def nextPage(self):
        return self.current_page+1
    
    @property
    def previousPage(self):
        return self.current_page-1

class ProfileDetails:
    def __init__(self,user):
        self.username = user.username
        self.firstname = user.first_name
        self.lastname = user.last_name
        self.email = user.email
        self.mobile = user.extuser.mobile
        self.gender = user.extuser.gender
        self.dob = str(user.extuser.dob)
        self.skillset = list(user.skills.skillset.all())
        self.specialization = user.skills.specialization
        self.pastexp = user.skills.pastexp
        self.workexpec = user.skills.workexpec
        self.bio = user.skills.bio
        self.rating = user.skills.rating
    
class TeamProfile:
    def __init__(self, team):
        self.primary_key = team.pk
        self.teamname = team.teamname
        self.teamdescription = team.teamdesc.teamdescription
        self.teammotive = team.teamdesc.teammotive
        self.teammembers = list(team.members.all())
        
class ProfileTeamList:
    def __init__(self, teams):
        self.primary_keys = []
        self.teamname = []
        for item in teams:
            self.primary_keys.append(item.team.pk)
            self.teamname.append(item.team.teamname)
        
class TeamProfileList:
    def __init__(self,users):
        self.usernames = []
        self.fullnames = []
        for item in users:
            self.usernames.append(item.user.username)
            self.fullnames.append(item.user.get_full_name())

class ProfileRequests:
    def __init__(self,user):
        self.requests = []
        self.primary_keys = []
        teams = user.uruser.all()
        for item in teams:
            self.requests.append(item.team.teamname)
            self.primary_keys.append(item.team.pk)

class TeamRequests:
    def __init__(self,team):
        self.requests = []
        self.usernames = []
        users = team.trteam.all()
        for item in users:
            self.requests.append(item.user.get_full_name())
            self.usernames.append(item.user.username)