import json

with open('todos.json', 'r') as dosya:
    veri = json.load(dosya)

def gorev_ekle(y_baslik):  
    yeni_gorev = {'id': len(veri) + 1, 'baslik': y_baslik, 'tamamlandi': False}
    veri.append(yeni_gorev)
    with open('todos.json', 'w') as dosya:
        json.dump(veri, dosya, ensure_ascii=False, indent=2)
    print("\nGörev Eklendi!")

def gorev_listele():
    print("\n=== GÖREV LİSTESİ ===")
    if not veri:
        print("Henüz görev yok...")
        return

    for gorev in veri:
        durum = "[✓]" if gorev['tamamlandi'] else "[ ]"
        print(f"{gorev['id']}. {durum} {gorev['baslik']}")
        
while True:
    print("\n=== TODO UYGULAMASI ===")
    print("1. Görev Ekle")
    print("2. Görevleri Listele")
    print("3. Görevi Tamamla")
    print("4. Görevi Sil")
    print("5. Çıkış")
    inp = int(input("Seçiminiz: "))
    
    if inp == 1:
        y_baslik = input("Yeni eklenecek olan görev için bir başlık giriniz: ")
        gorev_ekle(y_baslik)
    elif inp == 2:
        gorev_listele()
    elif inp == 5:
        print("\nGörüşürüz!")
        break
        