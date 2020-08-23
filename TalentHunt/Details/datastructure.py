class CardDetails:
    def __init__(self, username, fullname, skillset, workexpec, rating):
        self.username = username
        self.fullname = fullname
        self.skillset = skillset
        self.workexpec = workexpec
        self.rating = rating
    
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
        self.gender = user.extuser.gender
        self.mobile = user.extuser.mobile
        self.gender = user.extuser.gender
        self.dob = user.extuser.dob
        self.category = user.extuser.category
        self.skillset = user.individualskills.skillset.all()
        self.specialization = user.individualskills.specialization
        self.pastexp = user.individualskills.pastexp
        self.workexpec = user.individualskills.workexpec
        self.rating = user.individualskills.rating
    

