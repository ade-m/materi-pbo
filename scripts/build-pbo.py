from pathlib import Path
from html import escape as e
import re, json, base64
from kurikulum import M
from jejak import T
root=Path(__file__).resolve().parents[1]
def wrap(title,base,body,js=False):
 return f'''<!doctype html>
<html lang="id"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)} | Materi PBO</title><link rel="stylesheet" href="{base}aset/pbo.css">{f'<script defer src="{base}aset/pbo.js"></script>' if js else ''}</head>
<body><div class="top"><div class="shell"><a href="{base}">Materi PBO</a><span>Ade Maulana, S.Kom., M.T.I.</span></div></div>
<main class="shell">{body}</main><footer><div class="shell">Pemrograman Berorientasi Objek · Ade Maulana, S.Kom., M.T.I.</div></footer></body></html>
'''

jdbc=(root/'jdbc/index.html').read_text()
jdbc_style=jdbc.split('<style>',1)[1].split('</style>',1)[0]
base_css=jdbc_style[jdbc_style.index(':root{'):jdbc_style.index('.print-quiz{')]
base_css=re.sub(r'#slide-\d+[^{}]*\{[^{}]*\}', '', base_css)
footer_css=re.search(r'\.slide footer\{display:grid.*?tabular-nums\}',jdbc_style).group()
font_css=''
for weight in (600,700,800):
 face=re.search(r"@font-face\s*\{[^}]*font-weight:\s*"+str(weight)+r";[^}]*\}",jdbc_style).group()
 data=base64.b64decode(re.search(r'base64,([^)]*)',face)[1])
 name=f'inter-{weight}.ttf'
 (root/'aset'/name).write_bytes(data)
 font_css+=f'@font-face{{font-family:Inter;src:url({name}) format("truetype");font-weight:{weight};font-display:swap}}\n'
(root/'aset/deck-base.css').write_text('@font-face{font-family:Inter;src:url(inter.ttf) format("truetype");font-display:swap}\n'+font_css+base_css+'\n'+footer_css+'\n')
chrome=jdbc.split('</main>',1)[1].split('<script>',1)[0]
chrome=chrome.replace('Jelajahi Bab 4','Daftar slide').replace('01 / 27','01').replace('<button id="toc-open">','<a href="../../">Materi PBO</a><button id="toc-open">')

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
 traces=[dict(name=name,code=code.splitlines(),result=result,reason=reason,steps=steps)
         for (name,code,result,reason),steps in zip(m['cases'],T[slug])]
 assert len(traces)==len(m['cases'])==len(T[slug])
 assert all(len(t['steps'])>=2 and all(1<=line<=len(t['code']) for line,_,_ in t['steps']) for t in traces)
 trace_json=json.dumps(traces,ensure_ascii=False).replace('<','\\u003c')
 buttons=''.join(f'<button type="button" data-case="{j}" aria-pressed="{str(j==0).lower()}">{e(c["name"])}</button>' for j,c in enumerate(traces))
 trace_html=f'''<div class="trace-lab"><div class="choices" aria-label="Skenario">{buttons}</div>
 <div class="trace-grid"><pre tabindex="0" aria-label="Kode yang ditelusuri"><code data-code></code></pre>
 <div class="trace-state"><p class="hint" data-position></p><div data-state aria-live="polite"></div><form data-prediction hidden><label>Prediksi hasil <select required></select></label><button type="submit">Periksa</button></form><div data-outcome role="status" hidden></div></div></div>
 <div class="trace-controls"><button type="button" data-back class="secondary">Mundur</button><button type="button" data-step>Langkah pertama</button><button type="button" data-reset class="secondary">Ulangi</button></div>
 <script type="application/json" data-traces>{trace_json}</script></div>
 <div class="trace-print"><p><b>{e(traces[0]['name'])}</b> — {e(traces[0]['reason'])}</p><pre>{e(chr(10).join(traces[0]['code']))}</pre><p><b>Hasil:</b> {e(traces[0]['result'])}</p></div>'''
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
 slides=[]
 def add(heading, subtitle, body, note, cls=''):
  slides.append((heading,subtitle,body,note,cls))
 add(t,'Pertemuan '+n+' · Pemrograman Berorientasi Objek',
     f'<div class="cover-grid"><div><p class="lead">{e(m["intro"])}</p><div class="tags"><span>Konsep</span><span>Simulasi</span><span>Kuis</span></div><button data-jump="2">Mulai belajar</button> <button class="secondary" data-jump="{len(m["concepts"])+3}">Buka lab</button><p class="hint">← → untuk slide · O daftar · F layar penuh</p></div><div class="cover-sequence">{ "".join(f"<div><span>{k:02}</span><strong>{e(label)}</strong></div>" for k,label in enumerate(("Pelajari konsep","Lab bertahap","Cek pemahaman"),1)) }</div></div>',
     'Minta mahasiswa menyebutkan pengalaman atau contoh terkait topik sebelum membuka konsep inti.','cover')
 add('Peta pembelajaran','Topik yang dibahas',
     '<div class="topic-list">'+''.join(f'<button class="secondary" data-jump="{j+3}"><span>{j+1:02}</span>{e(k)}</button>' for j,(k,v) in enumerate(m['concepts']))+'</div>',
     'Gunakan peta untuk melompat ke konsep yang ingin dibahas.')
 for j,(k,v) in enumerate(m['concepts']):
  add(k,f'Konsep {j+1} dari {len(m["concepts"])}',f'<div class="feature concept-slide"><p>{e(v)}</p></div><p class="hint source-note">Sumber: {e(src)}, hlm. {e(m["pages"])}</p>',
      'Minta satu contoh tambahan dari mahasiswa, kemudian cocokkan dengan definisi pada slide.')
 add('Lab: telusuri dan prediksi','Jalankan satu tahap, amati keadaan, lalu prediksi hasil akhir.',
     trace_html+'<p class="hint">Simulasi terarah. Cuplikan kode tidak dijalankan oleh JVM di browser.</p>',
     'Minta mahasiswa memprediksi keadaan pada tahap berikutnya, kemudian bandingkan dengan panel keadaan.','practice')
 if live:
  add('Coba dengan masukan sendiri','Ubah nilai untuk melihat hasil simulasi.',live,
      'Uji satu nilai normal dan satu nilai batas. Bandingkan prediksi dengan hasil simulasi.')
 add('Cek pemahaman','Pilih jawaban untuk melihat umpan balik.',
     f'<form id="kuis-form" data-lesson="{slug}"><div class="quiz-columns">{"".join(qs)}</div><div class="quiz-status"><p data-score role="status"></p><button type="reset" class="secondary">Ulangi kuis</button></div><progress max="{len(qs)}" value="0" aria-label="Jawaban kuis benar"></progress><small data-progress>0/{len(qs)} jawaban benar</small></form><div class="print-answers"><h3>Kunci dan pembahasan</h3>{"".join(f"<p><b>{j+1}. {e(q[1])}</b> — {e(q[4])}</p>" for j,q in enumerate(m["quiz"]))}</div>',
     'Diskusikan alasan di balik jawaban, termasuk mengapa pilihan lain kurang tepat.','quiz-slide')
 add('Latihan mandiri','Terapkan konsep pada program Java.',
     f'<div class="callout"><p>{e(m["task"])}</p></div>',
     'Minta mahasiswa menjelaskan hasil dan satu kasus yang mereka uji.')
 add('Sumber dan pertemuan berikutnya','Rujukan untuk memperdalam materi.',
     f'<div class="feature"><p>Diadaptasi dari <cite>{e(src)}</cite>, halaman {e(m["pages"])}.</p><p><a href="{url}">{e(ref)}</a></p></div><nav class="paging" aria-label="Navigasi pertemuan">{"".join(links)}<a href="../../">Kembali ke daftar materi</a></nav>',
     'Arahkan mahasiswa ke rujukan dan pertemuan berikutnya.')
 htmlslides=[]
 for j,(heading,sub,content,note,cls) in enumerate(slides,1):
  tag='h1' if j==1 else 'h2'
  htmlslides.append(f'<section class="slide {cls}{" active" if j==1 else ""}" id="slide-{j}" aria-label="Slide {j}: {e(heading)}"{" inert" if j>1 else ""}><header><{tag}>{e(heading)}</{tag}><p class="subtitle">{e(sub)}</p></header><div class="body">{content}</div><footer><span class="course-identity">Mata Kuliah Pemrograman Berorientasi Objek</span><span class="lecturer-identity">Ade Maulana., S.Kom., M.T.I.</span><span class="footer-source">Pertemuan {e(n)}</span><span>{j:02} / {len(slides)}</span></footer></section>')
 notes=json.dumps([x[3] for x in slides],ensure_ascii=False).replace('<','\\u003c')
 page=f'''<!doctype html><html lang="id"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{e(t)} | Materi PBO</title><link rel="stylesheet" href="../../aset/deck-base.css"><link rel="stylesheet" href="../../aset/deck.css"><script defer src="../../aset/deck.js"></script><script defer src="../../aset/pbo.js"></script></head><body><main id="viewport">{"".join(htmlslides)}</main>{chrome}<script type="application/json" id="deck-notes">{notes}</script></body></html>'''
 folder=root/'materi'/slug;folder.mkdir(parents=True,exist_ok=True);(folder/'index.html').write_text(page)

rows=''.join(f'<li><span class="meta">Pertemuan {e(m["no"])}</span><div><a href="materi/{m["slug"]}/">{e(m["title"])}</a><p>{e(m["intro"])}</p></div></li>' for m in M)
body=f'''<header class="hero"><h1>Pemrograman Berorientasi Objek</h1><p>Telusuri perubahan program langkah demi langkah, uji prediksi, lalu cek pemahaman di setiap pertemuan.</p></header>
<div class="catalog"><section aria-labelledby="daftar"><h2 id="daftar">Materi per pertemuan</h2><ol>{rows}</ol></section>
<section aria-labelledby="jdbc"><h2 id="jdbc">Akses basis data</h2><div class="jdbc-row"><span class="meta">Materi JDBC</span><div><a href="jdbc/">Java Database Connectivity</a><p>27 slide, simulasi PostgreSQL, sinkronisasi model Java, dan pilihan koneksi lokal atau connection string.</p></div><a href="jdbc/bab-4-jdbc.pdf">Unduh PDF</a></div></section></div>'''
(root/'index.html').write_text(wrap('Daftar pertemuan','./',body))
