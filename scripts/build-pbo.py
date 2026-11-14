from pathlib import Path
from html import escape as e
from urllib.parse import quote
from kurikulum import M
root=Path(__file__).resolve().parents[1]
def wrap(title,base,body,js=False):
 return f'''<!doctype html>
<html lang="id"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)} | Materi PBO</title><link rel="stylesheet" href="{base}aset/pbo.css">{f'<script defer src="{base}aset/pbo.js"></script>' if js else ''}</head>
<body><div class="top"><div class="shell"><a href="{base}">Materi PBO</a><span>Ade Maulana, S.Kom., M.T.I.</span></div></div>
<main class="shell">{body}</main><footer><div class="shell">Pemrograman Berorientasi Objek · Ade Maulana, S.Kom., M.T.I.</div></footer></body></html>
'''
refs={
 7:('Java Language Specification: Packages','https://docs.oracle.com/javase/specs/jls/se21/html/jls-7.html'),
 8:('Java Language Specification: Classes','https://docs.oracle.com/javase/specs/jls/se21/html/jls-8.html'),
 10:('Java Language Specification: Arrays','https://docs.oracle.com/javase/specs/jls/se21/html/jls-10.html'),
 11:('Java Language Specification: Exceptions','https://docs.oracle.com/javase/specs/jls/se21/html/jls-11.html'),
 12:('Java Language Specification: Execution','https://docs.oracle.com/javase/specs/jls/se21/html/jls-12.html'),
 15:('Java Language Specification: Expressions','https://docs.oracle.com/javase/specs/jls/se21/html/jls-15.html'),
 'uml':('OMG: UML 2.5.1','https://www.omg.org/spec/UML/2.5.1/About-UML'),
 'collections':('Java API: Collections Framework','https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/package-summary.html'),
 'io':('Java API: Files','https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/nio/file/Files.html')
}
labs={
 '02':('Pembagian 10 dengan penyebut pilihan','Penyebut bulat (−100 sampai 100)','3','number'),
 '03':('Amati pergeseran indeks','Nama kota pertama yang akan dihapus','Medan','text'),
 '10':('Bandingkan List dan Set','Nama dipisahkan koma','B, A, B','text'),
 '14':('Telusuri blok try, catch, dan finally','Penyebut bulat (−100 sampai 100)','0','number'),
 '14-alt':('Hitung byte teks UTF-8','Teks yang akan ditulis','Halo, Medan!','text'),
}
for i,m in enumerate(M):
 n,t,slug=m['no'],m['title'],m['slug']
 concepts=''.join(f'<div class="concept"><h3>{e(k)}</h3><p>{e(v)}</p></div>' for k,v in m['concepts'])
 buttons=''.join(f'<button type="button" data-case="{j}" aria-pressed="{str(j==0).lower()}">{e(c[0])}</button>' for j,c in enumerate(m['cases']))
 examples=''.join(f'<div data-example="{j}"{" hidden" if j else ""}><pre tabindex="0"><code>{e(code)}</code></pre><div class="result" id="hasil-{j}" hidden aria-live="polite"><strong>Hasil</strong><br><samp>{e(result)}</samp><p>{e(reason)}</p></div></div>' for j,(_,code,result,reason) in enumerate(m['cases']))
 qs=[]
 for j,(question,correct,a,b,reason) in enumerate(m['quiz']):
  choices=[correct,a,b]; k=(i+j+1)%3; choices=choices[k:]+choices[:k]
  opts=''.join(f'<label class="option"><input type="radio" name="q{j}" value="{z}" data-correct="{str(v==correct).lower()}"><span>{e(v)}</span></label>' for z,v in enumerate(choices))
  qs.append(f'<fieldset><legend>{j+1}. {e(question)}</legend>{opts}<p class="feedback" data-explanation="{e(reason)}" aria-live="polite" hidden></p></fieldset>')
 links=[]
 if i: links.append(f'<a href="../{M[i-1]["slug"]}/">Sebelumnya: Pertemuan {e(M[i-1]["no"])}</a>')
 if i+1<len(M): links.append(f'<a href="../{M[i+1]["slug"]}/">Selanjutnya: Pertemuan {e(M[i+1]["no"])}</a>')
 else: links.append('<a href="../../jdbc/">Lanjut ke JDBC</a>')
 live=''
 if slug in labs:
  heading,label,value,kind=labs[slug]
  limit=' min="-100" max="100" step="1"' if kind=='number' else ' maxlength="160"'
  live=f'<div class="live-lab" data-live="{slug}"><h3>{e(heading)}</h3><label for="masukan-lab">{e(label)}</label><input id="masukan-lab" type="{kind}" value="{e(value)}"{limit}><output class="result" aria-live="polite"></output></div>'
 ref,url=refs[m['ref']]
 src=f'PBO - Pertemuan {m["source"]}.pdf'
 body=f'''<header class="hero"><h1>{e(t)}</h1><p>{e(m['intro'])}</p><span class="meta">Pertemuan {e(n)}</span></header>
<div class="layout"><aside class="aside"><nav aria-label="Isi modul"><a href="#konsep">Konsep</a><a href="#simulasi">Simulasi</a><a href="#kuis">Kuis</a><a href="#praktik">Praktik</a></nav>
<p class="meta" data-progress>0/{len(qs)} jawaban benar</p><progress max="{len(qs)}" value="0" aria-label="Jawaban kuis benar"></progress></aside>
<div><section id="konsep"><h2>Konsep inti</h2>{concepts}</section>
<section id="simulasi"><h2>Prediksi hasil</h2><p>Pilih skenario dan tebak hasilnya sebelum membuka pembahasan. Potongan kode Java menampilkan hasil yang diharapkan, tanpa menjalankan Java di browser.</p>
<div class="lab"><div class="choices" aria-label="Skenario">{buttons}</div>{examples}<button type="button" data-reveal class="primary" aria-expanded="false" aria-controls="hasil-0">Lihat hasil dan alasan</button>{live}</div></section>
<section id="kuis"><h2>Cek pemahaman</h2><form id="kuis-form" data-lesson="{slug}">{''.join(qs)}<p data-score role="status"></p><button type="reset" class="secondary">Ulangi kuis</button></form></section>
<section id="praktik"><h2>Latihan mandiri</h2><div class="task"><p>{e(m['task'])}</p></div></section>
<section aria-labelledby="sumber"><h2 id="sumber">Sumber</h2><p>Diadaptasi dari <cite>{e(src)}</cite>, halaman {e(m['pages'])}. <a href="{url}">{e(ref)}</a>.</p></section>
<nav class="paging" aria-label="Navigasi pertemuan">{''.join(links)}</nav></div></div>'''
 folder=root/'materi'/slug;folder.mkdir(parents=True,exist_ok=True);(folder/'index.html').write_text(wrap(t,'../../',body,True))
rows=''.join(f'<li><span class="meta">Pertemuan {e(m["no"])}</span><div><a href="materi/{m["slug"]}/">{e(m["title"])}</a><p>{e(m["intro"])}</p></div></li>' for m in M)
body=f'''<header class="hero"><h1>Pemrograman Berorientasi Objek</h1><p>Pelajari konsep Java, coba skenario, dan cek pemahaman lewat kuis setiap pertemuan.</p></header>
<div class="catalog"><section aria-labelledby="daftar"><h2 id="daftar">Materi per pertemuan</h2><ol>{rows}</ol></section>
<section aria-labelledby="jdbc"><h2 id="jdbc">Akses basis data</h2><div class="jdbc-row"><span class="meta">Materi JDBC</span><div><a href="jdbc/">Java Database Connectivity</a><p>27 slide, simulasi PostgreSQL, sinkronisasi model Java, dan pilihan koneksi lokal atau connection string.</p></div><a href="jdbc/bab-4-jdbc.pdf">Unduh PDF</a></div></section></div>'''
(root/'index.html').write_text(wrap('Daftar pertemuan','./',body))
