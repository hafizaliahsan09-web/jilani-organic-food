from django.shortcuts import render

from django.http import HttpResponse

from django.shortcuts import render

from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import BuyerForm


def home(request):
    return render(request, "myapp/home.html")

def new_page(request):
    return render(request, "myapp/newpage.html")

def orders(request):
    return render(request, 'orders.html') 


def buy_now(request):
    if request.method == "POST":
        name = request.POST.get('name')
        # father name = request.POST.get('father name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        address = request.POST.get('address')
        # quantity = request.POST.get('quantity')
        item = request.POST.get('item')
        # You can save this data to database here or print for now
        print(name, phone, email, address, item)
        return render(request, 'thankyou.html')  # After submission
        return render(request, 'buy_now.html')  # Form page

def order_form(request):
    if request.method == 'POST':
        form = BuyerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thankyou')  # redirect to a thank-you page
    else:
        form = BuyerForm()
    return render(request, 'order_form.html', {'form': form})


def thankyou(request):
    return render(request, 'thankyou.html')




