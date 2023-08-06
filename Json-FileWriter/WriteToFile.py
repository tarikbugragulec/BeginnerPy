import os
import json
import FetchData
veriler = FetchData.verileri_al()

def ToFile(veri):
    kod= veri + ".txt"
    try:
        with open(kod, "w") as f:
            for x in veriler:
                json_str = json.dumps(x) + "\n"
                f.write(json_str)
    except Exception as e:
        print("Hata:", e)
    pass

