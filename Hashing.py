def linear_search(arr, hedef):
    for i in range(len(arr)):
        if arr[i] == hedef:
            return i
    return -1

def binary_search(arr, hedef):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == hedef:
            return mid
        elif arr[mid] < hedef:
            low = mid + 1
        else:
            high = mid - 1

    return -1

def hashing_search(veri, anahtar):
    return veri.get(anahtar, "Bulunamadı")

# Örnek kullanım
sayilar = [1, 3, 4, 5, 7, 9]
hedef = 7
sonuc = binary_search(sayilar, hedef)
if sonuc != -1:
    print(f"{hedef} dizide {sonuc}. indexte bulundu (Binary Search).")
else:
    print(f"{hedef} dizide bulunamadı (Binary Search).")

veritabani = {"Ali": 1234, "Ayşe": 5678, "Mehmet": 9101}
kisi = "Ayşe"
print(f"{kisi} için numara: {hashing_search(veritabani, kisi)}")

#Time Complexity : O(n)
#Space Complexity: O(1)

#Hashing, bir anahtar-değer eşleme yapısıdır ve hızlı arama sağlar. Ancak, bu yöntem uygun bir hash fonksiyonunun seçilmesini ve çakışmaların ele alınmasını gerektirir.
#Hash tablosu, hızlı arama ve eşleşme sağladığı için büyük veri kümeleri üzerinde performansı artırmak ve anahtar-değer çiftlerini yönetmek için tercih edilir.