from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.
class IndexView(View):
    def get(self, request):
        return HttpResponse("Zde bude titulní stránka. Náš katalog najdete zde: "
                            "<a href='http://localhost:8000/katalog/seznam/'>Katalog</a>"
                            )

class SeznamView(View):
    def get(self, request):
        return HttpResponse("Zde bude seznam aut.")