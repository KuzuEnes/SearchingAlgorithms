def linear_search(arr, hedef):
    for i in range(len(arr)):
        if arr[i] == hedef:
            return i  # hedef bulunduğunda indeks döndürülür
    return -1  # hedef bulunamazsa -1 döndürülür

# Örnek kullanım
sayilar = [5, 3, 7, 1, 9, 4]
hedef = 9
sonuc = linear_search(sayilar, hedef)

if sonuc != -1:
    print(f"{hedef} dizide {sonuc}. indexte bulundu.")
else:
    print(f"{hedef} dizide bulunamadı.")

#Time Complexity: O(n)
#Space Complexity : O(1)

#Lineer arama, en temel arama algoritmasıdır. Bu algoritma, bir diziyi baştan sona tarar ve hedef öğeyi bulana kadar her öğeyi karşılaştırır. Eğer hedef öğe bulunursa, öğenin indisini döndürür.
#Lineer arama, küçük ve sıralı olmayan veri listelerinde eleman aramak için kullanılır.
