import json

with open('todos.json', 'r') as dosya:
    veri = json.load(dosya)

def gorev_ekle(y_baslik):  
    idler = [gorev['id'] for gorev in veri]
    yeni_gorev = {'id': max(idler, default=0) + 1, 'baslik': y_baslik, 'tamamlandi': False}
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
    
def gorev_tamamla(g_id):
    for gorev in veri:
        if g_id == gorev['id']:
            gorev['tamamlandi'] = True
            with open('todos.json', 'w') as dosya:
                json.dump(veri, dosya, ensure_ascii=False, indent=2) 
            print(f"\n✓ '{gorev['baslik']}' tamamlandı!")
            return
    print("Girilen id bulunamadı!")
        
def gorev_sil(g_id):
    for gorev in veri:
        if g_id == gorev['id']:
            baslik = gorev['baslik']
            veri.remove(gorev)
            with open('todos.json', 'w') as dosya:
                json.dump(veri, dosya, ensure_ascii=False, indent=2)
            print(f"\n'{baslik}' silindi!")
            return
    print("Girilen id'ye sahip görev bulunamadı!")
        
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
    elif inp == 3:
        g_id = int(input("Tamamlamak istediğiniz görevin idsini giriniz: "))
        gorev_tamamla(g_id)
    elif inp == 4:
        g_id = int(input("Silmek istediğiniz görevin idsini giriniz: "))
        gorev_sil(g_id)
    elif inp == 5:
        print("\nGörüşürüz!")
        break
        