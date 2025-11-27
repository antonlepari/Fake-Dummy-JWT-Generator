# 🔐 Fake JWT Tools  
###### _Unsigned JWT Generator & Decoder for Debugging_  

![GitHub stars](https://img.shields.io/github/stars/<username>/<repo>?style=for-the-badge)
![GitHub forks](https://img.shields.io/github/forks/<username>/<repo>?style=for-the-badge)
![GitHub license](https://img.shields.io/github/license/<username>/<repo>?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge)

> Tools ringan untuk membuat **JWT unsigned (alg:none)** dan mendecode header/payload tanpa verifikasi signature.  
> Cocok untuk debugging, testing, dan edukasi keamanan JWT.

---

# 🚀 Fitur

### 🔧 Generator (fake_jwt.py)
- Membuat JWT **unsigned**
- Mendukung payload custom
- Base64URL encoding tanpa padding
- Tidak membutuhkan dependensi eksternal

### 🧩 Decoder (decode_jwt.py)
- Mendecode header & payload JWT
- Tanpa memverifikasi signature
- Output rapi dan mudah dibaca

---

# 📁 Struktur Repo
Fake-Dummy-JWT-Generator/
├── fake_jwt.py # Generator token JWT unsigned
├── decode_jwt.py # Decoder JWT (header & payload)
├── screenshot.png
└── README.md


---

# 🧰 Instalasi

Pastikan Python 3.8+ terinstall.

### Clone repo
```bash
git clone https://github.com/<username>/<repo>.git
cd <repo>


