from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# ----------------------
# Home view
# ----------------------
def home(request):
    return render(request, 'home.html')

# ----------------------
# Cities view (login required)
# ----------------------
@login_required(login_url='/login/')
def cities(request):
    cities_list = [
        {
            "name": "Barisal",
            "url_name": "barisal",
            "image_url": "images/barisal.jpg",
            "description": "Known as the 'Venice of the East', Barisal has rivers, floating markets, and Kuakata Beach."
        },
        {
            "name": "Cox's Bazar",
            "url_name": "coxsbazar",
            "image_url": "images/coxsbazar.jpg",
            "description": "Home to the world's longest unbroken sandy beach and vibrant island attractions."
        },
        {
            "name": "Khulna",
            "url_name": "khulna",
            "image_url": "images/khulna.jpg",
            "description": "Gateway to the Sundarbans, rich in biodiversity and history."
        },
        {
            "name": "Rajshahi",
            "url_name": "rajshahi",
            "image_url": "images/rajshahi.jpg",
            "description": "Known for silk, mangoes, and historical sites like Puthia Temple."
        },
        {
            "name": "Chittagong",
            "url_name": "chittagong",
            "image_url": "images/chittagong.jpg",
            "description": "A bustling port city with beaches, lakes, and cultural landmarks."
        },
        {
            "name": "Tangail",
            "url_name": "tangail",
            "image_url": "images/tangail.jpg",
            "description": "Famous for the 201 Dome Mosque and rich cultural heritage."
        },
        {
            "name": "Sylhet",
            "url_name": "sylhet",
            "image_url": "images/sylhet.jpg",
            "description": "Hilly region with tea gardens, waterfalls, and natural beauty."
        },
    ]
    return render(request, 'cities.html', {"cities": cities_list})
# Login view
# ----------------------
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()
        user = authenticate(request, username=username, password=password)
        if user:
            auth_login(request, user)
            messages.success(request, f'Welcome back, {user.username}!')
            return redirect('cities')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')

# ----------------------
# Signup view
# ----------------------
def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '').strip()
        confirm_password = request.POST.get('confirm_password', '').strip()

        # Validations
        if password != confirm_password:
            messages.error(request, 'Passwords do not match.')
        elif User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'Email is already registered.')
        else:
            # Create user and hash password automatically
            user = User.objects.create_user(username=username, email=email, password=password)
            auth_login(request, user)  # Auto-login after signup
            messages.success(request, f'Account created successfully. Welcome, {user.username}!')
            return redirect('cities')

    return render(request, 'signup.html')

# ----------------------
# Logout view
# ----------------------
def logout_view(request):
    logout(request)
    messages.success(request, 'You have successfully logged out.')
    return redirect('home')
