from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='katalog'),
    path('seznam/', views.SeznamAutView.as_view(), name='auta'),
    path('vypujcky/', views.PrehledVypujcekView.as_view(), name='vypujcky'),
    path('zakaznici/', views.PrehledZakaznikuView.as_view(), name='zakaznici'),
    path("vypujcky/<int:pk>", views.DetailVypujckyView.as_view(), name='vypujcka'),
    path("zakaznici/<int:pk>", views.DetailZakaznikaView.as_view(), name='zakaznik'),
    path("<int:pk>/", views.DetailAutaView.as_view(), name='auto'),
    path("auto/nove_auto/", views.NoveAutoView.as_view(), name='pridej_auto'),
    path("auto/potvrd_auto/", views.PotvrdNoveAutoView.as_view(), name='potvrd_auto'),
    path("zakaznik/novy_zakaznik/", views.NovyZakaznikView.as_view(), name='pridej_zakaznika'),
    path("zakaznik/potvrd_zakaznika/", views.PotvrdNovyZakaznikView.as_view(), name='potvrd_zakaznika'),
]
