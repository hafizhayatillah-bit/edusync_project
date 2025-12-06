import smtplib

# --- KONFIGURASI ---
EMAIL_PENGIRIM = "naufalmuyassar23@gmail.com"
EMAIL_PASSWORD = "lmmqxtemroevkqvn" # Bukan password login biasa!
EMAIL_PENERIMA = "hafizh.ayatillah@gmail.com"

isi_pesan = """\
Subject: Halo dari VS Code

Ini adalah pesan percobaan yang dikirim menggunakan Python di VS Code.
Keren kan?
"""

try:
    # Menghubungkan ke server Gmail
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls() # Enkripsi koneksi
        
        # Login
        smtp.login(EMAIL_PENGIRIM, EMAIL_PASSWORD)
        
        # Kirim Email
        smtp.sendmail(EMAIL_PENGIRIM, EMAIL_PENERIMA, isi_pesan)
        
        # Ini supaya ada tampilan di Terminal VS Code Anda
        print("------------------------------------------------")
        print("SUKSES! Email berhasil dikirim. Cek inbox sekarang.")
        print("------------------------------------------------")

except Exception as e:
    print("GAGAL mengirim email. Errornya:")
    print(e)