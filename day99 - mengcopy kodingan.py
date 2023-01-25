def copy():
    try : 
        nama_file = str(input("masukkan nama file yang ingin dicopy : "))
        file = open(f"{nama_file}.py","r")
        isi_file = file.read()
        jumlah_salinan = 1
        while True : 
            try :
                file_salinan = open(f"{nama_file} copy({jumlah_salinan}).py","x")
                file_salinan = open(f"{nama_file} copy({jumlah_salinan}).py","w")
                file_salinan.write(isi_file)
                file_salinan.close()
                print("kodingan sukses dicopy")
                break
            except FileExistsError :
                jumlah_salinan += 1
    except FileNotFoundError :
        print("file tidak ditemukan!")
        copy()
          
copy()