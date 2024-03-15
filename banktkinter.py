import sqlite3
import random
import tkinter as tk
from tkinter import messagebox


class BankaGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Banka Yönetim Sistemi")
        self.master.geometry("600x400")

        self.banka = Banka()

        self.label = tk.Label(master, text="Hoş Geldiniz!", font=("Helvetica", 20), bg="blue", fg="white")
        self.label.pack(pady=10)

        self.button1 = tk.Button(master, text="Hesap Oluştur", command=self.hesap_olusturma_popup, font=("Helvetica", 14))
        self.button1.pack(pady=5)

        self.button2 = tk.Button(master, text="Tüm Hesaplar", command=self.tum_hesaplar, font=("Helvetica", 14))
        self.button2.pack(pady=5)

        self.button3 = tk.Button(master, text="Tüm Müşteriler", command=self.tum_musteriler, font=("Helvetica", 14))
        self.button3.pack(pady=5)

        self.button4 = tk.Button(master, text="Para Yatırma", command=self.para_yatirma_popup, font=("Helvetica", 14))
        self.button4.pack(pady=5)

        self.button5 = tk.Button(master, text="Para Çekme", command=self.para_cekme_popup, font=("Helvetica", 14))
        self.button5.pack(pady=5)

        self.button6 = tk.Button(master, text="Hesap Silme", command=self.hesap_silme_popup, font=("Helvetica", 14))
        self.button6.pack(pady=5)

        self.button7 = tk.Button(master, text="Hesap Aktif Etme", command=self.hesap_aktif_etme_popup, font=("Helvetica", 14))
        self.button7.pack(pady=5)

        self.button8 = tk.Button(master, text="Bakiye Sorgulama", command=self.bakiye_sorgulama_popup, font=("Helvetica", 14))
        self.button8.pack(pady=5)

    def hesap_olusturma_popup(self):
        popup = tk.Toplevel()
        popup.title("Hesap Oluşturma")
        popup.geometry("400x300")
        label = tk.Label(popup, text="Hesap Oluşturma Ekranı", font=("Helvetica", 16))
        label.pack(pady=10)

        self.ad_label = tk.Label(popup, text="Ad:", font=("Helvetica", 14))
        self.ad_label.pack()
        self.ad_entry = tk.Entry(popup, font=("Helvetica", 14))
        self.ad_entry.pack()

        self.soyad_label = tk.Label(popup, text="Soyad:", font=("Helvetica", 14))
        self.soyad_label.pack()
        self.soyad_entry = tk.Entry(popup, font=("Helvetica", 14))
        self.soyad_entry.pack()

        self.button = tk.Button(popup, text="Hesap Oluştur", command=self.hesap_olusturma, font=("Helvetica", 14))
        self.button.pack(pady=20)

    def hesap_olusturma(self):
        ad = self.ad_entry.get()
        soyad = self.soyad_entry.get()
        musteri = Musteri(ad, soyad)
        hesap = self.banka.hesap_olusturmak(musteri)
        messagebox.showinfo("Başarılı", f"Hesap oluşturuldu. Müşteri Numarası: {musteri.musteri_numarası}, "
                                         f"Hesap Numarası: {hesap.hesap_numarasi}")

    def tum_hesaplar(self):
        popup = tk.Toplevel()
        popup.title("Tüm Hesaplar")
        popup.geometry("600x400")
        self.banka.tum_hesaplar(popup)

    def tum_musteriler(self):
        popup = tk.Toplevel()
        popup.title("Tüm Müşteriler")
        popup.geometry("600x400")
        self.banka.tum_musteriler(popup)

    def para_yatirma_popup(self):
        popup = tk.Toplevel()
        popup.title("Para Yatırma")
        popup.geometry("400x200")
        label = tk.Label(popup, text="Para Yatırma Ekranı", font=("Helvetica", 16))
        label.pack(pady=10)

        self.hesap_label = tk.Label(popup, text="Hesap Numarası:", font=("Helvetica", 14))
        self.hesap_label.pack()
        self.hesap_entry = tk.Entry(popup, font=("Helvetica", 14))
        self.hesap_entry.pack()

        self.miktar_label = tk.Label(popup, text="Yatırılacak Miktar:", font=("Helvetica", 14))
        self.miktar_label.pack()
        self.miktar_entry = tk.Entry(popup, font=("Helvetica", 14))
        self.miktar_entry.pack()

        self.button = tk.Button(popup, text="Para Yatır", command=self.para_yatirma, font=("Helvetica", 14))
        self.button.pack(pady=20)

    def para_yatirma(self):
        hesap_numarasi = self.hesap_entry.get()
        miktar = float(self.miktar_entry.get())
        hesap = self.banka.hesap_numarasi_kontrolu(hesap_numarasi)
        if hesap:
            hesap.para_yatirmak(miktar)

    def para_cekme_popup(self):
        popup = tk.Toplevel()
        popup.title("Para Çekme")
        popup.geometry("400x200")
        label = tk.Label(popup, text="Para Çekme Ekranı", font=("Helvetica", 16))
        label.pack(pady=10)

        self.hesap_label = tk.Label(popup, text="Hesap Numarası:", font=("Helvetica", 14))
        self.hesap_label.pack()
        self.hesap_entry = tk.Entry(popup, font=("Helvetica", 14))
        self.hesap_entry.pack()

        self.miktar_label = tk.Label(popup, text="Çekilecek Miktar:", font=("Helvetica", 14))
        self.miktar_label.pack()
        self.miktar_entry = tk.Entry(popup, font=("Helvetica", 14))
        self.miktar_entry.pack()

        self.button = tk.Button(popup, text="Para Çek", command=self.para_cekme, font=("Helvetica", 14))
        self.button.pack(pady=20)

    def para_cekme(self):
        hesap_numarasi = self.hesap_entry.get()
        miktar = float(self.miktar_entry.get())
        hesap = self.banka.hesap_numarasi_kontrolu(hesap_numarasi)
        if hesap:
            hesap.para_cekmek(miktar)

    def hesap_silme_popup(self):
        popup = tk.Toplevel()
        popup.title("Hesap Silme")
        popup.geometry("400x150")
        label = tk.Label(popup, text="Hesap Silme Ekranı", font=("Helvetica", 16))
        label.pack(pady=10)

        self.hesap_label = tk.Label(popup, text="Hesap Numarası:", font=("Helvetica", 14))
        self.hesap_label.pack()
        self.hesap_entry = tk.Entry(popup, font=("Helvetica", 14))
        self.hesap_entry.pack()

        self.button = tk.Button(popup, text="Hesabı Sil", command=self.hesap_silme, font=("Helvetica", 14))
        self.button.pack(pady=20)

    def hesap_silme(self):
        hesap_numarasi = self.hesap_entry.get()
        hesap = self.banka.hesap_numarasi_kontrolu(hesap_numarasi)
        if hesap:
            hesap.hesap_kapatmak()

    def hesap_aktif_etme_popup(self):
        popup = tk.Toplevel()
        popup.title("Hesap Aktif Etme")
        popup.geometry("400x150")
        label = tk.Label(popup, text="Hesap Aktif Etme Ekranı", font=("Helvetica", 16))
        label.pack(pady=10)

        self.hesap_label = tk.Label(popup, text="Hesap Numarası:", font=("Helvetica", 14))
        self.hesap_label.pack()
        self.hesap_entry = tk.Entry(popup, font=("Helvetica", 14))
        self.hesap_entry.pack()

        self.button = tk.Button(popup, text="Hesabı Aktif Et", command=self.hesap_aktif_etme, font=("Helvetica", 14))
        self.button.pack(pady=20)

    def hesap_aktif_etme(self):
        hesap_numarasi = self.hesap_entry.get()
        hesap = self.banka.hesap_numarasi_kontrolu(hesap_numarasi)
        if hesap:
            hesap.hesap_aktif_etmek()

    def bakiye_sorgulama_popup(self):
        popup = tk.Toplevel()
        popup.title("Bakiye Sorgulama")
        popup.geometry("400x150")
        label = tk.Label(popup, text="Bakiye Sorgulama Ekranı", font=("Helvetica", 16))
        label.pack(pady=10)

        self.hesap_label = tk.Label(popup, text="Hesap Numarası:", font=("Helvetica", 14))
        self.hesap_label.pack()
        self.hesap_entry = tk.Entry(popup, font=("Helvetica", 14))
        self.hesap_entry.pack()

        self.button = tk.Button(popup, text="Sorgula", command=self.bakiye_sorgulama, font=("Helvetica", 14))
        self.button.pack(pady=20)

    def bakiye_sorgulama(self):
        hesap_numarasi = self.hesap_entry.get()
        hesap = self.banka.hesap_numarasi_kontrolu(hesap_numarasi)
        if hesap:
            hesap.bakiye_sorgulama()


class Musteri:
    def __init__(self, ad, soyad):
        self.musteri_numarası = random.randint(10000000, 99999999)
        self.ad = ad
        self.soyad = soyad


class Hesap:
    def __init__(self, hesap_numarasi, musteri, bakiye=0):
        self.hesap_numarasi = hesap_numarasi
        self.musteri = musteri
        self.bakiye = bakiye
        self.acik_hesap = True

    def para_yatirmak(self, miktar):
        if self.acik_hesap and miktar > 0:
            self.bakiye += miktar
            self.guncelle_hesap()
            messagebox.showinfo("Başarılı", f"{miktar} TL yatırıldı.\nŞuanki Hesap Bakiyesi: {self.bakiye}")
        elif not self.acik_hesap:
            messagebox.showerror("Hata", "Hesap kapalıdır.")
        else:
            messagebox.showerror("Hata", "Girdiğiniz miktar yanlıştır.")

    def para_cekmek(self, miktar):
        if self.acik_hesap and miktar > 0 and miktar <= self.bakiye:
            self.bakiye -= miktar
            self.guncelle_hesap()
            messagebox.showinfo("Başarılı", f"{miktar} TL çekildi.\nŞuanki Hesap Bakiyesi: {self.bakiye}")
        elif not self.acik_hesap:
            messagebox.showerror("Hata", "Hesap Kapalıdır.")
        elif miktar > self.bakiye:
            messagebox.showerror("Hata", "Girilen miktar hesap bakiyesinden fazladır.")
        else:
            messagebox.showerror("Hata", "Girdiğiniz miktar yanlıştır.")

    def bakiye_sorgulama(self):
        if self.acik_hesap:
            messagebox.showinfo("Bakiye Sorgulama", f"Şuanki hesap bakiyeniz: {self.bakiye} TL")
        else:
            messagebox.showerror("Hata", "Hesap Kapalıdır.")

    def hesap_kapatmak(self):
        if self.acik_hesap:
            self.acik_hesap = False
            self.guncelle_hesap()
            messagebox.showinfo("Başarılı", "Hesap başarılı bir şekilde kapatıldı.")
        else:
            messagebox.showerror("Hata", "Hesap Zaten Kapalıdır.")

    def hesap_aktif_etmek(self):
        if not self.acik_hesap:
            self.acik_hesap = True
            self.guncelle_hesap()
            messagebox.showinfo("Başarılı", "Hesap başarılı bir şekilde aktif edildi.")
        else:
            messagebox.showerror("Hata", "Hesap Zaten Aktiftir.")

    def guncelle_hesap(self):
        connection = sqlite3.connect("banka.db")
        cursor = connection.cursor()
        cursor.execute('UPDATE Hesaplar SET bakiye=?, acik_hesap=? WHERE hesap_numarasi=?',
                       (self.bakiye, 1 if self.acik_hesap else 0, self.hesap_numarasi))
        connection.commit()
        connection.close()


class Banka:
    def __init__(self):
        self.baglanti_olustur()

    def baglanti_olustur(self):
        self.connection = sqlite3.connect("banka.db")
        self.cursor = self.connection.cursor()

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Musteriler(
            musteri_numarası  INTEGER PRIMARY KEY,
            ad VARCHAR(100),
            soyad VARCHAR(100)
            )
        ''')

        self.cursor.execute('''
             CREATE TABLE IF NOT EXISTS Hesaplar(
             hesap_numarasi INTEGER PRIMARY KEY,
             musteri_numarası INTEGER,
             bakiye REAL,
             acik_hesap BIT,
             FOREIGN KEY (musteri_numarası) REFERENCES Musteriler (musteri_numarası)
             )
        ''')
        self.connection.commit()

    def hesap_olusturmak(self, musteri):
        hesap_numarasi = random.randint(100000, 999999)
        hesap = Hesap(hesap_numarasi, musteri)
        self.kaydet_musteri(musteri)
        self.kaydet_hesap(hesap)
        return hesap

    def kaydet_musteri(self, musteri):
        self.cursor.execute('INSERT INTO Musteriler VALUES (?,?,?)',
                            (musteri.musteri_numarası, musteri.ad, musteri.soyad))
        self.connection.commit()

    def kaydet_hesap(self, hesap):
        self.cursor.execute('INSERT INTO Hesaplar VALUES (?,?,?,?)',
                            (hesap.hesap_numarasi, hesap.musteri.musteri_numarası, hesap.bakiye,
                             1 if hesap.acik_hesap else 0))
        self.connection.commit()

    def tum_hesaplar(self, master):
        self.cursor.execute('SELECT * FROM Hesaplar')
        hesap_rows = self.cursor.fetchall()

        for row in hesap_rows:
            hesap_numarasi, musteri_numarasi, bakiye, acik_hesap = row

            musteri = self.musteri_getir(musteri_numarasi)
            hesap = Hesap(hesap_numarasi, musteri, bakiye)
            hesap.acik_hesap = True if acik_hesap == 1 else False

            label = tk.Label(master, text=f"Hesap Numarası: {hesap.hesap_numarasi}, "
                                           f"Müşteri: {musteri.ad} {musteri.soyad}, "
                                           f"Bakiye: {hesap.bakiye}, "
                                           f"Hesap Durumu: {'Açık' if hesap.acik_hesap else 'Kapalı'}",
                             font=("Helvetica", 12))
            label.pack()

    def tum_musteriler(self, master):
        self.cursor.execute('SELECT * FROM Musteriler')
        musteri_rows = self.cursor.fetchall()

        for row in musteri_rows:
            musteri_numarası, ad, soyad = row

            label = tk.Label(master, text=f"Müşteri Numarası: {musteri_numarası}, "
                                           f"Ad: {ad}, Soyad: {soyad}",
                             font=("Helvetica", 12))
            label.pack()

    def musteri_getir(self, musteri_numarası):
        self.cursor.execute('SELECT * FROM Musteriler WHERE musteri_numarası=?', (musteri_numarası,))
        musteri_row = self.cursor.fetchone()

        if musteri_row:
            musteri = Musteri(musteri_row[1], musteri_row[2])
            return musteri
        else:
            return None

    def hesap_numarasi_kontrolu(self, hesap_numarasi):
        self.cursor.execute('SELECT * FROM Hesaplar WHERE hesap_numarasi=?', (hesap_numarasi,))
        hesap_row = self.cursor.fetchone()

        if hesap_row:
            musteri = self.musteri_getir(hesap_row[1])
            hesap = Hesap(hesap_row[0], musteri, hesap_row[2])
            hesap.acik_hesap = True if hesap_row[3] == 1 else False
            return hesap
        else:
            messagebox.showerror("Hata", "Hesap Bulunamadı")
            return None


root = tk.Tk()
banka_gui = BankaGUI(root)
root.mainloop()
