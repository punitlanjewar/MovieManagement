from django.shortcuts import render
from django.contrib.auth import authenticate
from django.shortcuts import redirect
from django.contrib.auth.models import User
from MovieApp.models import Movie

# Create your views here.
def home(request):
    return render(request, 'home.html')

def admin_home_page(request):
    return render(request, 'adminhome.html')

def customer_home_page(request):
    return render(request, 'customerhome.html')

def customer_login_page(request):
    if request.method == 'POST':
        user_name = request.POST['txtUsername']
        user_password = request.POST['txtPassword']
        u1 = authenticate(username=user_name, password=user_password)
        if u1 is not None:
            if u1.is_superuser:
                return render(request, 'customerlogin.html', {'Msg': 'User not registered'})
            else:
                return redirect('customer_home')
        else:
            return render(request, 'customerlogin.html', {'Msg': 'Username and Password is not matching'})    
    else:
        return render(request, 'customerlogin.html')
    
def customer_register_page(request):
    if request.method == 'POST':
        user_first_name = request.POST['txtFirstName']
        user_last_name = request.POST['txtLastName']
        user_name = request.POST['txtUsername']
        user_email = request.POST['txtEmail']
        user_contact = request.POST['txtContact']
        user_password = request.POST['txtPassword']
        if User.objects.filter(username=user_name).exists():
            return render(request, 'customerregister.html', {'Msg': 'Username is already taken'})
        elif User.objects.filter(email=user_email).exists():
            return render(request, 'customerregister.html', {'Msg': 'Email is already registered'})
        else:
            u1 = User.objects.create_user(first_name=user_first_name, last_name=user_last_name, username=user_name, email=user_email, password=user_password)
            u1.save()
            return redirect('customer_login')
    return render(request, 'customerregister.html')

def admin_login_page(request):
    if request.method == 'POST':
        user_name = request.POST['txtUsername']
        user_password = request.POST['txtPassword']
        a1 = authenticate(username=user_name, password=user_password)
        if a1 is not None:
            if a1.is_superuser:
                return redirect('admin_home')
            else:
                return render(request, 'adminlogin.html', {'Msg': 'Admin does not exist'})
        else:
            return render(request, 'adminlogin.html', {'Msg': 'Username and Password is not matching'})
    else:        
        return render(request, 'adminlogin.html')

def admin_register_page(request):
    if request.method == 'POST':
        admin_first_name = request.POST['txtFirstName']
        admin_last_name = request.POST['txtLastName']
        admin_contact = request.POST['txtAdminContact']
        admin_username = request.POST['txtAdminUsername']
        admin_email = request.POST['txtAdminEmail']
        admin_password = request.POST['txtAdminPassword']
        if User.objects.filter(username=admin_username).exists():
            return render(request, 'adminregister.html', {'Msg': 'Username is taken'})
        elif User.objects.filter(email=admin_email).exists():
            return render(request, 'adminregister.html', {'Msg': 'Email already registered'})
        else:
            a1 = User.objects.create_superuser(first_name=admin_first_name, last_name=admin_last_name, username=admin_username, email=admin_email, password=admin_password)
            a1.save()
            return redirect('admin_login')
    else:   
        return render(request, 'adminregister.html')    
    
def add_movie_page(request):
    if request.method == 'POST':
        m1 = Movie()
        m1.movie_name = request.POST['txtMovieName']
        m1.actor_name = request.POST['txtActorName']
        m1.actor_name = request.POST['txtActressName']
        m1.director_name = request.POST['txtDirectorName']
        m1.total_cost = request.POST['txtMovieCost']
        m1.save()
        return render(request, 'addmovie.html', {'Msg': 'Movie Added Successfully'})
    else:
        return render(request, 'addmovie.html')
    
def display_movie_page(request):
    movie_data = Movie.objects.all()
    return render(request, 'displaymovie.html', {'MovieData': movie_data})    

def update_movie_page(request, id):
    m1 = Movie.objects.get(id=id)
    if request.method == 'POST':
        m1 = Movie()
        m1.movie_name = request.POST['txtMovieName']
        m1.actor_name = request.POST['txtActorName']
        m1.actor_name = request.POST['txtActressName']
        m1.director_name = request.POST['txtDirectorName']
        m1.total_cost = request.POST['txtMovieCost']
        m1.save()
        return render(request, 'displaymovie.html', {'Msg': 'Movie Updated Successfully'})
    else:
        return render(request, 'addmovie.html')
    
def delete_movie_page(request, id):
    m1 = Movie.objects.get(id=id)
    m1.delete()
    return redirect('display_movie')   

def display2_movie_page(request):
    movie_data = Movie.objects.all()
    return render(request, 'customermoviedisplay.html', {'MovieData': movie_data})
    