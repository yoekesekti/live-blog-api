# Live Blog API

## Deskripsi
Project ini membuat ulang Live Blog menyerupai referensi API [IP/API URL].  
Dikembangkan menggunakan **Python FastAPI** dan **SQLite/PostgreSQL** sebagai database.  
Project ini digunakan untuk tugas kuliah.

---

## Fitur
- **Register User:** Membuat akun baru.
- **Login:** Masuk ke sistem untuk user terdaftar.
- **Post Artikel:** Membuat, melihat, mengupdate, dan menghapus post.
- **Swagger UI:** Dokumentasi API interaktif.

---

## Teknologi
- Python 3.x
- FastAPI
- Uvicorn
- SQLAlchemy / Tortoise ORM
- SQLite / PostgreSQL
- Pydantic

---

## Struktur Folder
live-blog-api/
│
├─ main.py # File utama FastAPI
├─ models.py # Definisi model database
├─ routes.py # Endpoint API
├─ requirements.txt
└─ README.md


---

## Instalasi
1. Clone repository:

git clone https://github.com/username/live-blog-api.git


2. Masuk folder project:
cd live-blog-api

3. Install dependencies:
pip install -r requirements.txt


## Menjalankan API
1. Jalankan server:
uvicorn main:app --reload

2. Buka Swagger UI di browser:
http://127.0.0.1:8000/docs

## Input data
1. Postman
2. Swegger
   
## Buka UI menggunakan Live Server
Install Live Server di VS Code (jika belum ada):
Buka VS Code → Extensions → cari Live Server → Install
Buka folder project di VS Code
Klik kanan index.html → Open with Live Server
Browser akan terbuka otomatis, misal di http://127.0.0.1:5500
