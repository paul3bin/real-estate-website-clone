from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

from contacts.models import Contact


def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username=username, password=password)

        if user:
            auth.login(request, user)
            messages.success(request, "You are now logged in!")
            return redirect("dashboard")

        messages.error(request, "Invalid credentials")
        return redirect("login")

    return render(request, "accounts/login.html")


def logout(request):
    if request.method == "POST":
        auth.logout(request)
        messages.success(request, "You are now logged out!")
        return redirect("index")


def register(request):
    if request.method == "POST":

        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        password2 = request.POST["password2"]

        # check if passwords match
        if password == password2:

            # check for duplicate username
            if User.objects.filter(username=username).exists():
                messages.error(request, "Passwords do not match")
                return redirect("register")

            else:
                # check for duplicate email
                if User.objects.filter(email=email).exists():
                    messages.error(request, "Email already exists!")
                    return redirect("register")

                user = User.objects.create_user(
                    username=username,
                    password=password,
                    email=email,
                    first_name=first_name,
                    last_name=last_name,
                )
                user.save()
                messages.success(
                    request, "User registered successfully! You can now login!"
                )
                return redirect("login")

        messages.error(request, "Passwords do not match")
        return redirect("register")

        return redirect("register")

    return render(request, "accounts/register.html")


def dashboard(request):
    user_contacts = Contact.objects.order_by("-contact_date").filter(
        user_id=request.user.id
    )

    return render(
        request, "accounts/dashboard.html", context={"contacts": user_contacts}
    )
