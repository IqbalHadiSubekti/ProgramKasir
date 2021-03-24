def variable(): # function dan variabel
    global nama_menu
    global harga_menu
    global total
    total = 0
    nama_menu = { #mendefinisikan variabel menggunakan set
             1 : "1 .Tahu Bacem",
             2 : "2. Tempe Goreng",
             3 : "3. Ayam Goreng",
             4 : "4. Soto Ayam",
             5 : "5. Mie Goreng",
             6 : "6. Mie Rebus",
             7 : "7. Nasi Goreng",
             8 : "8. Nasi Rames"
             }
    harga_menu = {
              1 : 1500,
              2 : 1000,
              3 : 4000,
              4 : 6000,
              5 : 5000,
              6 : 5000,
              7 : 10000,
              8 : 8000
              }

def title(): #mendefinisikan function title
    print_list = [f"{'='*41}",f"={'PROGRAM KASIR'.center(39)}=",f"={'RUMAH MAKAN PELIPUR LAPAR'.center(39)}=",f"{'='*41}"]
    for i in print_list:
        print(i)
    print('') #print kosong
    
def menu():
    print(f"{'='*41}")
    for i in range(len(nama_menu)+1)[1:]: #len untuk menghitung panjang data/kelas
        print(f"= {nama_menu[i]}{' '*(29-len(nama_menu[i]))}={str(harga_menu[i]).center(8)}=")
    print(f"{'='*41}\n")
    
def count(): #memanggil pesanan
    global total
    print("UNTUK MEMESESAN MAKANAN MASUKAN\nBERDASARKAN ANGKA DI MENU")
    print("KETIK 'Sudah' UNTUK BERHENTI MEMESAN")
    print('='*41)
    while True:
        try:
            pilihan = input('Pilihan menu\t: ')
            if pilihan.isdigit():
                print(f"nama menu\t: {nama_menu[int(pilihan)]}")
                jumlah = input("Jumlah Pesanan\t: ")
                if int(pilihan)%1!=0 or int(pilihan)>8 or int(pilihan)<1: #pilihan harus sesuai format
                    print("Masukan angka bulat!!!")
                    print('='*41)
                else:
                    total += int(jumlah)*harga_menu[int(pilihan)]
                    print(f"total\t\t: {total}")
                    print('='*41)
            elif pilihan.lower() == 'sudah': #harus sesuai kondisi
                raise Exception
            else:
                print("Masukan Perintah Yang Benar!!")
                print('='*41)
                pass #melompati kode yang ada
        except Exception:
            break #memberhentikan program

def perhitungan(): #untuk menghitung total pembayaran
    global total
    result = f"total yang perlu dibayarkan {total}" #mencari nilai total
    print('='*41)
    print(f"={result.center(39)}=")
    print('='*41)
    
def main(): #memanggil fungsi yang ada
    global total
    variable()
    title()
    menu()
    count()
    perhitungan()
    
if __name__ == "__main__" : #harus sesuai dengan kondisi
    main()









