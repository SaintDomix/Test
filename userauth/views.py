from django.shortcuts import render, redirect
from userauth.forms import UserRegisterForm
from django.contrib.auth import login, authenticate, get_user_model
from django.contrib import messages
from .forms import EmailForm
from .forms import ProfileForm

def register_view(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save()

            # Authenticate the user only if registration is successful
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password1")
            User = get_user_model()
            new_user = authenticate(request, username=email, password=password)

            if new_user is not None:
                login(request, new_user)
                messages.success(request, f"Hey {email}, Your account was created successfully")
                return redirect("app:home")
            else:
                messages.error(request, "Failed to authenticate user.")
    else:
        form = UserRegisterForm()

    context = {
        'form': form
    }

    # Clear messages after they have been displayed
    storage = messages.get_messages(request)
    storage.used = True

    return render(request, "userauth/sign-up.html", context)


def subscribe(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to the home page
            return redirect('app:home')
    else:
        form = EmailForm()

    return render(request, 'app/home.html', {'form': form})



def login_view(request):
    if request.method == "POST":
        email = request.POST.get('email')

        # Perform any necessary checks, e.g., check if the email exists in the database
        # Replace the following check with your actual logic
        if email == "user@example.com":
            # Assuming 'app:home' is the correct URL pattern name for your home page
            return redirect('app:home')
        else:
            messages.error(request, "Invalid email. Please register.")
            return redirect('app:login')

    return render(request, 'app/profile.html')
