from django.shortcuts import render,get_object_or_404
from django.views.generic import CreateView, UpdateView, DeleteView

from blog.forms import ContactForm
from blog.models import Home, Home1, Home2, Home3, Home4, Home5, Home6, Contact
from django.views.generic.edit import CreateView, UpdateView, DeleteView


# Create your views here.
def index(request):
    form = ContactForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
    home = Home.objects.filter(nomi="FC MOBILE")
    home1 = Home1.objects.all()
    home2 = Home2.objects.all()
    home3 = Home3.objects.all()
    home4 = Home4.objects.all()
    home5 = Home5.objects.all()
    home6 = Home6.objects.all()
    contact = Contact.objects.all()
    context = {
        'home': home,
        'home1': home1,
        'home2': home2,
        'home3': home3,
        'home4': home4,
        'home5': home5,
        'home6': home6,
        'contact': contact,
    }

    return render(request,"index.html", context=context)



def about(request):
    home1 = Home1.objects.all()
    context = {
        'home1': home1,
    }
    return render(request,"about.html", context=context)



def contact(request):
    contact = Contact.objects.all()
    context = {
        "contact": contact,

    }
    return render(request,"contact.html", context=context)


def menu(request):
    home2 = Home2.objects.all()
    home5 = Home5.objects.all()
    context = {
        'home2': home2,
        'home5': home5,
    }
    return render(request,"menu.html", context=context)



def service(request):
    home3 = Home3.objects.all()
    context = {
        'home3': home3,

    }
    return render(request,"service.html", context=context)

def team(request):
    home4 = Home4.objects.all()
    context = {
        'home4': home4,

    }
    return render(request,"team.html", context=context)


def testimonial(request):
    home6 = Home6.objects.all()
    context = {
        'home6': home6,

    }

    return render(request,"testimonial.html", context=context)


def index_detel(request,slug):
    text = get_object_or_404(Home5,slug=slug)
    context = {
        'detel': text,
    }


    return render(request,"detel.html",context = context)


class Home5CreateView(CreateView):
    model = Home5
    template_name = 'home_create.html'
    fields = '__all__'
    success_url = "/"

class Home5UpdateView(UpdateView):
    model = Home5
    template_name = 'home_update.html'
    fields = '__all__'
    success_url = "/"

class Home5DeleteView(DeleteView):
    model = Home5
    template_name = 'home_delete.html'
    success_url = "/"

