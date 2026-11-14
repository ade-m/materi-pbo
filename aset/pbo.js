'use strict';
const lab = document.querySelector('.lab');
if (lab) {
  const buttons = [...lab.querySelectorAll('[data-case]')];
  const examples = [...lab.querySelectorAll('[data-example]')];
  const reveal = lab.querySelector('[data-reveal]');
  let active = 0;
  function select(i) {
    active = i;
    buttons.forEach((b,j) => b.setAttribute('aria-pressed', String(i === j)));
    examples.forEach((x,j) => {
      x.hidden = i !== j;
      x.querySelector('.result').hidden = true;
    });
    reveal.setAttribute('aria-expanded','false');
    reveal.setAttribute('aria-controls','hasil-'+i);
    reveal.textContent = 'Lihat hasil dan alasan';
  }
  buttons.forEach((b,i) => b.addEventListener('click', () => select(i)));
  reveal.addEventListener('click', () => {
    const result = examples[active].querySelector('.result');
    result.hidden = !result.hidden;
    reveal.setAttribute('aria-expanded',String(!result.hidden));
    reveal.textContent = result.hidden ? 'Lihat hasil dan alasan' : 'Sembunyikan hasil';
  });
  select(0);
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
