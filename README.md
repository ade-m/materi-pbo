# Materi PBO

Materi perkuliahan **Pemrograman Berorientasi Objek** — **Ade Maulana., S.Kom., M.T.I.**

🌐 https://ade-m.github.io/materi-pbo/

## Daftar materi

- [Bab 4 — JDBC](https://ade-m.github.io/materi-pbo/jdbc/): 27 slide, simulator akses 10 tahap, panduan PostgreSQL, sinkronisasi model Java, dan 6 soal kuis.

## Struktur

- `index.html`: daftar materi perkuliahan.
- `jdbc/`: presentasi dan berkas latihan JDBC.

Untuk materi berikutnya, tambahkan folder topik baru dan tautkan dari halaman depan.

## Penggunaan

Presentasi: panah untuk navigasi; O daftar slide; F layar penuh. Di simulator (slide 11 dan20), panah/Spasi menjalankan tahapan; PageUp/PageDown berpindah slide. Semua simulasi memakai JavaScript lokal; tidak terhubung ke database nyata.

Referensi materi ditautkan di presentasi. Font Inter menggunakan SIL Open Font License; lihat `jdbc/FONT-LICENSE.txt`.

## Materi per pertemuan

Katalog mencakup Pertemuan 1–7, 9–11, 13–14, serta 11 Bonus, 13 Bonus, dan 14 Alternatif. Pertemuan 5–7 diadaptasi dari satu PDF gabungan. Pertemuan 8 dan 12 tidak disertakan karena tidak ada PDF sumber. Setiap modul mencantumkan halaman sumber dan menyediakan skenario prediksi, kuis, serta latihan.

Ubah data pada `scripts/kurikulum.py`, lalu jalankan `PYTHONDONTWRITEBYTECODE=1 python3 scripts/build-pbo.py`. Kuis menyimpan pilihan secara lokal di browser. Skenario kode menampilkan hasil pembelajaran yang telah disiapkan, bukan menjalankan Java di browser.

Modul per pertemuan menggunakan template presentasi JDBC. Build mengambil kerangka visual dari `jdbc/index.html`; `aset/deck.css` menyesuaikan konten pertemuan dan tampilan potret ponsel. Navigasi: panah kiri/kanan, O untuk daftar slide, N untuk catatan, dan F untuk layar penuh.

Lab setiap pertemuan menyorot baris kode dan memperlihatkan perubahan keadaan per langkah. Mahasiswa bisa mundur atau mengulang, lalu memilih prediksi sebelum hasil dibuka. Skenario dan keadaan tiap langkah didefinisikan di `scripts/kurikulum.py` dan `scripts/jejak.py`. Lima pertemuan juga punya simulasi dengan masukan sendiri.
