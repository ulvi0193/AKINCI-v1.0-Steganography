import os
import sys
import time
import tkinter as tk
from tkinter import ttk, messagebox, filedialog

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_cool_ascii():
    clear_screen()
    os.system('') # Windows ANSI renk uyumu için
    
    red = "\033[31m"
    white = "\033[37m"
    cyan = "\033[36m"
    gold = "\033[33m"
    reset = "\033[0m"

    logo = f"""
{red}    ███████████████████████████████████████████████████████████████
{red}    █████████████████████{white}▄▄███████▄▄{red}███████████████████████████████
{red}    ███████████████████{white}▄█████████████▄{red}█████████████████████████████
{red}    ██████████████████{white}████████▀▀▀▀▀▀▀{red}██████████████████████████████
{red}    █████████████████{white}███████▀{red}██████████████{white}▄██▄{red}████████████████████
{red}    █████████████████{white}███████{red}█████████████{white}▄██████▄{red}██████████████████
{red}    █████████████████{white}███████{red}█████████████{white}▀▀████▀▀{red}██████████████████
{red}    █████████████████{white}███████▄{red}██████████████{white}▀██▀{red}████████████████████
{red}    ██████████████████{white}████████▄▄▄▄▄▄▄{red}██████████████████████████████
{red}    ███████████████████{white}▀█████████████▀{red}█████████████████████████████
{red}    █████████████████████{white}▀▀███████▀▀{red}███████████████████████████████
{red}    ███████████████████████████████████████████████████████████████
{white}        ================================================================
{red}           ██████╗ ██╗  ██╗██╗███╗   ██╗ █████ ██
{red}          ██╔══██╗██║ ██╔╝██║████╗  ██║██╔════╝██║
{red}          ███████║█████╔╝ ██║██╔██╗ ██║██║     ██║ 
{red}          ██╔══██║██╔═██╗ ██║██║╚██╗██║██║     ██║  
{red}          ██║  ██║██║  ██╗██║██║ ╚████║╚██████╗██║  
{red}          ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝╚═╝  
{white}        ================================================================
{cyan}                 >> DEVELOPED BY : Ülvi Eyvazzadə <<
{gold}                 >> STATUS       : STEGANOGRAPHY & CRYPTO GUARD <<
{white}        ================================================================

[*] Şanlı Bayrak Altında Güvenlik Servisleri Başlatılıyor...
[*] Grafik Arayüzü (GUI) Yükleniyor, Lütfen Bekleyin...
"""
    print(logo)
    time.sleep(2.5)

print_cool_ascii()

class AkinciMuhafiz:
    def __init__(self, root):
        self.root = root
        self.root.title("AKINCI v1.0 - Ülvi Eyvazzadə")
        self.root.geometry("600x450")
        self.root.configure(bg="#0a0a0a")
        self.root.resizable(False, False)

        # Stil Ayarları
        self.style = ttk.Style()
        self.style.theme_use("clam")
        self.style.configure("TNotebook", background="#0a0a0a", borderwidth=0)
        self.style.configure("TNotebook.Tab", background="#151515", foreground="#ffffff", font=("Courier", 10, "bold"), padding=[15, 5])
        self.style.map("TNotebook.Tab", background=[("selected", "#ce1212")], foreground=[("selected", "#ffffff")])

        # Başlık Bannerı
        title_label = tk.Label(root, text="⚡ AKINCI MUHAFIZ v1.0 ⚡", font=("Courier", 22, "bold"), fg="#ce1212", bg="#0a0a0a")
        title_label.pack(pady=10)
        subtitle = tk.Label(root, text="Geliştirici: Ülvi Eyvazzadə", font=("Arial", 9, "italic"), fg="#666666", bg="#0a0a0a")
        subtitle.pack()

        # Sekmeler
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill="both", expand=True, padx=15, pady=15)

        self.tab1 = tk.Frame(self.notebook, bg="#111111")
        self.tab2 = tk.Frame(self.notebook, bg="#111111")

        self.notebook.add(self.tab1, text=" MESAJI DOSYAYA GİZLE ")
        self.notebook.add(self.tab2, text=" GİZLİ MESAJI ÇÖZ ")

        self.init_encrypt_tab()
        self.init_decrypt_tab()

    def init_encrypt_tab(self):
        lbl_msg = tk.Label(self.tab1, text="Gizlenecek Mesaj veya Link:", font=("Arial", 10, "bold"), fg="#ffffff", bg="#111111")
        lbl_msg.pack(pady=10)
        
        self.txt_message = tk.Entry(self.tab1, font=("Arial", 10), width=50, bg="#222222", fg="#ffffff", borderwidth=0, insertbackground="white")
        self.txt_message.pack(pady=5)

        btn_file = tk.Button(self.tab1, text="Kapak Fotoğrafı Seç (.jpg/.png)", font=("Arial", 9, "bold"), bg="#333333", fg="#ffffff", command=self.select_file_enc, borderwidth=0)
        btn_file.pack(pady=15)

        self.lbl_file_path_enc = tk.Label(self.tab1, text="Dosya Seçilmedi", font=("Arial", 8, "italic"), fg="#888888", bg="#111111")
        self.lbl_file_path_enc.pack()

        btn_start = tk.Button(self.tab1, text="İÇİNE GİZLE VE KAYDET", font=("Courier", 11, "bold"), bg="#ce1212", fg="#ffffff", width=30, command=self.hide_message, borderwidth=0)
        btn_start.pack(pady=25)

    def init_decrypt_tab(self):
        lbl_dec = tk.Label(self.tab2, text="İçinde Mesaj Gizli Olan Dosyayı Seçin:", font=("Arial", 10, "bold"), fg="#ffffff", bg="#111111")
        lbl_dec.pack(pady=15)

        btn_file_dec = tk.Button(self.tab2, text="Dosya Seç", font=("Arial", 9, "bold"), bg="#333333", fg="#ffffff", command=self.select_file_dec, borderwidth=0)
        btn_file_dec.pack(pady=10)

        self.lbl_file_path_dec = tk.Label(self.tab2, text="Dosya Seçilmedi", font=("Arial", 8, "italic"), fg="#888888", bg="#111111")
        self.lbl_file_path_dec.pack(pady=5)

        btn_decode = tk.Button(self.tab2, text="GİZLİ MESAJI ÇIKAR", font=("Courier", 11, "bold"), bg="#ce1212", fg="#ffffff", width=30, command=self.extract_message, borderwidth=0)
        btn_decode.pack(pady=20)

        self.txt_result = tk.Entry(self.tab2, font=("Courier", 11, "bold"), width=50, bg="#050505", fg="#00ff00", borderwidth=0, justify="center")
        self.txt_result.pack(pady=15)

    def select_file_enc(self):
        self.file_path_enc = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg *.png *.jpeg")])
        if self.file_path_enc:
            self.lbl_file_path_enc.config(text=os.path.basename(self.file_path_enc), fg="#00ff00")

    def select_file_dec(self):
        self.file_path_dec = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg *.png *.jpeg")])
        if self.file_path_dec:
            self.lbl_file_path_dec.config(text=os.path.basename(self.file_path_dec), fg="#00ff00")

    def hide_message(self):
        try:
            msg = self.txt_message.get()
            if not msg or not hasattr(self, 'file_path_enc') or not self.file_path_enc:
                messagebox.showwarning("Hata", "Lütfen hem bir mesaj yazın hem de dosya seçin!")
                return
            
            save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG Image", "*.png")])
            if not save_path:
                return

            with open(self.file_path_enc, "rb") as f:
                file_bytes = f.read()

            secret_data = b"##AKINCI##" + msg.encode('utf-8') + b"##AKINCI##"
            
            with open(save_path, "wb") as f:
                f.write(file_bytes + secret_data)

            messagebox.showinfo("Başarılı", "Mesajınız fotoğrafın içine başarıyla gizlendi ve kaydedildi!")
        except Exception as e:
            messagebox.showerror("Hata", f"İşlem başarısız oldu: {e}")

    def extract_message(self):
        try:
            if not hasattr(self, 'file_path_dec') or not self.file_path_dec:
                messagebox.showwarning("Hata", "Lütfen içinde veri gizli olan bir dosya seçin!")
                return

            with open(self.file_path_dec, "rb") as f:
                file_bytes = f.read()

            start_marker = b"##AKINCI##"
            if start_marker in file_bytes:
                parts = file_bytes.split(start_marker)
                secret_msg = parts[1].decode('utf-8')
                self.txt_result.delete(0, tk.END)
                self.txt_result.insert(0, secret_msg)
                messagebox.showinfo("Başarılı", "Gizli mesaj başarıyla çözüldü!")
            else:
                self.txt_result.delete(0, tk.END)
                self.txt_result.insert(0, "Temiz / Gizli Mesaj Bulunamadı.")
        except Exception as e:
            messagebox.showerror("Hata", f"Mesaj çözülemedi: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = AkinciMuhafiz(root)
    root.mainloop()
