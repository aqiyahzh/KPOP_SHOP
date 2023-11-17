from prettytable import PrettyTable
from datetime import datetime
import os

user_data = {
    'Nama': 'Aqiyah Zulqiyah',
    'PIN': '1234',
    'saldo': 10000000,
    'e-pay': 1000000,
    'member': 'Biasa'
}

voucher_data = {
    'kode': 'DISC30',
    'nama_voucher': 'Diskon Akhir Tahun',
    'persentase_diskon': 30,
    'status': 'Aktif'
}

def hapusLayar():
    os.system('cls' if os.name == 'nt' else 'clear')

def cek_epay():
    print("------- C E K  E P A Y -------")
    epay = PrettyTable(["Nama", "Jumlah epay sekarang"])
    epay.add_row([user_data['Nama'], f"Rp. {user_data['e-pay']}"])
    print(epay)

def cek_saldo():
    print("------- C E K  S A L D O -------")
    saldo = PrettyTable(["Nama", "Jumlah saldo sekarang"])
    saldo.add_row([user_data['Nama'], f"Rp. {user_data['saldo']}"])
    print(saldo)

def tukar_saldo_ke_epay():
    print("------- T U K A R  S A L D O  M E N J A D I  E P A Y -------")
    try:
        saldo_tukar = int(input("Masukkan Jumlah Saldo yang Ingin Ditukar ke e-Pay: "))
        if saldo_tukar > 0 and saldo_tukar <= user_data['saldo']:
            # Kurangi saldo dan tambahkan ke e-pay
            user_data['saldo'] -= saldo_tukar
            user_data['e-pay'] += saldo_tukar
            status_table = PrettyTable(["Transaksi","Jumlah saldo yang ditukar","E-pay Sekarang","Saldo Sekarang"])
            status_table.add_row(["Tukar Saldo ke e-Pay", f"Rp. {saldo_tukar}",f"Rp. {user_data['e-pay']}", f"Rp. {user_data['saldo']}"])
            print(status_table)
        else:
            print("Jumlah saldo tidak valid atau melebihi saldo yang tersedia.")
    except ValueError:
        print("Masukkan angka yang valid.")

# Fungsi untuk registrasi member VIP
def registrasi_member_vip():
    if user_data['Nama'] == 'Aqiyah Zulqiyah':
        print("------- ANDA TELAH MASUK MENJADI MEMBER VIP! -------")
        vip()

# Fungsi untuk melakukan pembelian dengan diskon otomatis untuk Member VIP
def vip():
    print('Silahkan pilih barang yang ingin anda beli', user_data['Nama'])

    menu_items = {
        1: {'GG/BG': 'Stray Kids', 'Name': 'T-Shirt Women Korean Streetwear', 'Price': 269000, 'Metode Pembayaran': 'E-pay'},
        2: {'GG/BG': 'Stray Kids', 'Name': 'Oddinary Standing Sign', 'Price': 300000, 'Metode Pembayaran': 'E-pay'},
        3: {'GG/BG': 'ITZY', 'Name': 'Cartoon Keychain', 'Price': 269000, 'Metode Pembayaran': 'Saldo'},
        4: {'GG/BG': 'ITZY', 'Name': 'Poster (Wall Art Painting)', 'Price': 253000, 'Metode Pembayaran': 'Saldo'},
        5: {'GG/BG': 'BTS', 'Name': 'Blanket for Home Sofa', 'Price': 582000, 'Metode Pembayaran': 'Saldo'},
        6: {'GG/BG': 'Blackpink', 'Name': 'Shut Down Keychain', 'Price': 125000, 'Metode Pembayaran': 'Saldo'},
        7: {'GG/BG': 'Blackpink', 'Name': 'Loungefly Heart Mini Backpack', 'Price': 1251000, 'Metode Pembayaran': 'E-pay'},
        8: {'GG/BG': 'ATEEZ', 'Name': 'Baseball T-Shirt', 'Price': 441000, 'Metode Pembayaran': 'Saldo'},
        9: {'GG/BG': 'ATEEZ', 'Name': 'Hip Hop Hoodie', 'Price': 520000, 'Metode Pembayaran': 'E-pay'},
        10: {'GG/BG': 'ATEEZ', 'Name': 'Badge 58mm Brooch', 'Price': 625000, 'Metode Pembayaran': 'E-pay'},
    }

    jualan = PrettyTable(["No", "GG/BG", "Name", "Price", "Metode Pembayaran"])
    for key, item in menu_items.items():
        jualan.add_row([key, item['GG/BG'], item['Name'], f"Rp. {item['Price']}", item['Metode Pembayaran']])
    print(jualan)

    try:
        pilihBarang = int(input("Masukkan Nomor Barang yang Ingin Dibeli: "))
        jumlah = int(input("Masukkan Jumlah: "))
        if pilihBarang not in menu_items:
            print("Barang tidak valid.")
            return
    except ValueError:
        print("Input harus berupa angka.")
        return

    selected_item = menu_items[pilihBarang]
    harga_barang = selected_item['Price'] * jumlah
    metode_pembayaran = selected_item['Metode Pembayaran']
    diskon = 30 / 100

    if metode_pembayaran == 'Saldo':
        potongan_harga = harga_barang * diskon  # 30% discount for saldo
        total_pembayaran = harga_barang - potongan_harga
        user_data['saldo'] -= total_pembayaran
        hapusLayar()
        # Struk Pembayaran
        print("\t\t\tKPOP SHOP")
        print('\t\t   JL. P. ANTASARI GG. 8')
        print('\t\temail: akukentang99@gamil.com')
        print("=" * 50)
        print("=" * 50)
        print(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
        print("Barang yang dipesan          :", {selected_item['Name']})
        print("Jumlah Item                  :", {jumlah})

        total_harga = selected_item['Price'] * jumlah
        setelah_diskon =  selected_item['Price'] - potongan_harga
        print("Total Harga Asli             : Rp.", total_harga)
        print(f"Diskon 30%")
        print("Anda Hemat                   : Rp.", potongan_harga)
        print("Total Harga Setelah Diskon   : Rp.", setelah_diskon)
        print("Saldo saat ini               : Rp.", user_data['saldo'])
        
        print("=" * 50)
        print("Barang yang sudah dibeli tidak dapat dikembalikan")
        print("=" * 50)
    else:
        potongan_harga = harga_barang * diskon  # 30% discount for e-pay
        total_pembayaran = harga_barang - potongan_harga
        user_data['e-pay'] -= total_pembayaran
        hapusLayar()
        # Struk Pembayaran
        print("\t\t\tKPOP SHOP")
        print('\t\t\tJL. P. ANTASARI GG. 8')
        print('\t\temail: akukentang99@gamil.com')
        print("=" * 50)
        print("=" * 50)
        print(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
        print("Barang yang dipesan          :", {selected_item['Name']})
        print("Jumlah Item                  :", {jumlah})

        total_harga = selected_item['Price'] * jumlah
        setelah_diskon =  selected_item['Price'] - potongan_harga
        print("Total Harga Asli             : Rp.", total_harga)
        print(f"Diskon 30%")
        print("Anda Hemat                   : Rp.", potongan_harga)
        print("Total Harga Setelah Diskon   : Rp.", setelah_diskon)
        print("E-pay saat ini               : Rp.", user_data['e-pay'])
        
        print("=" * 50)
        print("Barang yang sudah dibeli tidak dapat dikembalikan")
        print("=" * 50)

# Fungsi untuk melakukan pembelian dengan menggunakan voucher untuk Member Biasa
def gratisan(kode_voucher):
    if kode_voucher == voucher_data['kode'] and voucher_data['status'] == 'Aktif':
        print('Silahkan pilih barang yang ingin anda beli', user_data['Nama'])

        menu_items = {
            1: {'GG/BG': 'Stray Kids', 'Name': 'T-Shirt Women Korean Streetwear', 'Price': 269000, 'Metode Pembayaran': 'E-pay'},
            2: {'GG/BG': 'Stray Kids', 'Name': 'Oddinary Standing Sign', 'Price': 300000, 'Metode Pembayaran': 'E-pay'},
            3: {'GG/BG': 'ITZY', 'Name': 'Cartoon Keychain', 'Price': 269000, 'Metode Pembayaran': 'Saldo'},
            4: {'GG/BG': 'ITZY', 'Name': 'Poster (Wall Art Painting)', 'Price': 253000, 'Metode Pembayaran': 'Saldo'},
            5: {'GG/BG': 'BTS', 'Name': 'Blanket for Home Sofa', 'Price': 582000, 'Metode Pembayaran': 'Saldo'},
            6: {'GG/BG': 'Blackpink', 'Name': 'Shut Down Keychain', 'Price': 125000, 'Metode Pembayaran': 'Saldo'},
            7: {'GG/BG': 'Blackpink', 'Name': 'Loungefly Heart Mini Backpack', 'Price': 1251000, 'Metode Pembayaran': 'E-pay'},
            8: {'GG/BG': 'ATEEZ', 'Name': 'Baseball T-Shirt', 'Price': 441000, 'Metode Pembayaran': 'Saldo'},
            9: {'GG/BG': 'ATEEZ', 'Name': 'Hip Hop Hoodie', 'Price': 520000, 'Metode Pembayaran': 'E-pay'},
            10: {'GG/BG': 'ATEEZ', 'Name': 'Badge 58mm Brooch', 'Price': 625000, 'Metode Pembayaran': 'E-pay'},
        }

        jualan = PrettyTable(["No", "GG/BG", "Name", "Price", "Metode Pembayaran"])
        for key, item in menu_items.items():
            jualan.add_row([key, item['GG/BG'], item['Name'], f"Rp. {item['Price']}", item['Metode Pembayaran']])
        print(jualan)

        try:
            pilihBarang = int(input("Masukkan Nomor Barang yang Ingin Dibeli: "))
            jumlah = int(input("Masukkan Jumlah: "))
            if pilihBarang not in menu_items:
                print("Barang tidak valid.")
                return
        except ValueError:
            print("Input harus berupa angka.")
            return

        selected_item = menu_items[pilihBarang]
        harga_barang = selected_item['Price'] * jumlah
        metode_pembayaran = selected_item['Metode Pembayaran']
        diskon = 30 / 100

        if metode_pembayaran == 'Saldo':
            potongan_harga = harga_barang * diskon  # 30% discount for saldo
            total_pembayaran = harga_barang - potongan_harga
            user_data['saldo'] -= total_pembayaran
            hapusLayar()
            # Struk Pembayaran
            print("\t\t\tKPOP SHOP")
            print('\t\t   JL. P. ANTASARI GG. 8')
            print('\t\temail: akukentang99@gamil.com')
            print("=" * 50)
            print("=" * 50)
            print(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
            print("Barang yang dipesan          :", {selected_item['Name']})
            print("Jumlah Item                  :", {jumlah})

            total_harga = selected_item['Price'] * jumlah
            setelah_diskon =  selected_item['Price'] - potongan_harga
            print("Total Harga Asli             : Rp.", total_harga)
            print(f"Diskon 30%")
            print("Anda Hemat                   : Rp.", potongan_harga)
            print("Total Harga Setelah Diskon   : Rp.", setelah_diskon)
            print("Saldo saat ini               : Rp.", user_data['saldo'])
            
            print("=" * 50)
            print("Barang yang sudah dibeli tidak dapat dikembalikan")
            print("=" * 50)
        else:
            potongan_harga = harga_barang * diskon  # 30% discount for e-pay
            total_pembayaran = harga_barang - potongan_harga
            user_data['e-pay'] -= total_pembayaran
            hapusLayar()
            # Struk Pembayaran
            print("\t\t\tKPOP SHOP")
            print('\t\t\tJL. P. ANTASARI GG. 8')
            print('\t\temail: akukentang99@gamil.com')
            print("=" * 50)
            print("=" * 50)
            print(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
            print("Barang yang dipesan          :", {selected_item['Name']})
            print("Jumlah Item                  :", {jumlah})

            total_harga = selected_item['Price'] * jumlah
            setelah_diskon =  selected_item['Price'] - potongan_harga
            print("Total Harga Asli             : Rp.", total_harga)
            print(f"Diskon 30%")
            print("Anda Hemat                   : Rp.", potongan_harga)
            print("Total Harga Setelah Diskon   : Rp.", setelah_diskon)
            print("E-pay saat ini               : Rp.", user_data['e-pay'])
            
            print("=" * 50)
            print("Barang yang sudah dibeli tidak dapat dikembalikan")
            print("=" * 50)
    else:
        print("Voucher tidak valid atau sudah tidak aktif. Pembelian gagal.")

# program utama
def main():
    print("Silahkan masukkan PIN anda sebelum masuk ke Aplikasi")
    pin_input = input("Masukkan PIN Anda: ")
    if pin_input == user_data['PIN']:
        print("Login berhasil!")

        while True:
            print("\n----- KPOP STUFF STORE ------")
            print("\nSelamat Datang", user_data['Nama'])
            print("\nMenu Utama:")
            print("1. Registrasi Member VIP")
            print("2. Beli Barang")
            print("3. Cek E-pay")
            print("4. Cek Saldo")
            print("5. Tukar Saldo ke epay")
            print("6. Keluar")

            pilihan = input("Pilih menu (1/2/3/4/5/6): ")

            if pilihan == '1':
                registrasi_member_vip()
            elif pilihan == '2':
                kode_voucher = input("Masukkan kode voucher: ")
                gratisan(kode_voucher)
            elif pilihan == '3':
                cek_epay()
            elif pilihan == '4':
                cek_saldo()
            elif pilihan == '5':
                tukar_saldo_ke_epay()
            elif pilihan == '6':
                print("Terima kasih telah berbelanja. Sampai jumpa!")
                break
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")

    else:
        print("PIN salah. Login gagal.")

main()