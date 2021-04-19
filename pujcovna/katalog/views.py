from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.
class IndexView(View):
    def get(self, request):
        return HttpResponse("<h1>Vítejte v autopůjčovně U Starýho Bouráka!</h1>"
                            "<p>Tady Vám řekneme, proč si půjčit auto zrovna u nás</p>"
                            "<h2>Užitečné odkazy:</h2>"
                            "<a href='http://localhost:8000/katalog/seznam/'>Náš katalog</a>"
                            "<p>Těšíme se na Vaši návštěvu!</p>"
                            "<p>Kontakty:</p>"
                            "<ul>"
                                "<li>E-mail: ustaryhobouraka@seznam.cz</li>"
                                "<li>Tel: 000 000 000</li>"
                                "<li>Adresa: Za zatáčkou 123, Nikdynestůj</li>"
                            "</ul>"
                            )

class SeznamView(View):
    def get(self, request):
        return HttpResponse("Zde bude seznam aut.")