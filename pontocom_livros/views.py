from django.shortcuts import render


def home_page(request):
    return render(request, "pontocom_livros/templates/ecomerce/pages/home.html")
