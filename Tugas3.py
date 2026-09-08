batas_nilai = (65,100)
nilai_masuk = []
lulus = []
remedi = []

print("INPUT NILAI UJIAN MAHASISWA")
print("ketik 'selesai' untuk mengakhiri input.\n")

while True:
    inputan = input("Masukkan nilai mahasiswa: ")

    if inputan.lower() == "selesai":
        if len(nilai_masuk) < 5:
            print("(!) Harap masukkan minimal 5 nilai terlebih dahulu.\n")
            continue

        lulus = [n for n in nilai_masuk if n >= batas_nilai[0]]
        remedi = [n for n in nilai_masuk if n < batas_nilai[0]]

        if len(lulus) == 0 or len(remedi) == 0:
            print(
                "(!) Data harus memuat minimal satu nilai LULUS dan satu nilai REMEDI.\n"
                )
            continue

        break

    try:
        nilai = float(inputan)
        if 0 <= nilai <= batas_nilai[1]:
            nilai_masuk.append(nilai)
            print(f"-> Nilai {nilai} berhasil ditambahkan. ")
        else:
            print(f"(!) Nilai harus berada dalam rentang 0 - {batas_nilai[1]}")
    except ValueError:
        print("(!) Input tidak valid. Masukkan angka atau ketik 'selesai'. ")

print("\n PEMERIKSAAN & HAPUS DATA  ")
while True:
    print(f"Data nilai saat ini: {nilai_masuk}")
    pilihan = input(
        "Apakah ada nilai yang ingin dihapus? (ya/tidak): "
    ).lower()

    if pilihan == "ya":
        try:
            nilai_hapus = float(
                input("Masukkan nilai yang ingin dihapus: ")
            )
            if nilai_hapus in nilai_masuk:
                nilai_masuk.remove(nilai_hapus)

                if nilai_hapus >= batas_nilai[0]:
                    lulus.remove(nilai_hapus)
                else:
                    remedi.remove(nilai_hapus)

                print(f"-> Nilai {nilai_hapus} berhasil dihapus.\n")
            else:
                print("(!) Nilai tersebut tidak ada dalam list.\n")
        except ValueError:
            print("(!) Input angka tidak valid.\n")
    elif pilihan == "tidak":
        break
    else:
        print("(!) Ketik 'ya' atau 'tidak'.\n")

print(" REKAPITULASI NILAI" )

print(f"Seluruh Nilai Masuk : {nilai_masuk}")
print(f"Daftar Nilai Lulus : {lulus}")
print(f"Daftar Nilai Remedi : {remedi}")