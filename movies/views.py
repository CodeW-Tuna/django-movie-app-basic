from django.shortcuts import render
from .models import Kategoriler, Filmler


kategori_list = ["Ask","Macera","Aksiyon","Bilim Kurgu","Biografi","Romantik Komedi"]

filmler_list = [
    {   
        "id": 1,
        "film_adi":"Aykut Eniste",
        "yonetmen":"Cem Gelinoglu",
        "aciklama":"ailecek izlenebilecek komik bir film. Bence izleyin derim.",
        "resim":"aykuteniste.jpg",
        "anasayfa": True
    },
    {
        "id": 2,
        "film_adi":"Fury",
        "yonetmen":"Brad Pit",
        "aciklama":"ailecek izlenebilecek bir savas dizisi film",
        "resim":"fury.jpg",
        "anasayfa": False
    },
    {
        "id": 3,
        "film_adi":"Titanic",
        "yonetmen":"James Cameron",
        "aciklama":"efsane bir ask film sonunda adam oluyo",
        "resim":"titanic.jpg",
        "anasayfa": True
    },
    {
        "id": 4,
        "film_adi":"Er Ryan'i Kurtarmak",
        "yonetmen":"John Elfrad",
        "aciklama":"Efsanelesmis bir savas ve aksiyon bas yapidir.",
        "resim":"erryan.jpg",
        "anasayfa": True
    },
    {
        "id": 5,
        "film_adi":"Bati Cephesinde Her Sey Yolunda",
        "yonetmen":"Adam Clared",
        "aciklama":"Almanya Hitler zamaninda bati Fransanin isgalini anlatan bir asker gozunden film",
        "resim":"sikintiyok.jpg",
        "anasayfa": False
    },
    {
        "id": 6,
        "film_adi":"Konus Benimle",
        "yonetmen":"Horland Cref",
        "aciklama":"Konusmanin onemini anlatan bir drama filmi",
        "resim":"konusbenimle.jpg",
        "anasayfa": False

    },
    {
        "id": 7,
        "film_adi":"Tron",
        "yonetmen":"Sahan Gokbakar",
        "aciklama":"halktan birini yine halkin icinden gelip bizleri hem guldurup hem de aglatmasi",
        "resim":"tron.jpg",
        "anasayfa": False
    },
    {
        "id": 8,
        "film_adi":"Snowden",
        "yonetmen":"Sahan Gokbakar",
        "aciklama":"halktan birini yine halkin icinden gelip bizleri hem guldurup hem de aglatmasi",
        "resim":"snowden.jpg",
        "anasayfa": True

    }
]



# Create your views here.
def anasayfa(request):
    data = {
        "kategoriler":Kategoriler.objects.all(),
        "filmler":Filmler.objects.all()
    }
    return render(request, "index.html", data)

def movies(request):
    data = {
        "kategoriler":Kategoriler.objects.all(),
        "filmler":Filmler.objects.all()
    }
    return render(request, "movies.html",data)

def categories(request):
    data = {
        "kategoriler":Kategoriler.objects.all(),
        "filmler":Filmler.objects.all()
    }
    return render(request, "categories.html",data)


def watch(request, id):
    data = {
        "id":Filmler.objects.get(id=id), # {"id":3} id.id - "id"
        "filmler":Filmler.objects.all(),
    }
    return render(request, "watchnow.html", data)