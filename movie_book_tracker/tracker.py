import tkinter as tk  # Pencere oluşturma araçlarını ekler.

window = tk.Tk()  # Ana pencereyi açar.
window.title("Movie and Book Tracker")  # Pencerenin başlığını yazar.
window.geometry("380x500")  # Pencerenin boyutunu ayarlar.

tk.Label(window, text="Ad (ör. Stranger Things - Dizi):").pack()  # Ad kutusunun açıklamasını gösterir.
name_entry = tk.Entry(window)  # Kitap veya dizi adını yazacağın kutuyu oluşturur.
name_entry.pack()  # Ad kutusunu pencereye yerleştirir.

tk.Label(window, text="Kaldığın yer (ör. Bölüm 3 / Sayfa 40):").pack()  # İlerleme kutusunu açıklar.
progress_entry = tk.Entry(window)  # Bölüm veya sayfa bilgisini yazacağın kutuyu oluşturur.
progress_entry.pack()  # İlerleme kutusunu pencereye yerleştirir.

list_box = tk.Listbox(window)  # Kayıtların görüneceği listeyi oluşturur.
list_box.pack(fill="both", expand=True, padx=10, pady=10)  # Listeyi pencereye yerleştirir.

def save_list():  # Listedeki kayıtları dosyaya kaydeder.
    with open("tracker_data.txt", "w", encoding="utf-8") as file:  # Dosyayı yazmak için açar ve işi bitince kapatır.
        for number in range(list_box.size()):  # Listedeki kayıtları sırayla gezer.
            file.write(list_box.get(number) + "\n")  # Her kaydı dosyaya yazar.

def add_item():  # Yeni kitap veya dizi ekler.
    name = name_entry.get().strip()  # Ad kutusundaki yazıyı alır.
    progress = progress_entry.get().strip()  # İlerleme kutusundaki yazıyı alır.
    if name and progress:  # İki kutu da doluysa devam eder.
        list_box.insert(tk.END, name + " | " + progress)  # Adı ve ilerlemeyi listeye ekler.
        save_list()  # Güncel listeyi dosyaya kaydeder.
        name_entry.delete(0, tk.END)  # Ad kutusunu temizler.
        progress_entry.delete(0, tk.END)  # İlerleme kutusunu temizler.

def update_progress():  # Seçtiğin kaydın bölüm veya sayfa bilgisini değiştirir.
    selected = list_box.curselection()  # Seçili satırın numarasını alır.
    progress = progress_entry.get().strip()  # Yeni ilerleme bilgisini alır.
    if selected and progress:  # Bir kayıt seçilmiş ve yeni bilgi yazılmışsa devam eder.
        number = selected[0]  # Seçili kaydın sıra numarasını alır.
        old_item = list_box.get(number)  # Seçili kaydın mevcut yazısını alır.
        name = old_item.split(" | ", 1)[0]  # Kaydın adını mevcut yazıdan ayırır.
        list_box.delete(number)  # Eski kaydı listeden kaldırır.
        list_box.insert(number, name + " | " + progress)  # Yeni ilerlemeyle aynı yere ekler.
        save_list()  # Güncel listeyi dosyaya kaydeder.
        progress_entry.delete(0, tk.END)  # İlerleme kutusunu temizler.

def delete_item():  # Seçtiğin kaydı siler.
    selected = list_box.curselection()  # Seçili satırın numarasını alır.
    if selected:  # Bir kayıt seçilmişse devam eder.
        list_box.delete(selected[0])  # Seçili kaydı listeden siler.
        save_list()  # Silinmiş listeyi dosyaya kaydeder.

open("tracker_data.txt", "a", encoding="utf-8").close()  # Dosya yoksa oluşturur.
with open("tracker_data.txt", "r", encoding="utf-8") as file:  # Kayıt dosyasını okumak için açar.
    for line in file:  # Dosyadaki kayıtları sırayla gezer.
        list_box.insert(tk.END, line.strip())  # Her kaydı pencerenin listesine ekler.

tk.Button(window, text="Ekle", command=add_item).pack()  # Yeni kayıt ekleme düğmesini oluşturur.
tk.Button(window, text="İlerlemeyi güncelle", command=update_progress).pack()  # Seçili kaydın ilerlemesini değiştirir.
tk.Button(window, text="Seçileni sil", command=delete_item).pack()  # Seçili kaydı silme düğmesini oluşturur.

window.mainloop()  # Pencereyi açık tutar.
