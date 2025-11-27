# 🟧 Fake / Dummy JWT Generator (Unsigned, "alg": "none")

Script Python sederhana untuk membuat **JWT unsigned** dengan algoritma `"none"`.  
Cocok untuk kebutuhan debugging, testing sistem autentikasi, eksplorasi struktur JWT, atau demonstrasi keamanan.

⚠️ **PERINGATAN: Token ini TIDAK aman. Jangan digunakan untuk produksi.**  
Ini hanya untuk edukasi & pengujian.

---

## 🚀 Fitur
- Membuat JWT dummy tanpa signature (`alg: none`)
- Payload bisa dikustomisasi dari CLI
- Base64URL encoding tanpa padding
- Sangat ringan & tanpa dependency eksternal

---

## 📌 Contoh Penggunaan

### 1. Generate token default
```bash
python3 fake_jwt.py

---

# 🧪 JWT Decoder (Opsional)

Anda juga dapat mendecode header & payload JWT menggunakan script berikut:

## 📄 File: `decode_jwt.py`

Script ini hanya membaca dan mengdecode JWT tanpa memverifikasi signature.

### 🔧 Cara Menggunakan

```bash
python3 decode_jwt.py <token_jwt>
