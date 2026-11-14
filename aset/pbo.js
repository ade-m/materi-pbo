'use strict';
const trace = document.querySelector('.trace-lab');
if (trace) {
  const find = s => trace.querySelector(s);
  const cases = JSON.parse(find('[data-traces]').textContent);
  const tabs = [...trace.querySelectorAll('[data-case]')];
  const code = find('[data-code]');
  const form = find('[data-prediction]');
  const select = form.querySelector('select');
  const outcome = find('[data-outcome]');
  let chosen = 0, step = -1, answer = null;
  function render() {
    const c = cases[chosen], final = step === c.steps.length;
    const current = c.steps[Math.min(step,c.steps.length-1)];
    const waiting = step === c.steps.length-1 && answer === null;
    tabs.forEach((b,i) => b.setAttribute('aria-pressed',String(i===chosen)));
    code.replaceChildren(...c.code.map((line,i) => {
      const row = document.createElement('span');
      row.className = 'trace-line';
      if (current?.[0]===i+1) row.setAttribute('aria-current','step');
      const num=document.createElement('span');
      num.textContent=String(i+1).padStart(2,'0');
      num.setAttribute('aria-hidden','true');
      row.append(num,line);
      return row;
    }));
    const active = code.querySelector('[aria-current]');
    if (active) code.parentElement.scrollTop = Math.max(0,active.offsetTop - code.offsetTop - 38);
    find('[data-position]').textContent = final ? 'Penelusuran selesai' : step < 0 ? 'Siap menelusuri' : 'Langkah '+(step+1)+' / '+c.steps.length;
    const title=document.createElement('h3'), state=document.createElement('p');
    title.textContent=current?.[1] || 'Keadaan awal';
    state.textContent=current?.[2] || 'Pilih Langkah pertama untuk memulai.';
    find('[data-state]').replaceChildren(title,state);
    form.hidden = !waiting;
    outcome.hidden = !final;
    if (final) {
      const verdict=document.createElement('strong'), result=document.createElement('samp'), reason=document.createElement('p');
      verdict.textContent=answer===c.result?'Prediksi tepat':answer===''?'Hasil dan alasan':'Prediksi belum tepat';
      result.textContent=c.result;
      reason.textContent=c.reason;
      outcome.replaceChildren(verdict,result,reason);
    }
    find('[data-back]').disabled=step<0;
    const next=find('[data-step]');
    next.disabled=waiting || final;
    next.textContent=step<0?'Langkah pertama':final?'Selesai':'Langkah berikutnya';
  }
  function reset(i=chosen) {
    chosen=i; step=-1; answer=null;
    const values=[...new Set(cases.map(c=>c.result))];
    const shift=(chosen+1)%values.length;
    select.replaceChildren(new Option('Pilih perkiraan hasil',''));
    select.options[0].disabled=true;
    values.slice(shift).concat(values.slice(0,shift)).forEach(v=>select.add(new Option(v.replaceAll('\n',' · '),v)));
    select.add(new Option('Belum yakin','skip'));
    render();
  }
  tabs.forEach((b,i)=>b.addEventListener('click',()=>reset(i)));
  find('[data-step]').addEventListener('click',()=>{step++;render();if(!form.hidden)select.focus();});
  find('[data-back]').addEventListener('click',()=>{step--;answer=null;select.selectedIndex=0;render();});
  find('[data-reset]').addEventListener('click',()=>reset());
  form.addEventListener('submit',e=>{e.preventDefault();if(!select.value)return;answer=select.value==='skip'?'':select.value;step=cases[chosen].steps.length;render();find('[data-back]').focus();});
  reset();
}
const quiz = document.querySelector('#kuis-form');
if (quiz) {
  const questions = [...quiz.querySelectorAll('fieldset')];
  const status = quiz.querySelector('[data-score]');
  const meter = document.querySelector('progress');
  const meterText = document.querySelector('[data-progress]');
  const key = 'materi-pbo:quiz:'+quiz.dataset.lesson+':v1';
  function render() {
    let right = 0, answered = 0;
    questions.forEach(q => {
      const selected = q.querySelector('input:checked');
      const feedback = q.querySelector('.feedback');
      feedback.hidden = !selected;
      if (!selected) return;
      answered++;
      const correct = selected.dataset.correct === 'true';
      right += Number(correct);
      feedback.dataset.ok = String(correct);
      feedback.textContent = (correct ? 'Tepat. ' : 'Belum tepat. ')+feedback.dataset.explanation;
    });
    status.textContent = answered ? right+' dari '+questions.length+' benar; '+answered+' dijawab.' : 'Pilih jawaban untuk melihat pembahasan.';
    meter.value = right;
    meterText.textContent = right+'/'+questions.length+' jawaban benar';
  }
  try {
    const saved = JSON.parse(localStorage.getItem(key) || '[]');
    if (Array.isArray(saved)) questions.forEach((q,i) => {
      const x = [...q.querySelectorAll('input')].find(el => el.value === saved[i]);
      if (x) x.checked = true;
    });
  } catch {}
  quiz.addEventListener('change', () => {
    render();
    try { localStorage.setItem(key,JSON.stringify(questions.map(q => q.querySelector('input:checked')?.value ?? null))); } catch {}
  });
  quiz.addEventListener('submit', e => e.preventDefault());
  quiz.addEventListener('reset', () => {
    try { localStorage.removeItem(key); } catch {}
    setTimeout(render,0);
  });
  render();
}

const live = document.querySelector('[data-live]');
if (live) {
  const input = live.querySelector('input');
  const output = live.querySelector('output');
  function update() {
    const v = input.value;
    const integer = Number(v);
    const valid = v !== '' && input.validity.valid && Number.isInteger(integer);
    let result;
    switch (live.dataset.live) {
      case '02':
        result = !valid ? 'Masukkan bilangan bulat antara −100 dan 100.' : integer === 0
          ? '10 / 0 dengan int → ArithmeticException.'
          : 'int: ' + Math.trunc(10/integer) + '\ndouble: ' + (10/integer);
        break;
      case '03':
        result = 'Sebelum: 0 → ' + (v.trim() || 'Kota pertama') + ', 1 → Binjai, 2 → Berastagi'
          + '\nSesudah remove(0): 0 → Binjai, 1 → Berastagi. Ukuran: 2.';
        break;
      case '10': {
        const list = v.split(',').map(x => x.trim()).filter(Boolean);
        result = 'List: ['+list.join(', ')+']\nLinkedHashSet: ['+[...new Set(list)].join(', ')+']'
          + '\nTreeSet (urutan alami String): ['+[...new Set(list)].sort().join(', ')+']';
        break;
      }
      case '14':
        result = !valid ? 'Masukkan bilangan bulat antara −100 dan 100.' : integer === 0
          ? 'try: ArithmeticException\ncatch: Penyebut nol\nfinally: Selesai'
          : 'try: '+Math.trunc(10/integer)+'\ncatch: dilewati\nfinally: Selesai';
        break;
      case '14-alt':
        result = 'Panjang String (unit UTF-16): '+v.length+'\nUkuran saat ditulis sebagai UTF-8: '+new TextEncoder().encode(v).length+' byte.';
    }
    output.textContent = result;
  }
  input.addEventListener('input', update);
  update();
}
