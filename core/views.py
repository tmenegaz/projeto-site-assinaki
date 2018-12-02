from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'title': 'assinaki',
        'pagina_1': 'A empresa',
        'pagina_2': 'Produtos',
        'pagina_3': 'Cadastre-se',
        'pagina_4': 'Login',
    }
    return render(request, "index.html", context)

def index_light(request):
    return render(request, "index-light.html")

def about(request):
    return render(request, "about.html")

def services(request):
    return render(request, "services.html")

def clients(request):
    return render(request, "clients.html")

def contact(request):
    return render(request, "contact.html")

def login(request):
    return render(request, "login.html")

def cadastro(request):
    return render(request, "cadastro.html")

