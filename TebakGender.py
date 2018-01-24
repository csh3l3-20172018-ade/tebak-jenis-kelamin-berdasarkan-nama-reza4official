nama = input("Nama: ")  # Inputan nama
cw = 0
x = 0

for cewek in range(len(nama)):  # Fungsi cek huruf i, a, u, e, t, l untuk perempuan
    if nama == ' ': break #Pemberhentian perulangan jika bertemu spasi
    if nama[cewek] == "i":
        cw = cw + 1
    if nama[cewek] == "a":
        cw = cw + 1
    if nama[cewek] == "u":
        cw = cw + 1
    if nama[cewek] == "e":
        cw = cw + 1
    if nama[cewek] == "t":
        cw = cw + 1
    if nama[cewek] == "l":
        cw = cw + 1

laki2 = cw
co = 0
for cowok in range(len(nama)):  # Fungsi cek huruf i, a, u, e, t, l untuk laki-laki
    if nama == ' ': break #Pemberhentian perulangan jika bertemu spasi
    if nama[cowok] == "b":
        co = co + 1
    if nama[cowok] == "d":
        co = co + 1
    if nama[cowok] == "o":
        co = co + 1

if cw > co:  # Perbandingan untuk menentukan apakah output gender berupa perempuan, laki-laki, atau tidak diketahui
    print("Perempuan")
elif (cw == co):
    print("Tidak Diiketahui")
else:
    print("Laki-laki")

# Rata-rata output program menampilkan output "Perempuan" termasuk nama saya sendiri.
# Hal ini dikarenakan lebih banyaknya opsi huruf vokal di function untuk Perempuan.
# Dan semua nama lebih banyak menggunakan huruf vokal a, i, u, e yang ada di function Perempuan dibandingkan huruf vokal o di function Laki-laki
