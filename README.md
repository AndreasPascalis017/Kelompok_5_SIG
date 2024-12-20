# Kelompok 5 SIG

---

## **Anggota**

| **NO** | **Anggota**                     | **NIM**       |
|--------|--------------------------------|---------------|
| 1      | Andreas Pascalis Tristan       | 121140017     |
| 2      | Dimas Saputra                  | 121140059     |
| 3      | Dhian Adi Nugraha              | 121140055     |
| 4      | Fadel Malik                    | 121140165     |
| 5      | Muhammad Taqy Abdullah         | 121140166     |

---

## **Deskripsi Singkat**

Proyek ini adalah aplikasi berbasis web yang membantu pengguna menentukan jarak dan lokasi SMA Negeri terdekat di Kota Bandar Lampung. Aplikasi ini menggunakan peta interaktif yang memungkinkan pengguna memasukkan lokasi mereka secara manual untuk menemukan SMA Negeri terdekat.

**Fitur Utama:**
- Menampilkan peta interaktif dengan lokasi semua SMA Negeri di Kota Bandar Lampung.
- Menghitung jarak antara lokasi pengguna dan sekolah terdekat.
- Menampilkan sekolah dengan jarak terdekat berdasarkan koordinat input pengguna.

---

## **Cara Penggunaan**

1. Jalankan aplikasi web dengan menjalankan file Python utama `app.py`.
2. Setelah aplikasi berjalan, buka browser dan akses URL yang ditampilkan.
3. Pada halaman web, Anda akan melihat peta interaktif yang menampilkan lokasi SMA Negeri di Bandar Lampung.
4. Masukkan koordinat lokasi Anda secara manual.
5. Sistem akan menampilkan sekolah dengan jarak terdekat beserta informasi detailnya.

---

## **Cara Instalasi**

### **Persyaratan**
Pastikan Anda memiliki Python dan `pip` yang sudah diinstal pada sistem Anda.

**Daftar Library:**
- flask
- geopy

### **Langkah Instalasi**

1. Download repositori proyek dalam format ZIP melalui GitHub dan ekstrak file-nya.

2. Instal semua library yang diperlukan:
   ```bash
   pip install flask geopy
   ```

3. (Opsional) Jika Anda menggunakan sistem pengelolaan dependensi seperti `venv` atau `virtualenv`, aktifkan environment virtual Anda sebelum instalasi.

4. Jalankan server aplikasi:
   ```bash
   python app.py
   ```

5. Akses aplikasi melalui browser pada URL `http://127.0.0.1:5000` atau URL yang sesuai ditampilkan di konsol.

---

## **Struktur File**

- `app.py`: Skrip utama untuk menjalankan aplikasi web.
- `templates/index.html`: Template HTML untuk antarmuka pengguna.
- `sebaran-sma-bandar-lampung.geojson`: File GeoJSON yang berisi data lokasi SMA Negeri di Kota Bandar Lampung.

---

## **Pengembang**
Dibuat oleh Kelompok 5 SIG dalam rangka menyelesaikan tugas akhir mata kuliah Sistem Informasi Geografis.

