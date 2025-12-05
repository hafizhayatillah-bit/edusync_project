import smtplib
import datetime as dt
import os

# with open("debug_log.txt", "a") as f:
#     f.write(f"[{dt.datetime.now()}] Script started\n")
#
# with open("debug_log.txt", "a") as f:
#     f.write(f"[{dt.datetime.now()}] Script ended\n")

my_email = "hafizh.ayatillah@gmail.com"
password = "widkidgktthhxhgy"
# to_email = "mfarras337@gmail.com"
to_email = "naufalmuyassar23@gmail.com"
# to_email = "hafizhayatillah1024@gmail.com"

# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
# day = now.day
# print(day_of_week)

# Ambil tanggal hari ini
now = dt.datetime.now()
day_index = now.toordinal()  # angka unik per hari

# Ambil path absolut ke folder tempat script ini berada
base_dir = os.path.dirname(os.path.abspath(__file__))

# Gabungkan dengan nama file quotes.txt
quotes_path = os.path.join(base_dir, "quotes.txt")

# Buka file dengan path yang benar
with open(quotes_path, "r", encoding="utf-8") as file:
    quotes = file.readlines()

# Pilih quote berdasarkan hari
quote_today = quotes[day_index % len(quotes)].strip()

# Format isi email
subject = "Your Daily Quote"
message = f"Subject: {subject}\n\n{quote_today}"

# Kirim email
with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs=to_email,
        msg=message
    )