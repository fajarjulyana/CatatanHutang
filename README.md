
# 📒 Catatan Hutang

Aplikasi web berbasis **Python + Flask + SQLite** untuk mencatat dan mengelola hutang secara sederhana dan efisien.

---

## 🚀 Fitur Utama

* **Tambah Hutang**: Mencatat hutang baru dengan informasi lengkap.
* **Daftar Hutang**: Melihat semua catatan hutang yang telah dimasukkan.
* **Pembayaran**: Mencatat pembayaran terhadap hutang yang ada.
* **Status Hutang**: Menandai hutang sebagai lunas setelah pembayaran penuh.
* **Database SQLite**: Menyimpan data secara lokal menggunakan SQLite.

---

## 🛠 Teknologi yang Digunakan

* **Backend**: Python 3.x dengan Flask
* **Frontend**: HTML, CSS (Bootstrap 5)
* **Database**: SQLite
* **Form Handling**: WTForms([GitHub][1], [YouTube][2])

---

## 📦 Instalasi dan Penggunaan

1. **Clone repositori**:

   ```bash
   git clone https://github.com/fajarjulyana/CatatanHutang.git
   cd CatatanHutang
   ```



2. **Buat dan aktifkan virtual environment**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # Untuk Linux/Mac
   venv\Scripts\activate     # Untuk Windows
   ```



3. **Install dependensi**:

   ```bash
   pip install -r requirements.txt
   ```



4. **Jalankan aplikasi**:

   ```bash
   python app.py
   ```



5. **Akses aplikasi**:
   Buka browser dan kunjungi [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🗂 Struktur Direktori

```
CatatanHutang/
├── app.py            # File utama aplikasi Flask
├── forms.py          # Definisi form menggunakan WTForms
├── models.py         # Definisi model database
├── routes.py         # Routing aplikasi
├── seed_data.py      # Script untuk mengisi data awal (opsional)
├── templates/        # Folder untuk template HTML
│   ├── layout.html
│   ├── index.html
│   ├── add_debt.html
│   └── ...
├── static/           # Folder untuk file statis (CSS, JS, Gambar)
├── debt_tracker.db   # File database SQLite
├── requirements.txt  # Daftar dependensi Python
└── README.md         # Dokumentasi proyek
```


## 📝 Kontribusi

Kontribusi sangat diterima! Silakan fork repositori ini, buat cabang baru, dan ajukan pull request dengan fitur atau perbaikan yang Anda buat.

---

## 📄 Lisensi

Proyek ini dilisensikan di bawah **MIT License**.([GitHub][1])


[2]: https://www.youtube.com/watch?v=KO0FufpqC7c&utm_source=chatgpt.com "youtube.com/watch?v=ko0f..."
[3]: https://github.com/devcoderama/debt-notes-app/blob/main/README.md?utm_source=chatgpt.com "debt-notes-app/README.md at main - GitHub"
