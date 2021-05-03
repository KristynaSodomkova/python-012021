from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView
from . import models

# Create your views here.
class IndexView(View):
    def get(self, request):
        return HttpResponse("<h1>Vítejte v autopůjčovně U Starýho Bouráka!</h1>"
                            "<p>Tady Vám řekneme, proč si půjčit auto zrovna u nás</p>"
                            "<h2>Užitečné odkazy:</h2>"
                            "<a href='http://localhost:8000/katalog/seznam/'>Náš katalog</a>"
                            "<br>"
                            "<a href='http://localhost:8000/katalog/vypujcky/'>Přehled výpůjček</a>"
                            "<br>"
                            "<a href='http://localhost:8000/katalog/zakaznici/'>Naši spokojení zákazníci</a>"
                            "<p>Těšíme se na Vaši návštěvu!</p>"
                            "<p>Kontakty:</p>"
                            "<ul>"
                                "<li>E-mail: ustaryhobouraka@seznam.cz</li>"
                                "<li>Tel: 000 000 000</li>"
                                "<li>Adresa: Za zatáčkou 123, Nikdynestůj</li>"
                            "</ul>"
                            )

class SeznamAutView(ListView):
    model = models.Auto
    template_name = "katalog/seznam_aut.html"

class PrehledVypujcekView(ListView):
    model = models.Vypujcka
    template_name = "katalog/prehled_vypujcek.html"

class PrehledZakaznikuView(ListView):
    model = models.Zakaznik
    template_name = "katalog/prehled_zakazniku.html"