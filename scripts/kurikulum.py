# Data pembelajaran. Format: konsep (judul, penjelasan), simulasi (pilihan, kode, hasil, alasan),
# kuis (soal, jawaban benar, dua distraktor, pembahasan).
M=[]
def m(slug, no, title, source, pages, intro, concepts, cases, quiz, task, ref=8):
 M.append(dict(slug=slug,no=no,title=title,source=source,pages=pages,intro=intro,concepts=concepts,cases=cases,quiz=quiz,task=task,ref=ref))
m('01','1','Pengantar PBO dan Java','1','2–3, 5–30','Dari masalah sehari-hari ke rancangan kelas dan program Java pertama.',[
('Mulai dari kebutuhan','Kenali pengguna, tujuan, dan batasan. Susun langkah penyelesaian, tulis kode, uji, debug, lalu pelihara. Untuk petunjuk perjalanan, tentukan titik awal, tujuan, dan kondisi jalan sebelum memilih rute.'),
('Prosedur dan objek','Pendekatan prosedural mengelompokkan langkah dalam fungsi. PBO mengelompokkan data dan perilaku di objek. Program Java dapat memadukan keduanya.'),
('Kelas dan instans','Kelas adalah rancangan. Dua objek dari kelas Rekening dapat memiliki saldo berbeda. Enkapsulasi menjaga aturan saldo, abstraksi menyaring detail, pewarisan menyatakan subtipe, dan polimorfisme memungkinkan perilaku berbeda lewat kontrak yang sama.'),
('Dari sumber ke eksekusi','JDK menyediakan alat seperti javac. Kompilasi Hello.java menghasilkan bytecode Hello.class; JVM mengeksekusinya. IDE membantu mengedit dan menjalankan kode, tetapi tidak wajib.'),
('Java SE dan aplikasi enterprise','Java SE menyediakan fondasi bahasa dan pustaka. Materi sumber juga memperkenalkan JEE, kini Jakarta EE, untuk aplikasi enterprise. Pada sistem bertingkat, peramban mengakses layanan aplikasi; layanan berinteraksi dengan basis data. Cluster dapat membantu kapasitas dan ketersediaan.')],[
('Jalankan kelas Hello','javac Hello.java\njava Hello','Halo, Java!','Contoh mengasumsikan Hello.java berisi kelas Hello dengan main yang mencetak pesan tersebut.'),
('Nama kelas salah','javac Hello.java\njava Halo','Kelas Halo tidak ditemukan','Perintah java mencari kelas yang diminta, bukan nama bebas.')],[
('Apa hasil umum javac Hello.java?','Hello.class','Hello.exe','Halo.java','javac mengompilasi sumber menjadi bytecode.'),
('Apa contoh objek?','Rekening milik Dina dengan saldo 50000','Deklarasi class Rekening','Keyword private','Objek adalah instans konkret yang punya keadaan.')],
'Buat Hello.java, kompilasi dengan javac, dan jalankan dari terminal. Jelaskan peran JDK, JVM, dan IDE. Ketentuan pengumpulan mengikuti instruksi kelas yang berlaku.',12)
m('02','2','Elemen dasar Java','2','3–56','Baca struktur program, prediksi hasil ekspresi, dan telusuri alur kendali.',[
('Struktur dan tipe','Deklarasi package dan import mendahului class. main adalah titik masuk contoh terminal. Java memiliki delapan tipe primitif: byte, short, int, long, float, double, char, boolean; String adalah tipe referensi. Field mendapat nilai default, tetapi variabel lokal harus diinisialisasi sebelum dibaca.'),
('Modifier dan konvensi','Gunakan PascalCase untuk kelas, camelCase untuk method/variabel, dan huruf kecil untuk package. private membatasi akses, tanpa modifier berarti satu package, protected juga menyediakan akses tertentu untuk subclass lintas package, public paling terbuka. static milik kelas; final mencegah penugasan ulang.'),
('Ekspresi dan konversi','Urutan operator menentukan hasil; gunakan kurung agar jelas. Pembagian int memotong ke arah nol. Casting double ke int tidak membulatkan; Math.round membulatkan. Konversi pelebaran ke float dapat kehilangan presisi.'),
('String dan masukan','Gunakan equals untuk membandingkan isi String. substring(a,b) mencakup a dan tidak mencakup b. Scanner membaca System.in; argumen CLI tersedia lewat args. Integer.parseInt mengubah teks ke int dan dapat gagal. Gunakan escape seperti \\n, \\t dan \\".'),
('Kendali alur','if dan switch memilih cabang. for cocok saat jumlah iterasi jelas; while memeriksa kondisi di awal, do-while di akhir. break keluar dari loop, continue melewati sisa iterasi, return keluar dari method. Label dapat menargetkan loop luar.')],[
('Pembagian int','System.out.println(7 / 2);','3','Kedua operand bertipe int.'),
('Pembagian double','System.out.println((double) 7 / 2);','3.5','Casting dilakukan sebelum pembagian.'),
('Lewati iterasi','for (int i = 1; i <= 4; i++) {\n  if (i == 2) continue;\n  System.out.print(i);\n}','134','continue melewatkan pencetakan angka 2.')],[
('Bagaimana membandingkan isi String a dan b?','a.equals(b) jika a tidak null','a == b','a = b','equals membandingkan isi String; == membandingkan referensi.'),
('Berapa kali do-while berjalan jika kondisi pertama false?','Satu kali','Nol kali','Tidak terbatas','Kondisi diperiksa setelah badan loop.')],
'Baca dua bilangan dengan Scanner, tampilkan hasil pembagian pecahan, dan tangani penyebut nol sebelum membagi.',15)
m('03','3','Dekomposisi, array, dan ArrayList','3','2–22','Pilih struktur data berdasarkan kebutuhan, lalu amati perubahan indeks dan ukuran.',[
('Dekomposisi','Pisahkan program menjadi tanggung jawab kecil. Dalam contoh koordinat, kelas Lokasi menyimpan x dan y; kelas App menangani interaksi. Dekomposisi prosedural memecah langkah; dekomposisi objek memecah tanggung jawab.'),
('Tipe data abstrak','ADT menjelaskan operasi dan perilaku yang terlihat, tanpa mengharuskan pengguna mengetahui penyimpanan internal. Antarmuka List, misalnya, menyatakan operasi koleksi berurutan.'),
('Array','Array mempunyai panjang tetap setelah dibuat, indeks mulai nol, dan properti length. new int[3] membuat tiga elemen bernilai nol; akses indeks 3 berada di luar batas.'),
('ArrayList','ArrayList dapat bertambah atau berkurang. add menambah, get membaca, set mengganti, remove menghapus, dan size() menghitung elemen. Menyisipkan atau menghapus dapat menggeser indeks. Gunakan Integer untuk menyimpan bilangan bulat sebagai tipe generik.')],[
('Akses array','String[] kota = {"Medan", "Binjai"};\nSystem.out.println(kota[1]);','Binjai','Indeks 1 adalah elemen kedua.'),
('Hapus dari daftar','List<String> kota = new ArrayList<>(List.of("Medan", "Binjai"));\nkota.remove(0);\nSystem.out.println(kota.get(0));','Binjai','Elemen berikutnya bergeser ke indeks 0.'),
('Ganti elemen','List<String> kota = new ArrayList<>(List.of("Medan", "Binjai"));\nkota.set(1, "Berastagi");\nSystem.out.println(kota);','[Medan, Berastagi]','set mengganti nilai tanpa mengubah ukuran.')],[
('Apa yang terjadi setelah remove(0) pada daftar dua elemen?','Elemen kedua bergeser ke indeks 0','Ukuran tetap dua','ArrayList berubah menjadi array','Elemen sesudah posisi penghapusan bergeser.'),
('Apa cara membaca panjang array a?','a.length','a.size()','a.length()','Array memakai field length.')],
'Buat daftar tiga kota, sisipkan kota baru di indeks 1, lalu hapus kota pertama. Catat hasil tiap langkah.',10)
m('04','4','Merancang dan mengimplementasikan kelas','4','2–22','Rancang kelas dengan keadaan, aturan validasi, dan tanggung jawab yang jelas.',[
('Identifikasi kelas','Ambil konsep umum dari kasus, misalnya Produk, bukan satu produk tertentu. Tentukan atribut, operasi, dan relasi. Tampilan aplikasi tidak menentukan batas kelas dengan sendirinya.'),
('Enkapsulasi','Field private membatasi perubahan langsung. Method publik menetapkan aturan, misalnya tolak harga negatif. Getter dan setter tidak wajib untuk semua field.'),
('Nama file dan static','Kelas top-level public Produk ditempatkan pada Produk.java. Field static dibagi semua instans; field biasa terpisah per objek. Method static tidak memiliki this dan tidak bisa mengakses field instans tanpa objek.'),
('Constructor dan this','Constructor menginisialisasi objek dan tidak punya tipe kembalian. this.harga = harga membedakan field dan parameter. this(...) memanggil constructor lain; pada Java 21 pemanggilan ini harus menjadi pernyataan pertama.'),
('Relasi has-a dan dokumentasi','Field bertipe objek lain dapat mewakili relasi has-a. Contoh: Keranjang memiliki daftar Produk. Dokumentasikan kontrak method, parameter, hasil, dan kondisi gagal dengan Javadoc.')],[
('Dua objek, satu penghitung','class Produk {\n  static int jumlah;\n  Produk() { jumlah++; }\n}\n// Di dalam main:\nnew Produk();\nnew Produk();\nSystem.out.println(Produk.jumlah);','2','jumlah milik kelas sehingga kedua constructor mengubah penghitung yang sama.'),
('Field dan parameter','class Produk {\n  private int harga;\n  Produk(int harga) { this.harga = harga; }\n  int getHarga() { return harga; }\n}\n// Di dalam main:\nSystem.out.println(new Produk(15000).getHarga());','15000','this.harga adalah field objek, sedangkan harga adalah parameter.')],[
('Apa tujuan private pada harga?','Membatasi perubahan langsung dari luar kelas','Membuat harga milik semua objek','Menghapus kebutuhan constructor','Perubahan dapat disalurkan lewat operasi yang memvalidasi.'),
('Apa deklarasi constructor Produk yang valid?','Produk(int harga) { }','void Produk(int harga) { }','int Produk() { return 0; }','Constructor bernama sama dengan kelas dan tanpa tipe kembalian.')],
'Rancang Produk dengan nama dan harga, tolak harga negatif dalam constructor, dan dokumentasikan method yang membaca harga.')
m('05','5','Diagram kelas, dependency, dan asosiasi','5-7','2–10, 20–25','Bedakan hubungan penggunaan sementara dan hubungan struktural antarkelas.',[
('Membaca kotak kelas','Diagram kelas UML memodelkan struktur. Kotak kelas dapat memuat nama, atribut, dan operasi. + berarti public, − private, # protected. Contoh: −status: int dan +start(): void.'),
('Dependency','Jika satu kelas menggunakan kelas lain, misalnya hanya sebagai parameter atau objek sementara, gambarkan dependency sebagai panah putus-putus dari pengguna ke penyedia.'),
('Asosiasi','Asosiasi menggambarkan hubungan struktural. Garis utuh dapat diberi nama peran dan multiplicity. Contoh: Mahasiswa terkait banyak MataKuliah dan keduanya tetap dapat ada sendiri.'),
('Studi kasus inventaris','Pisahkan Gitar yang didata dari Inventaris yang menyimpan koleksi gitar. Pencarian dapat menerima spesifikasi sebagai parameter. Tandai peran dan jumlah objek di tiap ujung relasi.')],[
('Parameter sementara','class Laporan {\n  void cetak(Printer alat) { alat.cetak(); }\n}','Laporan - - > Printer\nDependency','Printer dipakai untuk pekerjaan ini; tidak disimpan oleh Laporan.'),
('Hubungan yang disimpan','class Mahasiswa {\n  List<MataKuliah> mataKuliah = new ArrayList<>();\n}','Mahasiswa ─── MataKuliah\nAsosiasi','Field koleksi mewakili tautan yang bertahan selama keadaan objek.')],[
('Apa arti 0..* di ujung relasi?','Nol atau lebih objek pada ujung tersebut','Tepat satu objek','Semua atribut private','Multiplicity menunjukkan jumlah instans yang dapat terhubung.'),
('Dependency ditunjukkan dengan?','Panah putus-putus ke penyedia','Berlian isi di sisi bagian','Segitiga kosong ke kelas anak','Panah menunjuk elemen yang dibutuhkan.')],
'Gambar hubungan Inventaris, Gitar, dan SpesifikasiGitar. Tentukan dependency, asosiasi, dan multiplicity yang diperlukan.','uml')
m('06','6','Agregasi dan komposisi','5-7','11–15, 20–25','Gunakan aturan kepemilikan dan daur hidup untuk memilih relasi bagian–keseluruhan.',[
('Agregasi','Agregasi bersama merupakan asosiasi dengan berlian kosong di sisi keseluruhan. Dalam model sederhana, bagian dapat dipertahankan atau dipindahkan terlepas dari keseluruhan.'),
('Komposisi','Komposisi memiliki berlian terisi di sisi keseluruhan. Bagian menjadi milik paling banyak satu komposit pada suatu saat; jika komposit dihapus, bagian yang masih dimilikinya ikut dihapus dalam model.'),
('Kode bukan satu-satunya bukti','Field List<Bagian> saja tidak menentukan notasi. Periksa aturan bisnis: siapa membuat, menyimpan, memindahkan, dan menghapus bagian. Garbage collector Java berbeda dari aturan daur hidup domain.'),
('Uji desain inventaris','Jika gitar tetap ada walau cabang inventaris ditutup, jangan modelkan gitar sebagai bagian yang harus ikut terhapus. Detail baris pesanan yang tidak berdiri sendiri dapat dimodelkan sebagai komposisi.')],[
('Bagian dapat berpindah','// Tim A melepas anggota.\n// Anggota tetap terdaftar di sistem.\n// Tim B dapat menerimanya.','Tim ◇── Anggota\nAgregasi','Daur hidup Anggota tidak terikat pada Tim.'),
('Bagian terikat pesanan','// Baris hanya bermakna di dalam pesanan.\n// Saat pesanan dihapus, barisnya ikut dihapus.','Pesanan ◆── BarisPesanan\nKomposisi','Model menyatakan kepemilikan komposit dan penghapusan bagian yang masih dimiliki.')],[
('Di mana posisi berlian komposisi?','Di sisi keseluruhan','Di sisi bagian','Di kedua ujung','Berlian menempel pada kelas komposit.'),
('Apa yang paling membantu memilih komposisi?','Aturan kepemilikan dan daur hidup','Ada keyword new','Field bertipe List','Struktur kode serupa dapat mewakili aturan yang berbeda.')],
'Bandingkan Mobil–Mesin untuk kendaraan rakitan dan toko suku cadang. Jelaskan bagaimana aturan domain mengubah pilihan relasi.','uml')
m('07','7','Pewarisan dan realisasi interface','5-7','16–25','Bedakan relasi is-a dan pemenuhan kontrak interface.',[
('Generalisasi kelas','Sedan is-a Mobil hanya jika Sedan dapat dipakai di tempat Mobil tanpa melanggar kontraknya. Di Java gunakan extends untuk satu superclass langsung.'),
('Akses dan pewarisan','Subclass dapat menambahkan dan override method instans yang dapat dioverride. Constructor tidak diwariskan. Gunakan super(...) untuk inisialisasi superclass dan akses anggota melalui kontrak yang tersedia.'),
('Realisasi interface','Gunakan implements ketika kelas memenuhi kontrak interface, misalnya Mesin implements Penggerak. Kelas konkret menyediakan implementasi untuk method abstrak yang masih belum dipenuhi.'),
('Notasi UML','Generalisasi memakai garis utuh dan segitiga kosong ke induk. Realisasi memakai garis putus-putus dan segitiga kosong ke interface. Keduanya berbeda dari berlian has-a.')],[
('Turunan kelas','class Mobil {}\nclass Sedan extends Mobil {}\n// Di dalam main:\nMobil kendaraan = new Sedan();','Sedan ──▷ Mobil\nGeneralisasi','Sedan adalah subtipe Mobil.'),
('Kontrak interface','interface Penggerak { void on(); }\nclass Mesin implements Penggerak {\n  public void on() { System.out.println("Menyala"); }\n}','Mesin - -▷ Penggerak\nRealisasi','Mesin menyediakan method public sesuai kontrak.')],[
('Keyword apa untuk kelas yang memenuhi interface?','implements','extends','import','Kelas memakai implements; interface bisa extends interface lain.'),
('Apakah constructor induk diwariskan?','Tidak; subclass dapat memanggilnya lewat super','Ya; semua constructor menjadi constructor anak','Hanya jika private','Constructor bukan anggota yang diwariskan.')],
'Tambahkan interface BisaDimainkan pada rancangan inventaris gitar. Bedakan generalisasi GitarElektrik–Gitar dan realisasi BisaDimainkan.','uml')
m('09','9','Polimorfisme, kelas abstrak, dan interface','9','2–17','Prediksi method yang dipanggil dari tipe referensi dan tipe objek saat runtime.',[
('Satu kontrak, banyak perilaku','Referensi Enemy dapat menunjuk Burung, Pocong, atau Zombie. Pemanggilan method instans yang dioverride memilih implementasi berdasarkan objek runtime.'),
('Overload dan override','Overload memakai nama sama dengan parameter berbeda, dipilih saat kompilasi. Override mengganti perilaku method instans pada subtipe. Tipe referensi menentukan anggota yang boleh dipanggil.'),
('Kelas abstrak','Kelas abstract tidak bisa dibuat langsung dengan new. Ia dapat memiliki field, constructor, method konkret, dan nol atau lebih method abstrak. Subclass konkret memenuhi method abstrak yang tersisa.'),
('Interface modern','Interface memodelkan kontrak, bisa memiliki method abstrak, default dan static; Java juga mendukung helper private di interface. Satu kelas dapat mengimplementasikan beberapa interface.')],[
('Objek Burung','Enemy e = new Burung();\ne.attack();','Burung menyerang dari udara','Override Burung dipilih saat runtime.'),
('Objek Zombie','Enemy e = new Zombie();\ne.attack();','Zombie menyerang dari tanah','Kontrak yang sama, implementasi berbeda.'),
('Panggil kemampuan khusus','Enemy e = new Burung();\ne.fly(); // fly tidak ada pada Enemy','Galat kompilasi','Tipe referensi Enemy tidak mendeklarasikan fly, walau objek aktual Burung bisa terbang.')],[
('Bolehkah kelas abstrak tidak memiliki method abstrak?','Boleh','Tidak pernah','Hanya jika final','Modifier abstract pada kelas tidak mensyaratkan method abstrak.'),
('Apa yang menentukan override saat runtime?','Tipe objek aktual','Nama variabel','Urutan import','Dispatch method instans mengikuti tipe objek runtime.')],
'Buat abstract class Enemy dengan attack(). Tambahkan Burung dan Zombie, simpan keduanya dalam Enemy[], lalu panggil attack dalam loop.')
m('10','10','Java Collections dan iterator','10','2–14','Pilih koleksi berdasarkan urutan, duplikasi, dan pola akses yang dibutuhkan.',[
('Kontrak koleksi','Collection menjadi kontrak bagi List, Set, dan Queue. Map merupakan bagian dari Collections Framework tetapi bukan subtype Collection. add, remove, contains, size, dan isEmpty adalah operasi umum; dukungan modifikasi tergantung implementasi.'),
('List','List menyimpan urutan dan dapat memuat duplikasi. ArrayList mendukung akses indeks; LinkedList juga mengimplementasikan Deque. Vector dan Stack adalah kelas lama; gunakan Deque untuk stack baru.'),
('Set','Set tidak menyimpan elemen duplikat. HashSet tidak menjanjikan urutan, LinkedHashSet menjaga urutan penyisipan, TreeSet mengurutkan menurut urutan alami atau comparator.'),
('Iterasi dan penghapusan','Iterator memakai hasNext dan next. Jika didukung, gunakan iterator.remove setelah next untuk menghapus elemen saat iterasi. Jangan memodifikasi koleksi langsung saat iterator masih berjalan kecuali kontraknya mengizinkan.')],[
('List dengan duplikasi','List<String> nama = new ArrayList<>();\nnama.add("Ravi"); nama.add("Vijay"); nama.add("Ravi");\nSystem.out.println(nama);','[Ravi, Vijay, Ravi]','List mempertahankan urutan dan duplikasi.'),
('Set sesuai urutan masuk','Set<String> nama = new LinkedHashSet<>();\nnama.add("Vijay"); nama.add("Ravi"); nama.add("Vijay");\nSystem.out.println(nama);','[Vijay, Ravi]','Set menolak duplikat; LinkedHashSet menjaga urutan penyisipan.'),
('Stack dengan Deque','Deque<String> s = new ArrayDeque<>();\ns.push("A"); s.push("B");\nSystem.out.println(s.pop());','B','Elemen terakhir yang masuk adalah yang pertama keluar.')],[
('Mana yang menjaga urutan masuk tanpa duplikat?','LinkedHashSet','HashSet','ArrayList','LinkedHashSet memenuhi kedua syarat tersebut.'),
('Apakah Map turunan Collection?','Tidak','Ya, melalui List','Ya, melalui Set','Map memiliki kontrak terpisah untuk pasangan kunci–nilai.')],
'Bandingkan hasil List, LinkedHashSet, dan TreeSet untuk input B, A, B. Jelaskan perbedaan urutan dan duplikasi.','collections')
m('11','11','Kelas generik','11','2–9','Buat kelas yang dapat dipakai dengan berbagai tipe tanpa casting manual saat membaca nilai.',[
('Motivasi','Kelas berbasis Object dapat menyimpan beragam nilai, tetapi pemanggil perlu casting dan dapat mengalami ClassCastException. Generics memindahkan banyak pemeriksaan tipe ke kompilasi.'),
('Parameter dan argumen tipe','Box<T> mendeklarasikan parameter T; Box<String> memilih String sebagai argumen tipe. new Box<>() memakai inferensi. Gunakan Integer, bukan int, sebagai argumen tipe.'),
('Konvensi nama','T sering berarti Type, E Element, K Key, V Value. Nama itu konvensi, bukan aturan sintaks. Hindari raw type karena melemahkan pemeriksaan tipe.'),
('Studi kasus kedai kopi','Pesanan<T> dapat menyimpan produk dengan tipe berbeda tanpa menggandakan kelas wadah. Jika operasi membutuhkan properti umum, pertimbangkan batas seperti T extends Produk.')],[
('Kotak teks','Box<String> b = new Box<>();\nb.set("Kopi");\nString isi = b.get();','Kompilasi berhasil; isi = Kopi','T digantikan String untuk pemeriksaan tipe.'),
('Tipe tidak cocok','Box<String> b = new Box<>();\nb.set(42);','Galat kompilasi','Nilai int yang di-box menjadi Integer tidak cocok dengan String.'),
('Kotak bilangan','Box<Integer> b = new Box<>();\nb.set(42);\nint hasil = b.get();','Kompilasi berhasil; hasil = 42','Java melakukan boxing dan unboxing untuk int dan Integer.')],[
('Mana deklarasi generik yang valid?','Box<Integer>','Box<int>','Box<42>','Argumen tipe adalah tipe referensi.'),
('Mengapa menghindari Box tanpa parameter tipe?','Pemeriksaan tipe menjadi lebih lemah','Kelas tidak bisa punya constructor','Semua field otomatis final','Raw type menghilangkan jaminan generik tertentu.')],
'Implementasikan Box<T> dengan set(T) dan get(). Buat Box<String> untuk nama menu dan Box<Integer> untuk jumlah.')
m('11-bonus','11 · Bonus','Nested class dan inner class','11 Bonus','2–7','Tentukan kapan kelas di dalam kelas lain membutuhkan instans luar.',[
('Istilah','Nested class adalah kelas yang dideklarasikan di dalam kelas lain. Member class non-static disebut inner class; static nested class tidak membutuhkan instans luar.'),
('Instans luar','Buat inner class dengan outer.new Inner(). Buat static nested class dengan new Outer.Nested(). Inner class dapat memakai Outer.this untuk merujuk instans luar.'),
('Akses anggota','Inner class dapat mengakses anggota private milik outer. Outer juga bisa mengakses anggota private nested class melalui referensi instans yang tepat. Scope dan kebutuhan referensi objek berbeda dari hak akses.'),
('Organisasi','Nested class dapat mengimplementasikan interface atau memperluas kelas sesuai aturan Java. Compiler umumnya menghasilkan nama file class dengan tanda $, misalnya Outer$Inner.class.')],[
('Inner non-static','Outer o = new Outer();\nOuter.Inner i = o.new Inner();','Kompilasi berhasil','i terikat ke instans o.'),
('Nested static','Outer.Nested n = new Outer.Nested();','Kompilasi berhasil','Tidak ada instans Outer implisit.'),
('Inner tanpa outer','Outer.Inner i = new Outer.Inner();','Galat kompilasi','Untuk member inner class non-static, gunakan instans outer.')],[
('Mana sintaks instans inner non-static?','outer.new Inner()','new Outer.Inner()','Outer.new Inner()','Instans luar digunakan sebelum .new.'),
('Bolehkah outer membaca field private inner?','Boleh melalui referensi inner yang tepat','Tidak pernah','Hanya jika field menjadi public','Akses private di antara kelas yang berada dalam top-level class yang sama dimungkinkan.')],
'Rancang Toko dengan inner class Kasir yang membaca nama toko, serta static nested class FormatNota yang tidak memerlukan instans toko.')
m('13','13','Anonymous inner class','13-','2–6','Buat implementasi satu kali pakai melalui subclass atau interface tanpa nama kelas baru.',[
('Deklarasi dan instans sekaligus','new Tipe(...) { ... } mendeklarasikan kelas anonim sekaligus membuat objeknya. Tipe dasar dapat berupa kelas yang dapat diturunkan atau satu interface yang akan diimplementasikan.'),
('Override dan kontrak','Gunakan @Override untuk memeriksa kesesuaian tanda tangan. Untuk interface, sediakan semua method abstrak yang tersisa. Kelas anonim tidak bisa menuliskan constructor bernama.'),
('Penangkapan variabel','Kelas anonim dapat menggunakan variabel lokal final atau effectively final dari lingkup luar. this di dalam badan kelas anonim menunjuk objek anonim itu sendiri.'),
('Pilih bentuk yang jelas','Gunakan kelas bernama jika perilaku perlu dipakai ulang atau cukup besar. Lambda cocok untuk interface fungsional ketika perbedaan semantik, seperti this, tidak dibutuhkan.')],[
('Implementasi Runnable','Runnable r = new Runnable() {\n  @Override public void run() { System.out.println("Siap"); }\n};\nr.run();','Siap','Pemanggilan run menjalankan method override; tidak otomatis membuat thread baru.'),
('Subclass sekali pakai','Object o = new Object() {\n  @Override public String toString() { return "Anonim"; }\n};\nSystem.out.println(o);','Anonim','println memakai toString yang dioverride.')],[
('Apakah r.run() otomatis membuat thread baru?','Tidak','Ya, karena Runnable','Ya, karena kelas anonim','run biasa adalah pemanggilan method.'),
('Variabel lokal yang ditangkap boleh ditugaskan ulang?','Tidak; harus final atau effectively final','Boleh tanpa syarat','Hanya bila private','Penangkapan variabel lokal mengikuti aturan final atau effectively final.')],
'Implementasikan Runnable anonim yang mencetak pesan dengan awalan dari variabel lokal. Coba ubah awalan setelah deklarasi dan jelaskan galat kompilasinya.')
m('13-bonus','13 · Bonus','Package, import, dan library','13 Bonus','2–8','Kelola lokasi tipe Java dan tambahkan dependensi tanpa mencampuradukkan import dan classpath.',[
('Ruang nama','Package mengelompokkan tipe terkait. Penamaan berbasis domain terbalik membantu menghindari tabrakan, misalnya id.ac.kampus.app. Susunan direktori sumber lazimnya mengikuti nama package.'),
('Deklarasi dan import','Deklarasi package mendahului import dan deklarasi tipe. import memungkinkan nama pendek; import java.util.* tidak mencakup subpackage. java.lang diimpor secara implisit.'),
('Library dan classpath','JAR dapat memuat kelas dan resource. import tidak memasang library. Pastikan classpath saat kompilasi dan runtime berisi dependensi yang diperlukan; pengelola build dapat mengurus resolusinya.'),
('Contoh API dan library','API adalah kontrak untuk memakai kemampuan tertentu; library adalah kode siap pakai yang dapat menyediakan API. Swing, JUnit, dan pustaka lain mempunyai tujuan berbeda.')],[
('Kompilasi dan jalankan package','// src/id/ac/kampus/App.java: package id.ac.kampus;\njavac -d out src/id/ac/kampus/App.java\njava -cp out id.ac.kampus.App','JVM mencari id/ac/kampus/App.class di out','Gunakan nama lengkap kelas, bukan nama file sumber.'),
('Library eksternal','javac -cp "lib/*" -d out src/id/ac/kampus/App.java\njava -cp "out:lib/*" id.ac.kampus.App','JAR ditemukan pada classpath','Pemisah classpath contoh ini untuk macOS/Linux; di Windows gunakan titik koma.')],[
('Apakah import memasang JAR?','Tidak','Ya, saat javac','Ya, jika menggunakan wildcard','JAR harus tersedia lewat classpath atau pengelola build.'),
('Apakah java.util.* mencakup java.util.concurrent?','Tidak','Ya, selalu','Ya, hanya saat runtime','Wildcard import tipe tidak bersifat rekursif.')],
'Bagi aplikasi menjadi package model dan app, kompilasi ke out, lalu jalankan main dengan nama kelas lengkap.',7)
m('14','14','Exception handling','14','2–15','Kenali jenis galat dan pilih cara menangani atau meneruskan exception.',[
('Tiga kategori masalah','Galat sintaks terdeteksi saat kompilasi. Galat runtime terjadi saat eksekusi; pembagian int dengan nol menimbulkan ArithmeticException. Galat logika dapat menghasilkan nilai salah tanpa exception.'),
('try dan catch','Tempatkan operasi berisiko dalam try dan tangani kasus yang bisa dipulihkan di catch. Urutkan catch dari tipe lebih spesifik ke tipe lebih umum. Hindari catch kosong.'),
('Checked dan unchecked','IOException adalah checked exception: tangani atau deklarasikan. RuntimeException dan turunannya unchecked. Error umumnya bukan kondisi pemulihan rutin.'),
('finally, throw, throws','finally biasanya dijalankan saat meninggalkan try/catch. Gunakan try-with-resources untuk menutup resource AutoCloseable. throw melempar objek exception, throws menyatakan exception pada signature.'),
('Diagnostik','Baca jenis exception dan stack trace, lalu cari baris pertama dari kode sendiri. NullPointerException, NumberFormatException, dan ArrayIndexOutOfBoundsException memiliki penyebab berbeda.')],[
('Penyebut valid','int d = 2;\ntry { System.out.println(10 / d); }\ncatch (ArithmeticException e) { System.out.println("Penyebut nol"); }\nfinally { System.out.println("Selesai"); }','5\nSelesai','try berhasil, catch dilewati, finally berjalan.'),
('Penyebut nol','int d = 0;\ntry { System.out.println(10 / d); }\ncatch (ArithmeticException e) { System.out.println("Penyebut nol"); }\nfinally { System.out.println("Selesai"); }','Penyebut nol\nSelesai','Pembagian int gagal saat runtime; catch yang cocok berjalan.'),
('Teks bukan bilangan','Integer.parseInt("dua");','NumberFormatException','Teks tidak memiliki representasi bilangan bulat yang valid.')],[
('Keyword yang melempar exception sekarang?','throw','throws','finally','throws hanya mendeklarasikan kemungkinan exception pada method.'),
('Mana contoh checked exception?','IOException','ArithmeticException','NullPointerException','IOException harus ditangani atau dideklarasikan.')],
'Buat pembaca bilangan yang menangani NumberFormatException dengan pesan yang membantu pengguna memperbaiki input.',11)
m('14-alt','14 · Alternatif','Baca dan tulis file Java','14 alt','2–9','Pilih stream yang sesuai dan bedakan karakter, byte, serta akhir file.',[
('Input dan output','InputStream membaca byte; OutputStream menulis byte. Reader dan Writer menangani karakter. Untuk teks tentukan charset, misalnya UTF-8.'),
('Metode penting','InputStream.read() mengembalikan 0–255 atau −1 saat akhir stream. OutputStream.write menulis; flush mendorong data buffered ke tujuan. close menutup resource. OutputStream tidak mempunyai read().'),
('File dan resource','FileInputStream dan FileOutputStream bekerja dengan file biner. Untuk teks sederhana gunakan Files.readString dan Files.writeString pada Java 11+. Untuk data besar, baca bertahap.'),
('Overwrite, append, dan galat','Penulisan default dapat mengganti isi file. Untuk menambah, pilih APPEND dan CREATE bila dibutuhkan. Tangani IOException dan gunakan try-with-resources ketika membuka stream sendiri.')],[
('Tulis teks UTF-8','Path file = Path.of("catatan.txt");\nFiles.writeString(file, "Halo", StandardCharsets.UTF_8);\nSystem.out.println(Files.readString(file, StandardCharsets.UTF_8));','Halo','Penulisan default membuat atau mengganti isi file.'),
('Tambahkan baris','// Isi awal file: Halo\nFiles.writeString(file, "\\nJava", StandardCharsets.UTF_8,\n                  StandardOpenOption.APPEND);\nSystem.out.println(Files.readString(file));','Halo\nJava','APPEND menulis di akhir file yang sudah ada.'),
('Baca akhir stream','try (InputStream in = new ByteArrayInputStream(new byte[]{65})) {\n  System.out.println(in.read());\n  System.out.println(in.read());\n}','65\n-1','Panggilan pertama membaca byte; kedua mencapai akhir stream.')],[
('Apa penanda akhir InputStream.read()?','-1','0','null','0 adalah byte valid; -1 menandakan tidak ada byte lagi.'),
('Apa yang menghindari masalah encoding teks?','Menyepakati charset seperti UTF-8','Mengganti semua teks menjadi int','Memanggil flush setelah read','Encoding pembaca dan penulis harus sesuai.')],
'Buat program yang menyimpan dua baris catatan UTF-8, menambahkan baris ketiga, lalu membacanya kembali. Tangani file yang belum ada.','io')
