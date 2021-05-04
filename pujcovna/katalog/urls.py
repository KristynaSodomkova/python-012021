from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='katalog'),
    path('seznam/', views.SeznamAutView.as_view(), name='auta'),
    path('vypujcky/', views.PrehledVypujcekView.as_view(), name='vypujcky'),
    path('zakaznici/', views.PrehledZakaznikuView.as_view(), name='zakaznici'),
    path("vypujcky/<int:pk>", views.DetailVypujckyView.as_view(), name='auto'),
    path("zakaznici/<int:pk>", views.DetailZakaznikaView.as_view(), name='zakaznik'),
    path("<int:pk>", views.DetailAutaView.as_view(), name='auto'),
    path("nove_auto/", views.NoveAutoView.as_view(), name='pridej_auto'),
    path("nove_auto/", views.PotvrdNoveAutoView.as_view(), name='potvrd_auto'),
    path("novy_zakaznik", views.NovyZakaznikView.as_view(), name='pridej_zakaznika'),
    path("novy_zakaznik/", views.PotvrdNovyZakaznikView.as_view(), name='potvrd_zakaznika'),
]
