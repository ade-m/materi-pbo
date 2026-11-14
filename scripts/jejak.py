# Each scenario has explicit teaching snapshots: (code line, phase, program state).
# The final outcome is authored in kurikulum.py and revealed after prediction.
T={
'01':[
 [(1,'Kompilasi','Sumber: Hello.java → bytecode Hello.class'),(2,'Muat kelas','JVM mencari Hello.class dan memanggil main.')],
 [(1,'Kompilasi','Hello.class tersedia.'),(2,'Cari kelas','Nama yang diminta: Halo. Hanya Hello.class yang disiapkan.')]],
'02':[
 [(1,'Baca operand','Kiri: 7 (int) · kanan: 2 (int)'),(1,'Hitung pembagian','Bagian pecahan dibuang saat pembagian int.')],
 [(1,'Casting','7 (int) berubah menjadi 7.0 (double).'),(1,'Promosi operand','2 dipromosikan menjadi 2.0 untuk pembagian double.')],
 [(1,'Inisialisasi','i = 1; i ≤ 4 benar.'),(3,'Cetak iterasi pertama','i = 1; keluaran sementara: 1'),(2,'Lewati iterasi kedua','i = 2; continue menuju pembaruan i.'),(3,'Cetak iterasi ketiga','i = 3; keluaran sementara: 13'),(3,'Cetak iterasi keempat','i = 4; kondisi berikutnya akan gagal pada i = 5.')]],
'03':[
 [(1,'Buat array','Indeks 0: Medan · indeks 1: Binjai · length = 2'),(2,'Ambil indeks','Indeks yang diminta: 1. Akses masih di dalam batas.')],
 [(1,'Buat daftar','[Medan, Binjai] · size = 2'),(2,'Hapus indeks 0','Medan dihapus; Binjai bergeser ke indeks 0.'),(3,'Ambil indeks 0','size = 1; baca elemen yang bergeser.')],
 [(1,'Buat daftar','[Medan, Binjai] · size = 2'),(2,'Ganti elemen','Indeks 1 menerima Berastagi. Ukuran tetap 2.'),(3,'Cetak daftar','println meminta representasi daftar saat ini.')]],
'04':[
 [(2,'Inisialisasi kelas','Produk.jumlah = 0; field dibagi oleh semua objek.'),(6,'Buat objek pertama','Constructor baris 3 menambah Produk.jumlah menjadi 1.'),(7,'Buat objek kedua','Constructor kembali menambah field kelas yang sama.'),(8,'Baca field kelas','Nilai dibaca dari Produk, tanpa referensi objek.')],
 [(2,'Siapkan field instans','Setiap objek Produk memiliki field harga sendiri.'),(3,'Jalankan constructor','Parameter harga = 15000; this.harga menunjuk field objek.'),(4,'Panggil getter','getHarga membaca harga dari objek baru pada baris 7.')]],
'05':[
 [(1,'Identifikasi pengguna','Laporan bertanggung jawab atas operasi cetak.'),(2,'Periksa pemakaian','Printer diterima sebagai parameter dan tidak disimpan.')],
 [(1,'Identifikasi pemilik tautan','Mahasiswa punya keadaan yang disimpan pada objek.'),(2,'Periksa field','Daftar MataKuliah dipertahankan dalam field mataKuliah.')]],
'06':[
 [(1,'Lepas bagian','Tautan Tim A–Anggota dihapus.'),(2,'Cek keberadaan','Anggota tetap terdaftar.'),(3,'Pindahkan bagian','Anggota yang sama dapat terhubung ke Tim B.')],
 [(1,'Tentukan pemilik','BarisPesanan hanya menjadi bagian dari satu pesanan.'),(2,'Hapus keseluruhan','Model menghapus pesanan beserta baris yang masih dimilikinya.')]],
'07':[
 [(1,'Baca tipe induk','Mobil menjadi superclass.'),(2,'Baca deklarasi turunan','Sedan memakai extends Mobil.'),(4,'Cek penugasan','Objek Sedan diberikan ke referensi bertipe Mobil.')],
 [(1,'Baca kontrak','Penggerak meminta operasi on().'),(2,'Cek deklarasi','Mesin memakai implements Penggerak.'),(3,'Cek operasi','on() public memenuhi tanda tangan yang diminta.')]],
'09':[
 [(1,'Buat referensi','Tipe referensi: Enemy · objek aktual: Burung'),(2,'Pilih implementasi','attack tersedia pada Enemy; dispatch mengikuti objek Burung.')],
 [(1,'Buat referensi','Tipe referensi: Enemy · objek aktual: Zombie'),(2,'Pilih implementasi','attack tersedia pada Enemy; dispatch mengikuti objek Zombie.')],
 [(1,'Periksa tipe statis','e dideklarasikan sebagai Enemy.'),(2,'Periksa anggota','Compiler mencari fly() pada kontrak Enemy sebelum runtime.')]],
'10':[
 [(1,'Buat List','[]'),(2,'Tambahkan Ravi','[Ravi]'),(2,'Tambahkan Vijay','[Ravi, Vijay]'),(2,'Tambahkan Ravi lagi','List menerima nama yang sama.'),(3,'Cetak isi','Urutan penyisipan dipertahankan.')],
 [(1,'Buat LinkedHashSet','[]'),(2,'Tambahkan Vijay dan Ravi','[Vijay, Ravi]'),(2,'Tambahkan Vijay lagi','Set memeriksa elemen yang sama sebelum menyimpan.'),(3,'Cetak isi','LinkedHashSet mempertahankan urutan penyisipan.')],
 [(1,'Buat Deque','Tumpukan kosong.'),(2,'Push A','Puncak: A'),(2,'Push B','Puncak: B · di bawahnya: A'),(3,'Pop','Ambil dan hapus elemen di puncak.')]],
'11':[
 [(1,'Ikat tipe','Untuk b, T = String.'),(2,'Periksa set','Argumen “Kopi” bertipe String.'),(3,'Ambil nilai','get() menghasilkan String tanpa cast manual.')],
 [(1,'Ikat tipe','Untuk b, T = String.'),(2,'Periksa argumen','set membutuhkan String, tetapi 42 bukan String.')],
 [(1,'Ikat tipe','Untuk b, T = Integer.'),(2,'Boxing','42 (int) di-box menjadi Integer.'),(3,'Unboxing','Nilai Integer dari get() dapat di-unbox ke int.')]],
'11-bonus':[
 [(1,'Buat objek luar','o adalah instans Outer.'),(2,'Buat objek inner','Ekspresi o.new Inner() mengikat i ke o.')],
 [(1,'Periksa jenis kelas','Nested adalah member class static.'),(1,'Periksa constructor','Pemanggilan tidak membutuhkan instans Outer.')],
 [(1,'Periksa jenis kelas','Inner adalah member class non-static.'),(1,'Periksa konteks','Contoh dijalankan di luar Outer; tidak ada instans luar yang diberikan.')]],
'13':[
 [(1,'Deklarasikan kelas anonim','r berkontrak Runnable.'),(2,'Isi implementasi','run() berisi perintah cetak, tetapi belum dipanggil.'),(4,'Panggil run','Method berjalan pada thread pemanggil.')],
 [(1,'Buat objek anonim','Tipe referensi: Object.'),(2,'Tentukan override','Objek menyediakan toString() sendiri.'),(4,'Cetak objek','println menggunakan representasi dari toString().')]],
'13-bonus':[
 [(1,'Baca nama package','Nama lengkap kelas: id.ac.kampus.App.'),(2,'Kompilasi','Opsi -d out menentukan direktori keluaran.'),(3,'Cari bytecode','Classpath dimulai dari out, bukan folder package.')],
 [(1,'Resolusi saat kompilasi','javac mencari tipe dependensi di lib/*.'),(2,'Resolusi saat runtime','JVM mencari kelas aplikasi di out dan dependensi di lib/*.')]],
'14':[
 [(1,'Baca penyebut','d = 2'),(2,'Jalankan try','Pembagian berhasil; keluaran sementara: 5'),(3,'Lewati catch','Tidak ada ArithmeticException.'),(4,'Jalankan finally','Eksekusi mencapai perintah cetak terakhir.')],
 [(1,'Baca penyebut','d = 0'),(2,'Jalankan try','ArithmeticException terjadi sebelum println mencetak hasil pembagian.'),(3,'Masuk catch','Handler cocok; keluaran sementara: Penyebut nol'),(4,'Jalankan finally','Eksekusi mencapai perintah cetak terakhir.')],
 [(1,'Baca teks','Input: “dua”.'),(1,'Periksa representasi','Tidak ada digit yang dapat diparse menjadi bilangan bulat.')]],
'14-alt':[
 [(1,'Tentukan path','Target: catatan.txt'),(2,'Tulis teks','Isi baru: Halo, dalam UTF-8.'),(3,'Baca ulang','Pembacaan mengembalikan isi file yang baru ditulis.')],
 [(1,'Baca keadaan awal','Isi awal: Halo'),(2,'Bentuk data tambahan','Data: baris baru diikuti Java.'),(3,'Terapkan APPEND','Posisi tulis berada setelah isi lama.'),(4,'Baca kembali','Pembacaan dimulai dari awal file.')],
 [(1,'Buka stream','Tersedia satu byte bernilai 65.'),(2,'Baca pertama','Byte dikonsumsi; posisi kini di akhir stream.'),(3,'Baca lagi','Tidak ada byte tersisa; periksa penanda akhir.')]],
}
