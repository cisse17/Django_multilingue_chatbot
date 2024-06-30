from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.views.generic import DetailView
from .forms import BlogUserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.contrib import messages
from .models import BlogPost

# Create your views here.


def index(request):
    posts = BlogPost.objects.all()

    return render(request, 'main/index.html', {'posts': posts})


class DetailBlog(DetailView):
    model = BlogPost
    template_name = 'main/detail.html'
    context_object_name = 'articles'    # 'object' disponible par défaut


# Create your views here.
def inscription(request):
    if request.method == 'POST':
        form = BlogUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('connexion')
    else:
        form = BlogUserCreationForm()
    return render(request, 'main/inscription.html', {'form': form})

def connexion(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None :
            login(request, user)
            return redirect('chatbot')
        else:
            messages.error(request, 'Nom d\'utilisateur ou mot de passe incorrect.')
    return render(request, 'main/connexion.html')


def deconnexion(request):
    logout(request)
    return redirect('connexion')



# mdp Technicaltest2024 username = DiotSiaci 
# someone who want to test the login form you can use this informations for loging to chat with IA chat


