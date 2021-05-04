from django.urls import path
from . import views

urlpatterns = [
    path("", views.MujPrvniPohled.as_view(), name="index"),
    path('kontakty/', views.KontaktyView.as_view(), name='kontakty'),
    path('organizace/', views.OrganizaceView.as_view(), name='organizace'),
    path("<int:pk>", views.DetailOrganizaceView.as_view(), name="detail_organizace"),
]