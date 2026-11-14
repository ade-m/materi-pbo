'use strict';
(() => {
  const slides = [...document.querySelectorAll('.slide')];
  const $ = s => document.querySelector(s);
  const notes = JSON.parse($('#deck-notes').textContent);
  let index = 0;
  function fit() {
    const v = $('#viewport'), gap = innerWidth < 700 ? 8 : 40;
    const scale = Math.max(.1,Math.min((v.clientWidth-gap)/1280,(v.clientHeight-gap)/720));
    slides.forEach(s => s.style.transform = 'scale('+scale+')');
  }
  function go(n) {
    const next = Math.max(0,Math.min(slides.length-1,n));
    if (next!==index) window.scrollTo(0,0);
    index=next;
    slides.forEach((s,i) => {s.classList.toggle('active',i===index);s.inert=i!==index;});
    $('#counter').textContent = String(index+1).padStart(2,'0')+' / '+slides.length;
    $('#progress').style.width = (100*(index+1)/slides.length)+'%';
    $('#prev').disabled = index===0;
    $('#next').disabled = index===slides.length-1;
    $('#note-text').textContent = notes[index];
    history.replaceState(null,'','#slide-'+(index+1));
    fit();
  }
  function toc(open) {
    $('#toc').hidden = !open;
    (open ? $('#toc-close') : $('#toc-open')).focus();
  }
  function toggleNotes(open = $('#notes').hidden) {
    $('#notes').hidden = !open;
    $('#notes-toggle').setAttribute('aria-pressed',String(open));
  }
  slides.forEach((slide,i) => {
    const button = document.createElement('button'), number=document.createElement('span');
    number.textContent=String(i+1).padStart(2,'0');
    button.append(number,slide.querySelector('h1,h2').textContent);
    button.addEventListener('click',()=>{go(i);toc(false);});
    $('#toc-grid').append(button);
  });
  $('#prev').onclick=()=>go(index-1);
  $('#next').onclick=()=>go(index+1);
  $('#toc-open').onclick=()=>toc(true);
  $('#toc-close').onclick=()=>toc(false);
  $('#notes-toggle').onclick=()=>toggleNotes();
  $('#print').onclick=()=>print();
  $('#fullscreen').onclick=async()=>{
    try { if(document.fullscreenElement) await document.exitFullscreen(); else await document.documentElement.requestFullscreen(); }
    catch { $('#fullscreen').textContent='Gunakan menu browser'; }
  };
  document.querySelectorAll('[data-jump]').forEach(b=>b.onclick=()=>go(Number(b.dataset.jump)-1));
  document.addEventListener('keydown',e=>{
    if(e.key==='Escape'){if(!$('#toc').hidden)toc(false);toggleNotes(false);return;}
    if(e.ctrlKey||e.metaKey||e.altKey||e.target.closest('input,textarea,select,button,summary,a,pre,[contenteditable]')||!$('#toc').hidden)return;
    if(['ArrowRight','PageDown',' '].includes(e.key)){e.preventDefault();go(index+1);}
    if(['ArrowLeft','PageUp'].includes(e.key)){e.preventDefault();go(index-1);}
    if(e.key==='Home'){e.preventDefault();go(0);}
    if(e.key==='End'){e.preventDefault();go(slides.length-1);}
    if(e.key.toLowerCase()==='o')toc(true);
    if(e.key.toLowerCase()==='n')toggleNotes();
    if(e.key.toLowerCase()==='f')$('#fullscreen').click();
  });
  function fromHash(){go((Number(location.hash.match(/^#slide-(\d+)$/)?.[1])||1)-1);}
  window.addEventListener('resize',fit);
  window.addEventListener('fullscreenchange',fit);
  window.addEventListener('hashchange',fromHash);
  fromHash();
})();
