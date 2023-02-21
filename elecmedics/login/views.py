from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template import loader
import datetime
from .models import Users

# def index(request):
#     return HttpResponse(Users.objects.get())
#     now = datetime.datetime.now()
#     return HttpResponse("Hello, world. You're at the login app." + str(now))

def index(request):
    # user = Users.objects.get(email="aizaz@test.com").password
    # return HttpResponse(user)
    if checkSession(request):
        return redirect('dashboard')
    elif request.POST.get('email'):
        #login here
        email = request.POST.get('email')
        password = request.POST.get('password')
        # password = "12"
        try:
            queryResult = Users.objects.get(email=email, password=password)
        except:
            queryResult = ""
        if queryResult:
            request.session['USER_EMAIL'] = email
            return redirect('dashboard')
            # return HttpResponse(queryResult)
        # else:
        #     return HttpResponse("not found")
        
    template = loader.get_template('login/index.html')
    context = {
        'attempt': "1",
    }
    return HttpResponse(template.render(context, request))

def dashboard(request):
    # return HttpResponse(Users.objects.all()[0].password + ' : ' + Users.objects.all()[0].email)
    if checkSession(request):
        # return redirect("logout")
        return redirect("/app")
        # return HttpResponse(str(request.session['USER_EMAIL']))
    else:
        return redirect("/")

def checkSession(request):
    if "USER_EMAIL" in request.session:
        return True
    else:
        return False

def logout(request):
    try:
        del request.session['USER_EMAIL']
    except:
        return redirect('/')
    return redirect('/')