from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.decorators import login_required
from reminder.models import Details
import datetime
# import time
# import schedule
# import sched, time


# Create your views here.

def home(request):
    return render(request,"home.html")

def signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        email = request.POST["email"]
        Password1 = request.POST["Password1"]
        Password2 = request.POST["Password2"]

        if Password1 != Password2:
            messages.error(request,"Your password not match")
            return redirect('/')

        myuser = User.objects.create_user(username,email,Password1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request,"user successfully created")
        return redirect("/")
    
    else:
        return HttpResponse("404 error")


def login_user(request):
    if request.method == "POST":
        username = request.POST["loginusername"]
        password = request.POST["loginPassword"]

        user = authenticate(username=username,password=password)

        if user is not None:
            login(request,user)
            messages.success(request,"user successfully login")
            return redirect("/")
        else:
            messages.error(request,"Invalid credentials")
            return redirect("/")
        
    else:
        return HttpResponse("404 error")

def logout_user(request):
    logout(request)
    messages.success(request,"user successfully logout")
    return redirect("/")

@login_required(login_url="/")
def task(request):
    if request.method == "POST":
        if request.POST.get('context') and request.POST.get('datetime'):
            data = Details()
            data.detail = request.POST.get('context')
            data.datetime = request.POST.get('datetime')
            data.user = request.user
            data.save()
            messages.success(request,"Your task has been created")
            return render(request,"task.html")
        else:
            messages.error(request,"Fill all the details")
            return render(request,"task.html")
    else:
        return render(request,"task.html")

@login_required(login_url="/")
def view(request):
    log_user = request.user
    alldata = Details.objects.filter(user=log_user)
    context = {'alldata':alldata}
    return render(request, "view.html",context)


def delete(request, id):
     data = Details.objects.get(sno=id)
     data.delete()
     return redirect("/view")


def update(request, id):
        data_task = Details.objects.get(sno=id)
        context = {'info':data_task}
        return render(request,"update.html",context)

def update_record(request,id):
    if request.method == "POST":
        data = Details.objects.get(sno=id)
        data.detail = request.POST.get('context')
        data.datetime = request.POST.get('datetime')
        data.save()
        messages.success(request,"Successfully updated task")
        return redirect("/view")
    else:
        return HttpResponse("404 error")


    

def search(request):
    query = request.GET['search']
    if len(query) == 0:
        alltask = Details.objects.none()
    elif len(query) > 70:
        alltask = Details.objects.none()
    else:
        alltasktitle = Details.objects.filter(detail__icontains=query)
        alltasktime = Details.objects.filter(datetime__icontains=query)
        alltask = alltasktitle.union(alltasktime)
    
    if alltask.count() == 0:
        messages.warning(request,"No result found.Please check The spelling correctly.")

    context = {'alltask':alltask, 'query':query}
    return render(request,'search.html',context)



# now = datetime.datetime.now()
# time = Details.objects.all()
# now.isoformat()
# while (now == time):
#     print('send message')

# def date(request):
#     now = datetime.datetime.now()
#     now_s = now.strftime("%Y-%m-%d"+'T'+"%H:%M")
#     print(now_s)
#     time = Details.objects.values_list('datetime',flat=True)
#     print(time)
#     if now_s in time:
#         print("sending_email")
#         t = Details.objects.filter(datetime=time)
#         print(str(t))
#         print(t.user)
#         return redirect("/")
    
#     return redirect("/")

# def date(request):
#     user = User.objects.get(username="s")
#     print(user.email)
#     return redirect("/")
# while True:
#     now = datetime.datetime.now()
#     now_s = now.strftime("%Y-%m-%d"+'T'+"%H:%M")
#     now_s = str(now_s)
    
#     time = Details.objects.values_list('datetime',flat=True)
# while now_s in time:
#     print('hi')
#     t = Details.objects.get(datetime=now_s)
#     name = str(t.user)
#     for_mail = User.objects.get(username=name)
#     mail = for_mail.email
#     print(mail)
#     break
    

# s = sched.scheduler(time.time, time.sleep)
# def do_something(sc): 
#     print("Doing stuff...")
#     # do your stuff
#     s.enter(60, 1, do_something, (sc,))

# s.enter(60, 1, do_something, (s,))
# s.run()

# import schedule
# import time

# def job():
#     print("I'm working...")

# schedule.every(10).seconds.do(job)

# while True:
#     schedule.run_pending()
#     time.sleep(1)

