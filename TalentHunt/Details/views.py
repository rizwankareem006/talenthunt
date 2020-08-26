from django.shortcuts import render,redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .models import IndividualSkills, IndividualSkillSet
from django.contrib.auth.models import User
from django.http import JsonResponse
from .datastructure import CardDetails, PageNumber, ProfileDetails

# Create your views here.
def signout(request):
    logout(request)
    return redirect('Registration:Login')

@login_required
def indiskills(request):
    if request.method == "POST":
        skillset = request.POST.getlist('skillset[]')
        valid = True
        if valid:
            iskills = IndividualSkills(user = request.user, specialization = request.POST['specialization'], pastexp = request.POST['pastexp'], workexpec = request.POST['workexpec'], bio = request.POST['bio'])
            iskills.save()
            for i in skillset:
                obj = iskills.skillset.create(description = i)
                obj.save()
            response = {
            'status':0,
            'message':'OK',
            }
            return JsonResponse(response)
    return render(request,'Details/indiskills.html')

@login_required
def feed(request,page=1):
    user = User.objects.get(username = request.user)
    if user.groups.filter(name="IndividualTalent").exists():
        skilldetails = IndividualSkills.objects.all().order_by("-rating")
        start = 10*(page-1)
        end = start + 10
        carddet = []
        for i in range(start, min(len(skilldetails),end)):
            item = skilldetails[i]
            uobj = User.objects.get(username = item.user)
            skset = list(item.skillset.all())
            cd = CardDetails(item.user,uobj.get_full_name(),skset,item.workexpec, item.rating)
            carddet.append(cd)
        nop = len(skilldetails)//10
        page_number = PageNumber(page)
        context = {'page_number':page_number, 'carddet':carddet}
        return render(request,'Details/feed.html',context = context)
    else:
        pass
    """return render(request,'Details/feed.html')"""

@login_required
def profile(request,username):
    if request.method == "POST":
        pass
    else:
        user = User.objects.get(username = request.user)
        pd = ProfileDetails(user)
        context = {'pd':pd}
        return render(request,'Details/profile.html', context=context)

@login_required
def profileupdate(request, username):
    user = User.objects.get(username = request.user)
    if request.method == "POST":
        if user.groups.filter(name="IndividualTalent").exists():
            user.first_name = request.POST['firstname']
            user.last_name = request.POST['lastname']
            user.email = request.POST['email']
            user.extuser.gender = request.POST['gender']
            user.extuser.mobile = request.POST['mobile']
            user.extuser.dob = request.POST['dob']
            li = request.POST.getlist('skillset[]')
            indiskills = IndividualSkills.objects.get(user=user)
            indiskills.skillset.all().delete()
            for i in li:
                item = IndividualSkillSet.objects.create(indiskills = indiskills, description=i)
                item.save()
            user.individualskills.specialization = request.POST['specialization']
            user.individualskills.pastexp = request.POST['pastexp']
            user.individualskills.workexpec = request.POST['workexpec']
            user.individualskills.bio = request.POST['bio']
            user.individualskills.save()
            user.extuser.save()
            user.save()
            response = {
                'status':0,
                'message':"Profile Updated Successfully!"
            }
            return JsonResponse(response)