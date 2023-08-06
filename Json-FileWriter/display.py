import matplotlib.pyplot as plt
import numpy as np
import FetchData

def metod1():
    a = FetchData.verileri_al()
    yaslar = [kisi["yas"] for kisi in a]
    isimler = [kisi["ad"] for kisi in a]
    xpoints = np.array(yaslar)
    ypoints = np.array(isimler)

    plt.xlabel("Yaş")
    plt.xlabel("İsim")
    plt.plot(xpoints, ypoints, 'o')
    plt.show()
    