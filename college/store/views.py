from django.shortcuts import render, redirect
from .forms import OrderForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.

def home(request):
    return render(request, 'home.html')


def department(request, depart):
    departments = {
        'computer_science': 'https://en.wikipedia.org/wiki/Computer_science',
        'commerce': 'https://en.wikipedia.org/wiki/Commerce',
        'physics': 'https://en.wikipedia.org/wiki/Physics',
        'mathematics': 'https://en.wikipedia.org/wiki/Mathematics',
        'english': 'https://en.wikipedia.org/wiki/English',
    }
    url = departments[depart]
    return redirect(url)


@login_required(login_url='/auth/login')
def detail(request):
    return render(request, 'detail.html')


@login_required(login_url='/auth/login')
def details(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            print("Successful form submitted")
            messages.success(request, "You registered Successfully.")
            return redirect("store:details")
        else:
            context = {
                'form': form
            }
            messages.info(request, "Your form has some error.")
            print(form.errors)
            return render(request, 'orderform.html', context)
    else:
        form = OrderForm()
        return render(request, 'orderform.html', {'form': form})
