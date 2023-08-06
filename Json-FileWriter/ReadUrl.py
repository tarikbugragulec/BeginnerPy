import json
import os

def get_url():
    try:
        with open("config.json", "r") as f:
            config_data = json.load(f)
            url_value = config_data["Url"]
            return url_value
    except FileNotFoundError:
        print("config.json dosyası bulunamadı.")
    except KeyError:
        print("Url anahtarı config.json dosyasında bulunamadı.")
    except Exception as e:
        print("Bir hata oluştu:", e)
