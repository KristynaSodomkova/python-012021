from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='katalog'),
    path('seznam/', views.SeznamAutView.as_view(), name='auta'),
    path('vypujcky/', views.PrehledVypujcekView.as_view(), name='vypujcky'),
    path('zakaznici/', views.PrehledZakaznikuView.as_view(), name='zakaznici')
]
