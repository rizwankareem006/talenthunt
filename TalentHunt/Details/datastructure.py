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
        
