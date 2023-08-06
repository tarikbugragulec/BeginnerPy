import matplotlib.pyplot as plt
import FetchData
import CityPeopleNumber

def metod():
    a = FetchData.verileri_al()

    ulkeler = {}
    for kisi in a:
        ulke = kisi["ulke"]
        if ulke in ulkeler:
            ulkeler[ulke] += 1
        else:
            ulkeler[ulke] = 1

    ulke_adlari = list(ulkeler.keys())
    kişi_sayilari = list(ulkeler.values())
    plt.pie(kişi_sayilari, labels=ulke_adlari, autopct='%1.1f%%')
    plt.title("Ülkelerde yaşayanların oranı")
    plt.show()
