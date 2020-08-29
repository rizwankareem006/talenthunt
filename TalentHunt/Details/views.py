from django.shortcuts import render,redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .models import Skills, SkillSet, Teams, TeamDesc, TeamMembers
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponseNotFound
from .datastructure import CardDetails, PageNumber, ProfileDetails, TeamProfile

# Create your views here.
def signout(request):
    logout(request)
    return redirect('Registration:Login')

@login_required
def skills(request):
    if request.method == "POST":
        skill_list = request.POST.getlist('skillset[]')
        valid = True
        if valid:
            skills = Skills(user = request.user, specialization = request.POST['specialization'], pastexp = request.POST['pastexp'], workexpec = request.POST['workexpec'], bio = request.POST['bio'])
            skills.save()
            for i in skill_list:
                obj = skills.skillset.create(description = i)
                obj.save()
            response = {
            'status':0,
            'message':'OK',
            }
            return JsonResponse(response)
    return render(request,'Details/skills.html')

@login_required
def feed(request,page=1):
    if request.method == "GET":
        skilldetails = Skills.objects.all().order_by("-rating")
        start = 10*(page-1)
        end = start + 10
        carddet = []
        for i in range(start, min(len(skilldetails),end)):
            sks = skilldetails[i]
            uobj = User.objects.get(username = sks.user)
            skset = list(sks.skillset.all())
            cd = CardDetails(uobj,sks,skset)
            carddet.append(cd)
        nop = len(skilldetails)//10
        page_number = PageNumber(page)
        context = {'page_number':page_number, 'carddet':carddet, 'np':nop}
        return render(request,'Details/feed.html',context = context)

@login_required
def profile(request,username):
    if str(request.user) == username:
        user = User.objects.get(username = request.user)
        pd = ProfileDetails(user)
        context = {'pd':pd, 'owner':True}
        print(context)
    else:
        user = User.objects.get(username = username)
        pd = ProfileDetails(user)
        context = {'pd':pd, 'owner':False}
    return render(request,'Details/profile.html', context=context)

@login_required
def profileupdate(request, username):
    if request.method == "POST":
        user = User.objects.get(username = request.user)
        user.first_name = request.POST['firstname']
        user.last_name = request.POST['lastname']
        user.email = request.POST['email']
        user.extuser.gender = request.POST['gender']
        user.extuser.mobile = request.POST['mobile']
        user.extuser.dob = request.POST['dob']
        li = request.POST.getlist('skillset[]')
        skills = Skills.objects.get(user=user)
        skills.skillset.all().delete()
        for i in li:
            item = SkillSet.objects.create(skills = skills, description=i)
            item.save()
        user.skills.specialization = request.POST['specialization']
        user.skills.pastexp = request.POST['pastexp']
        user.skills.workexpec = request.POST['workexpec']
        user.skills.bio = request.POST['bio']
        user.skills.save()
        user.extuser.save()
        user.save()
        response = {
            'status':0,
            'message':"Profile Updated Successfully!"
        }
        return JsonResponse(response)

@login_required
def createteam(request):
    if request.method == "POST":
        teamname = str(request.POST['teamname']).strip()
        teamdescription = str(request.POST['teamdescription']).strip()
        teammotive = str(request.POST['teammotive']).strip()
        if teamname == "":
            error = "Team name cannot be empty!"
            context = {'error':error}
        elif teamdescription == "":
            error = "Team description cannot be empty!"
            context = {'error':error}
        elif teammotive == "":
            error = "Team motive cannot be empty!"
            context = {'error':error}
        else:
            team = Teams.objects.create(teamname = teamname)
            teamdesc = TeamDesc.objects.create(team=team, teamdescription=teamdescription, teammotive=teammotive)
            teamdesc.save()
            team.save()
            return redirect('Details:TeamProfile', team=team.pk)
    else:
        context = {}
    return render(request, 'Details/teamcreation.html', context=context)

@login_required
def teamprofile(request, team):
    user = User.objects.get(username = request.user)
    teamitem = Teams.objects.filter(pk=team)
    if not teamitem.exists():
        return HttpResponseNotFound('<h3>Page not found</h3>')
    else:
        owner = teamitem.members.filter(user = user).exists()
        tp = TeamProfile(teamitem)
        context = {'tp':tp, 'owner':owner}
        return render(request, 'Details/teamprofile.html', context = context)

@login_required
def teamprofileupdate(request, team):
    if request.method == "POST":
        teamitem = Teams.objects.get(pk=team)
        teamdescription = str(request.POST['teamdescription']).strip()
        teammotive = str(request.POST['teammotive']).strip()
        if teamdescription == "":
            error = "Team description cannot be empty!"
            context = {'error':error}
        elif teammotive == "":
            error = "Team motive cannot be empty!"
            context = {'error':error}
        else:
            teamitem.teamdesc.teamdescription = teamdescription
            teamitem.teamdesc.teammotive = teammotive
            teamitem.teamdesc.save()
            teamitem.save()
            {'success':"Updated Successfully!"}
        return render(request, 'Details/teamprofile.html', context=context)
