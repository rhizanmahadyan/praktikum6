def input_data():
    from model.daftar_nilai import tambah_data
    while (True):
        nama = input("NAMA   : ")
        if nama == '':
            print('Nama tidak boleh kosong')
        else:
            break
    while (True):
        try:
            nim = int(input("NIM    : "))
            if nim == '':
                print('Masukan Nim')
        except ValueError:
            print('Masukan Nim dengan Angka')
        else:
            break
    while (True):
        try:
            tugas = int(input("TUGAS  : "))
            if tugas == '':
                print('Masukan TUGAS')
        except ValueError:
            print('Masukan TUGAS dengan Angka')
        else:
            break
    while (True):
        try:
            uts = int(input("UTS    : "))
            if uts == '':
                print('Masukan UTS')
        except ValueError:
            print('Masukan UTS dengan Angka')
        else:
            break
    while (True):
        try:
            uas = int(input("UAS    : "))
            if uas == '':
                print('Masukan UAS')
        except ValueError:
            print('Masukan UAS dengan Angka')
        else:
            break
    tambah_data(nama, nim, tugas, uts, uas)
    print("\n    (T)ambah       (U)bah      (H)apus     (C)ari      (L)ihat     (K)eluar   ")


def ubah_data():
    from model.daftar_nilai import ubah_data
    ubah_data(nama=input("Masukan nama perubahan : "))


def hapus_data():
    from model.daftar_nilai import hapus_data
    hapus_data(nama=input("Masukan nama untuk menghapus data : "))
    print("\n    (T)ambah       (U)bah      (H)apus     (C)ari      (L)ihat     (K)eluar   ")


def cari_data():
    from model.daftar_nilai import cari_data
    cari_data(nama=input("Masukan nama yang di cari : "))