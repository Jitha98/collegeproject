from django.contrib import messages, auth
from django.contrib.auth.models import User

from django.shortcuts import render, redirect

from collegeapp.models import student


# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('CollegeForm')
            print("login")

        else:
            messages.info(request, "Invalid credentials")
            return redirect('login')
    return render(request, "login.html")


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']

        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username Taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email Taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password, first_name=first_name,
                                                last_name=last_name,
                                                email=email)
                user.save()
                return redirect('login')
        else:
            messages.info(request, "password not matched")
            return redirect('register')
        return redirect('/')
    return render(request, "register.html")


def CollegeForm(request):
    return render(request, "CollegeForm.html")
    return redirect('formstudent')


def formstudent(request):
    if request.method == "POST":
        name = request.POST['name']
        dob = request.POST['dob']
        age = request.POST['age']
        gender = request.POST['gender']
        phno = request.POST['phno']
        email = request.POST['email']
        address = request.POST['address']
        department = request.POST['department']
        courses = request.POST['courses']
        purposes = request.POST['purposes']
        materials = request.POST['materials']
        formsstudent = student(name=name, dob=dob, age=age, gender=gender, phno=phno, email=email,
                               address=address, department=department, courses=courses, purposes=purposes,
                               materials=materials)
        formsstudent.save()
        return render(request, 'formstudent.html')
    else:
        return render(request, 'formstudent.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
