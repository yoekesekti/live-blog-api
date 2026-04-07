# Live Blog API

## Deskripsi
Project ini membuat ulang Live Blog berupa pesan anonimus

---

## Fitur
- **Register User:** Membuat akun baru.
- **Login:** Masuk ke sistem untuk user terdaftar.
- **Post Artikel:**
- **Swagger UI:** Dokumentasi API interaktif.


---

## Instalasi
1. Clone repository:

git clone https://github.com/yoekesekti/live-blog-api.git


2. Masuk folder project dan install uvicorn:
cd live-blog-api
venv\Scripts\activate
pip install fastapi uvicorn


## Menjalankan API
1. Jalankan server:
uvicorn main:app --reload

2. Buka Swagger UI di browser:
http://127.0.0.1:8000/docs

## Input data menggunakan: 
1. Postman
2. Swegger
   
## Buka UI menggunakan Live Server
1. Install Live Server di VS Code (jika belum ada):
2. Buka VS Code → Extensions → cari Live Server → Install
3. Buka folder project di VS Code
4. Klik kanan index.html → Open with Live Server
5. Browser akan terbuka otomatis, misal di http://127.0.0.1:5500
