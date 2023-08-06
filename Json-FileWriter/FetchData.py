import requests
import ReadUrl

def verileri_al():
    try:
        url=ReadUrl.get_url()
        istek = requests.get(url)
        if istek.status_code == 200:
            veri = istek.json()
            kisiler = veri["kisiler"]
            liste_veriler = []
            for kisi in kisiler:
                dict_kisi = {
                    "ad": kisi["ad"],
                    "soyad": kisi["soyad"],
                    "ulke": kisi["ulke"],
                    "sehir": kisi["sehir"],
                    "yas": kisi["yas"]
                }
                liste_veriler.append(dict_kisi)

            return liste_veriler
        else:
            print("Hata: İstek başarısız oldu.")
    except Exception :
        print("Hata:", Exception)
        return []
