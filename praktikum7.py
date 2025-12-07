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