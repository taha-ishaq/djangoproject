from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CatPostForm
from .models import CatPost
from django.contrib.auth import logout

# Register View
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully!')
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

# Login View
def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'You are logged in!')
                return redirect('home')  # Redirect to home or dashboard
            else:
                messages.error(request, 'Invalid username or password')
        else:
            messages.error(request, 'Invalid form submission')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'login.html', {'form': form})

def home(request):
    # Fetch all cat posts from the database
    cat_posts = CatPost.objects.all().order_by('-created_at')  # Order by creation date (most recent first)
    
    # Render the home template with the cat posts
    return render(request, 'home.html', {'cat_posts': cat_posts})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')


@login_required
def post_cat(request):
    if request.method == 'POST':
        form = CatPostForm(request.POST, request.FILES)
        if form.is_valid():
            cat_post = form.save(commit=False)
            cat_post.user = request.user  # Assign the logged-in user
            cat_post.save()
            return redirect('home')  # Redirect to the home page after successful post
    else:
        form = CatPostForm()

    return render(request, 'post_cat.html', {'form': form})
def logout_view(request):
    logout(request)
    return redirect('home') 