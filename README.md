# praktikum7
## NAMA  : ANDINURCAHYANA
## NIM   : 312510201
## KELAS : TI.25.C.4

## Tujuan Pemrograman
Tujuan dari program ini adalah mengaplikasikan konsep Object-Oriented Programming (OOP) dalam Python, khususnya konsep Class dan Instance Class, untuk membuat sistem manajemen data nilai mahasiswa sederhana yang meliputi fungsi CRUD (Create, Read, Update, Delete).

## flowchart
<img width="791" height="951" alt="image" src="https://github.com/user-attachments/assets/59c7cc00-28ae-4364-8cc7-0630441c831b" />


## penjelasan flowchart 
1. Inisialisasi Program
Alur dimulai dari simbol START. Langkah pertama yang dieksekusi adalah proses inisialisasi, yaitu membuat Instance Class nilai_mahasiswa = DaftarNilai(). Proses ini memanggil constructor __init__ dari DaftarNilai, yang menyiapkan atribut utama, yaitu list kosong self.data_nilai, tempat semua data mahasiswa akan disimpan.

2. Tampilan Menu Utama
Setelah inisialisasi, program masuk ke bagian MENU UTAMA. Pengguna disajikan pilihan fungsi CRUD (1-Tambah, 2-Tampil, 3-Hapus, 4-Ubah, 5-Keluar) dan diminta untuk memasukkan pilihan. Input ini kemudian akan masuk ke blok keputusan (Belah Ketupat) untuk menentukan aksi selanjutnya.

3. Eksekusi Fungsi (Decision Points)
Tergantung pada pilihan pengguna, alur program akan bercabang ke salah satu method yang diimplementasikan dalam class DaftarNilai:

Pilihan 1: Tambah Data (Create)
Jika pengguna memilih 1, program akan memanggil method tambah().

Method ini meminta input berupa nama dan nilai mahasiswa.

Setelah validasi dan penyimpanan berhasil ke dalam list self.data_nilai, program menampilkan konfirmasi "data telah disimpan".

Alur kemudian diarahkan untuk Kembali ke Menu Utama.

Pilihan 2: Tampilkan Data (Read)
Jika pengguna memilih 2, program memanggil method tampilkan().

Method ini bertugas untuk menampilkan semua data yang ada di dalam list self.data_nilai.

Output yang dihasilkan adalah "data ditampilkan" dalam format tabel.

Alur kemudian diarahkan untuk Kembali ke Menu Utama.

Pilihan 3: Hapus Data (Delete)
Jika pengguna memilih 3, program memanggil method hapus().

Pengguna diminta untuk memilih nama yang akan dihapus.

Method ini mencari dan menghapus data yang sesuai.

Setelah berhasil, program menampilkan konfirmasi "data dihapus".

Alur kemudian diarahkan untuk Kembali ke Menu Utama.

Pilihan 4: Ubah Data (Update)
Jika pengguna memilih 4, program memanggil method ubah().

Pengguna diminta untuk pilih nama yang akan diubah nilainya.

Setelah nama ditemukan, pengguna diminta memasukkan nilai baru.

Setelah pembaruan selesai, program menampilkan konfirmasi "data diubah".

Alur kemudian diarahkan untuk Kembali ke Menu Utama.

4. Mengakhiri Program (Keluar)
Jika pengguna memilih 5, program akan masuk ke proses pengecekan "apakah data selesai?".

Jika pengguna memilih "ya", program menampilkan pesan penutup dan alur berakhir pada simbol END.

Jika pengguna memilih "tidak", artinya pengguna ingin membatalkan keluar dan melanjutkan operasi, sehingga alur kembali diarahkan untuk Kembali ke Menu Utama.

## pemerograman python (praktikum7.py)
```py
# praktikum7.py

class DaftarNilai:
    
    def __init__(self):
        
        self.data_nilai = []

    def tambah(self):
        
        print("\n--- Tambah Data Mahasiswa ---")
        
        while True:
            nama = input("Masukkan Nama: ").strip()
            nilai_str = input("Masukkan Nilai: ").strip()
            
            if not nama:
                print("Nama tidak boleh kosong.")
                continue
            try:
                nilai = float(nilai_str)
                
                data_baru = {"nama": nama, "nilai": nilai}
                self.data_nilai.append(data_baru)
                print(f"Data '{nama}' berhasil ditambahkan.")
                break
            except ValueError:
                print("Nilai harus berupa angka.")
                
    
    def tampilkan(self):
        
        print("\n--- Daftar Nilai Mahasiswa ---")
        
        if not self.data_nilai:
            print("Daftar nilai kosong.")
            return

        print("{:<5} {:<20} {:>10}".format("No.", "Nama", "Nilai"))
        print("-" * 35)
        
        for i, data in enumerate(self.data_nilai, 1):
            print("{:<5} {:<20} {:>10.2f}".format(i, data["nama"], data["nilai"]))
        print("-" * 35)

    def hapus(self, nama):
    
        data_sebelum = len(self.data_nilai)
        
        self.data_nilai = [data for data in self.data_nilai if data["nama"].lower() != nama.lower()]
        
        data_sesudah = len(self.data_nilai)
        
        print("\n--- Hapus Data Mahasiswa ---")
        if data_sebelum > data_sesudah:
            print(f"Data dengan nama '{nama}' berhasil dihapus.")
        else:
            print(f"Data dengan nama '{nama}' tidak ditemukan.")

    def ubah(self, nama):
        
        print("\n--- Ubah Data Mahasiswa ---")
        ditemukan = False

        for data in self.data_nilai:
            if data["nama"].lower() == nama.lower():
                ditemukan = True
                while True:
                    try:
                        nilai_baru = float(input(f"Masukkan Nilai Baru untuk '{data['nama']}': ").strip())
                        
                        data["nilai"] = nilai_baru
                        print(f"Nilai '{data['nama']}' berhasil diubah menjadi {nilai_baru:.2f}.")
                        break
                    except ValueError:
                        print("Nilai harus berupa angka.")
                break 

        if not ditemukan:
            print(f"Data dengan nama '{nama}' tidak ditemukan.")

if __name__ == "__main__":
    
    nilai_mahasiswa = DaftarNilai()
    
    while True:
        print("\n\n=== Menu Aplikasi Manajemen Nilai ===")
        print("1. Tambah Data")
        print("2. Tampilkan Data")
        print("3. Hapus Data (Berdasarkan Nama)")
        print("4. Ubah Data (Berdasarkan Nama)")
        print("5. Keluar")
        
        pilihan = input("Masukkan Pilihan (1-5): ")
        
        if pilihan == '1':
            nilai_mahasiswa.tambah()
        elif pilihan == '2':
            nilai_mahasiswa.tampilkan()
        elif pilihan == '3':
            nama_hapus = input("Masukkan Nama Mahasiswa yang akan dihapus: ").strip()
            if nama_hapus:
                nilai_mahasiswa.hapus(nama_hapus)
            else:
                print("Nama tidak boleh kosong.")
        elif pilihan == '4':
            nama_ubah = input("Masukkan Nama Mahasiswa yang nilainya akan diubah: ").strip()
            if nama_ubah:
                nilai_mahasiswa.ubah(nama_ubah)
            else:
                print("Nama tidak boleh kosong.")
        elif pilihan == '5':
            print("Terima kasih, program dihentikan.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
```

## penjelasan pemerograman (praktikum7.py)
- Konsep OOP yang Digunakan

    1. Class dan Instance Class: Program ini menggunakan Class DaftarNilai , yang berfungsi sebagai blueprint (cetak biru) untuk membuat objek (instance class)  manajemen data. Di program utama, nilai_mahasiswa = DaftarNilai() adalah proses pembuatan instance class.

    2. Atribut dan Method:
        - Atribut (Deklarasi Variabel): Class DaftarNilai memiliki atribut publik self.data_nilai yang diinisialisasi di dalam constructor __init__. Atribut ini adalah list yang digunakan untuk menyimpan data mahasiswa.

        - Method (Fungsi): Class ini memiliki method publik tambah(), tampilkan(), hapus(nama), dan ubah(nama) , yang merupakan behavior (perilaku)  dari objek. Method ini dapat diakses di luar class, contohnya nilai_mahasiswa.tambah().


- Struktur Data
Data mahasiswa disimpan dalam format List of Dictionaries (self.data_nilai). Setiap elemen dalam list adalah sebuah dictionary yang merepresentasikan satu mahasiswa dengan key nama dan nilai.

- Fungsi Method

    - __init__(self): Constructor yang dieksekusi saat objek dibuat, menginisialisasi list self.data_nilai menjadi kosong.

    - tambah(): Menerima input nama dan nilai, memvalidasi nilai harus berupa angka, lalu menambahkan data ke self.data_nilai.

    - tampilkan(): Menampilkan seluruh data dalam format tabel yang rapi.

    - hapus(nama): Mencari data berdasarkan nama (tidak case-sensitive) dan menghapusnya menggunakan list comprehension.

    - ubah(nama): Mencari data berdasarkan nama (tidak case-sensitive) dan meminta input nilai baru untuk diperbarui.

## output
<img width="932" height="508" alt="output7 1" src="https://github.com/user-attachments/assets/9d1353fb-7e18-443f-8305-7b22fe1e0f76" />
<img width="927" height="649" alt="output7 2" src="https://github.com/user-attachments/assets/6366193b-b379-4bef-8f5e-75482f4d7edf" />
<img width="925" height="748" alt="output7 3" src="https://github.com/user-attachments/assets/189e1ece-a7ed-4037-90e3-003ca1e2f745" />
<img width="926" height="508" alt="output7 4" src="https://github.com/user-attachments/assets/700d5f75-743d-4741-98c9-04dad5484195" />
