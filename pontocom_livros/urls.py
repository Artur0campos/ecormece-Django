from django.urls import path

from pontocom_livros.views import home_page

urlpatterns = [
    path('home/', home_page),
    path('', home_page)
]
