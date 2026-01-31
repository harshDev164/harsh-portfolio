from django.shortcuts import render, redirect
from .mongodb import get_db


def home(request):
    if request.method == "POST":
        db = get_db()

        db.messages.insert_one({
            "full_name": request.POST.get("first_name"),
            "email": request.POST.get("email"),
            "company_name": request.POST.get("company_name"),
            "designation": request.POST.get("designation"),
            "message": request.POST.get("message"),
        })

        return redirect("/#contact")

    return render(request, "index.html")


def blog_detail(request):
    return render(request, "blog-details.html")


def project_detail(request):
    return render(request, "project-details.html")
