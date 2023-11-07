print("@@@ @  @@@ @@@@   @   @ @ @@@@@@     @@@")
print("@ @ @ @  @ @   @  @   @ @ @     @   @   @")
print("@ @ @ @@@@ @  @   @@@@@ @ @@@@@@    @@@@@")
print("@ @@@ @  @ @@     @   @ @ @    @    @   @")

# Meminta input pengguna untuk kecepatan awal(vo),waktu(t),dan percepatan(a)
vo = float(input("Masukkan kecepatan awal vo (m/s): "))
t = float(input("Masukkan waktu t (detik): "))
a = float(input("Masukkan percepatan a (m/s^2): "))

# Menghitung jarak tempuh
s = vo * t + (1/2) * a * t**2

print(f"Jarak tempuh adalah {s} meter.")

