from django.http import HttpResponse
from django.shortcuts import render, redirect
from pharmasite.models import Products, Contacts


# Create your views here.


def home(request):
    return render(request, "index.html")


def products(request):
    products = Products.objects.all()
    context = {
        'products': products

    }
    return render(request, "shop.html", context)


def single_products(request):
    return render(request, "shop-single.html")


def about(request):
    return render(request, "about.html")


def contact(request):
    if request.method == "GET":
        contact = Contacts.objects.all()
        return render(request, "contact.html")
    elif request.method == "POST":
        f_name = request.POST["c_fname"]
        l_name = request.POST["c_lname"]
        email = request.POST["c_email"]
        subject = request.POST["c_subject"]
        message = request.POST["c_message"]

        Contacts.objects.create(
            fast_name=f_name,
            last_name=l_name,
            email=email,
            subject=subject,
            message=message
        )

        return redirect('/')
