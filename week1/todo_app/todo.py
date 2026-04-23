import json

with open('todos.json', 'r') as dosya:
    veri = json.load(dosya)

def gorev_ekle(y_baslik):  
    yeni_gorev = {'id': len(veri) + 1, 'baslik': y_baslik, 'tamamlandi': False}
    veri.append(yeni_gorev)
    with open('todos.json', 'w') as dosya:
        json.dump(veri, dosya)
    print("Görev Eklendi!")

def gorev_listele():
    print("=== GÖREV LİSTESİ ===")
    

while True:
    print("=== TODO UYGULAMASI ===")
    print("1. Görev Ekle")
    print("2. Görevleri Listele")
    print("3. Görevi Tamamla")
    print("4. Görevi Sil")
    print("5. Çıkış")
    inp = int(input("Seçiminiz: "))
        
    if inp == 1:
        y_baslik = input("Yeni eklenecek olan görev için bir başlık giriniz: ")
        gorev_ekle(y_baslik)
    if inp == 2:
