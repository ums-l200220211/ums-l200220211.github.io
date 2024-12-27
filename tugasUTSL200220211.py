from metaflow import FlowSpec, step

class InformatikaKuliahFlow(FlowSpec):

    @step
    def start(self):
        """
        Mulai proses alur kuliah informatika.
        """
        print("Memulai proses mengikuti kuliah informatika.")
        self.next(self.bayar_spp)

    @step
    def bayar_spp(self):
        """
        Langkah pertama: Membayar SPP
        """
        self.spp_terbayar = True
        print("SPP berhasil dibayarkan.")
        self.next(self.konfirmasi_spp)

    @step
    def konfirmasi_spp(self):
        """
        Langkah kedua: Konfirmasi pembayaran SPP dan Aktivasi akun mahasiswa
        """
        if self.spp_terbayar:
            self.spp_dikonfirmasi = True
            print("Pembayaran SPP terkonfirmasi. Akun mahasiswa aktif.")
        else:
            self.spp_dikonfirmasi = False
            print("Gagal konfirmasi SPP. Proses berhenti.")
        self.next(self.mengikuti_perkuliahan)

    @step
    def mengikuti_perkuliahan(self):
        """
        Langkah ketiga: Mengikuti perkuliahan.
        """
        if self.spp_dikonfirmasi:
            print("Mahasiswa mengikuti perkuliahan sesuai jadwal.")
            self.perkuliahan_selesai = True
        else:
            print("Tidak dapat mengikuti perkuliahan karena SPP tidak terkonfirmasi.")
            self.perkuliahan_selesai = False
        self.next(self.ujian_akhir)

    @step
    def ujian_akhir(self):
        """
        Langkah keempat: Mengikuti ujian akhir semester.
        """
        if self.perkuliahan_selesai:
            print("Mahasiswa mengikuti ujian akhir semester.")
            self.ujian_selesai = True
        else:
            print("Mahasiswa tidak bisa mengikuti ujian karena tidak menyelesaikan perkuliahan.")
            self.ujian_selesai = False
        self.next(self.pengolahan_nilai)

    @step
    def pengolahan_nilai(self):
        """
        Langkah kelima: Pengolahan nilai ujian.
        """
        if self.ujian_selesai:
            print("Nilai ujian diproses.")
            self.nilai_diproses = True
        else:
            print("Nilai tidak diproses karena mahasiswa tidak mengikuti ujian.")
            self.nilai_diproses = False
        self.next(self.mendapatkan_khs)

    @step
    def mendapatkan_khs(self):
        """
        Langkah terakhir: Mendapatkan Kartu Hasil Studi (KHS)
        """
        if self.nilai_diproses:
            print("Mahasiswa berhasil mendapatkan KHS.")
        else:
            print("Mahasiswa tidak mendapatkan KHS karena nilai tidak diproses.")
        self.next(self.end)

    @step
    def end(self):
        """
        Mengakhiri proses.
        """
        print("Proses mengikuti kuliah informatika selesai.")

if __name__ == '__main__':
    InformatikaKuliahFlow().run()
