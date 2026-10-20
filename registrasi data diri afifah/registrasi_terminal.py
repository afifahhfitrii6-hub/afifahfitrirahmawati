import json
import os

FILE_DATA = "data_diri.json"

# Warna pink untuk teks di terminal VS Code
PINK = "\033[95m"
LIGHT_PINK = "\033[38;5;218m"
RESET = "\033[0m"


def pink(teks):
    return f"{PINK}{teks}{RESET}"


def muat_data():
    if os.path.exists(FILE_DATA):
        try:
            with open(FILE_DATA, "r", encoding="utf-8") as file:
                return json.load(file)
        except (json.JSONDecodeError, OSError):
            print(pink("File data tidak bisa dibaca."))
    return []


def simpan_data(data):
    with open(FILE_DATA, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def tampilkan_data(biodata):
    print(pink("\n" + "=" * 40))
    print(pink("               DATA DIRI"))
    print(pink("=" * 40))
    for kunci, nilai in biodata.items():
        print(f"{LIGHT_PINK}{kunci:<22}: {nilai}{RESET}")
    print(pink("=" * 40))


def registrasi():
    data = muat_data()
    print(pink("\n=== REGISTRASI DATA DIRI ==="))

    nik = input(pink("Masukkan NIK (16 angka): ")).strip()
    if not nik.isdigit() or len(nik) != 16:
        print(pink("NIK harus terdiri dari 16 angka."))
        return

    if any(item["NIK"] == nik for item in data):
        print(pink("NIK sudah terdaftar!"))
        return

    kolom = [
        ("Nama Lengkap", "Nama lengkap"),
        ("Tempat Lahir", "Tempat lahir"),
        ("Tanggal Lahir", "Tanggal lahir (DD-MM-YYYY)"),
        ("Jenis Kelamin", "Jenis kelamin"),
        ("Alamat", "Alamat"),
        ("Agama", "Agama"),
        ("Status Perkawinan", "Status perkawinan"),
        ("Pekerjaan", "Pekerjaan"),
        ("Kewarganegaraan", "Kewarganegaraan"),
    ]

    biodata = {"NIK": nik}
    for kunci, pertanyaan in kolom:
        nilai = input(pink(f"{pertanyaan}: ")).strip()
        if not nilai:
            print(pink("Semua data harus diisi. Registrasi dibatalkan."))
            return
        biodata[kunci] = nilai

    data.append(biodata)
    simpan_data(data)
    print(pink("\nRegistrasi berhasil!"))
    tampilkan_data(biodata)


def cari_data():
    data = muat_data()
    nik = input(pink("\nMasukkan NIK yang dicari: ")).strip()

    for biodata in data:
        if biodata["NIK"] == nik:
            tampilkan_data(biodata)
            return

    print(pink("Data tidak ditemukan!"))


def tampilkan_semua():
    data = muat_data()
    if not data:
        print(pink("\nBelum ada data yang terdaftar."))
        return

    print(pink(f"\nJumlah data terdaftar: {len(data)}"))
    for nomor, biodata in enumerate(data, start=1):
        print(pink(f"\nData ke-{nomor}"))
        tampilkan_data(biodata)


def menu():
    while True:
        print(pink("\n" + "=" * 40))
        print(pink("       APLIKASI REGISTRASI DATA DIRI"))
        print(pink("=" * 40))
        print(pink("1. Registrasi data diri"))
        print(pink("2. Cari dan tampilkan data"))
        print(pink("3. Tampilkan semua data"))
        print(pink("4. Keluar"))
        print(pink("=" * 40))

        pilihan = input(pink("Pilih menu (1-4): ")).strip()

        if pilihan == "1":
            registrasi()
        elif pilihan == "2":
            cari_data()
        elif pilihan == "3":
            tampilkan_semua()
        elif pilihan == "4":
            print(pink("Terima kasih telah menggunakan aplikasi!"))
            break
        else:
            print(pink("Pilihan tidak valid. Silakan coba lagi."))


if __name__ == "__main__":
    menu()