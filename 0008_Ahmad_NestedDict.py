import datetime
import os

perpustakaan = {}
no_urut = {}   # penghitung nomor urut tiap kategori

while True:
    os.system("cls" if os.name == "nt" else "clear")
    print(f"{'SISTEM PERPUSTAKAAN SEDERHANA':^40}")
    print("-" * 40)

    kategori = input("Kode kategori (contoh: NOV): ").upper()
    judul = input("Judul buku: ")
    penulis = input("Penulis: ")
    tahun_terbit = int(input("Tahun terbit: "))

    print("Tanggal terakhir dipinjam:")
    tahun = int(input("  Tahun (YYYY): "))
    bulan = int(input("  Bulan (1-12): "))
    tanggal = int(input("  Tanggal (1-31): "))

    pilih = input("Status (1 = Tersedia, 2 = Tidak Tersedia): ")
    status = "TERSEDIA" if pilih == "1" else "TIDAK TERSEDIA"

    # multi-keys: kunci berupa tuple (kategori, nomor urut)
    no_urut[kategori] = no_urut.get(kategori, 0) + 1
    kunci = (kategori, no_urut[kategori])

    # nesting dictionary: nilai berupa dictionary data buku
    perpustakaan[kunci] = {
        'judul': judul,
        'penulis': penulis,
        'tahun_terbit': tahun_terbit,
        'terakhir_pinjam': datetime.datetime(tahun, bulan, tanggal),
        'status': status
    }

    print(f"\n{'KEYS':<9} {'JUDUL BUKU':<20} {'PENULIS':<15} {'TERBIT':<7} {'TERAKHIR PINJAM':<16} {'STATUS':<15}")
    print("-" * 85)

    for kunci in perpustakaan:
        kode = f"{kunci[0]}-{kunci[1]:03d}"
        buku = perpustakaan[kunci]
        pinjam = buku['terakhir_pinjam'].strftime("%d-%m-%Y")
        print(f"{kode:<9} {buku['judul']:<20} {buku['penulis']:<15} {buku['tahun_terbit']:<7} {pinjam:<16} {buku['status']:<15}")

    lanjut = input("\nMau tambah buku lagi (y/n)? ")
    if lanjut == "n":
        break

print("\nAkhir dari program, terima kasih")