from view.view_nilai import cari_data,lihat_data,header,notoption
from view.input_nilai import input_data,ubah_data,hapus_data
header()
while True:

    c = input("\nPilih Opsi: ")

    if c.lower() == 'k':
        print(".:TERIMAKASIH TELAH MENGGUNAKAN PROGRAM INI:.")
        ext = input("\nPress ENTER to exit")
        if ext == '':
            break
        else:a


    elif c.lower() == 'l':
        lihat_data()


    elif c.lower() == 't':
        input_data()


    elif c.lower() == 'u':
        ubah_data()


    elif c.lower() == 'c':
        cari_data()


    elif c.lower() == 'h':
        hapus_data()

    else:
        notoption()