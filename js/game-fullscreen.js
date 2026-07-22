/* Shared full-screen "play mode" for all game pages.
   - On phones/tablets shows a floating "Full screen" button.
   - Tapping it hides the site header/footer/hero and fills the screen with the game.
   - Also requests native fullscreen where the browser supports it (Android/iPad).
   - Desktop is left untouched (button hidden on wide screens). */
(function(){
  var css = ''
    + '.fs-btn{position:fixed;right:12px;bottom:12px;z-index:10000;background:#2a9d8f;color:#fff;border:none;'
    + 'border-radius:999px;padding:11px 16px;font-weight:800;font-size:14px;font-family:inherit;cursor:pointer;'
    + 'box-shadow:0 3px 10px rgba(0,0,0,.28);display:none}'
    + '.fs-btn:active{transform:scale(.96)}'
    + '.fs-exit{position:fixed;right:12px;top:12px;z-index:10001;background:#e63946;color:#fff;border:none;'
    + 'border-radius:999px;width:44px;height:44px;font-size:20px;font-weight:900;cursor:pointer;'
    + 'box-shadow:0 3px 10px rgba(0,0,0,.28);display:none}'
    + '@media(max-width:900px){.fs-btn{display:block}}'
    + 'body.play-mode .site-header,body.play-mode .site-footer,body.play-mode .hero,'
    + 'body.play-mode .howto,body.play-mode .ad-slot{display:none!important}'
    + 'body.play-mode{overflow:hidden}'
    + 'body.play-mode .pm-host{position:fixed!important;inset:0!important;margin:0!important;'
    + 'border-radius:0!important;max-width:none!important;width:100%!important;height:100%!important;'
    + 'overflow:auto!important;z-index:9998;padding:52px 10px 16px;box-sizing:border-box}'
    + 'body.play-mode .fs-btn{display:none!important}'
    + 'body.play-mode .fs-exit{display:block}';
  var st=document.createElement('style'); st.textContent=css; document.head.appendChild(st);

  function host(){ return document.querySelector('[data-fs-host]') || document.querySelector('.panel') || document.querySelector('main'); }

  var enterBtn=document.createElement('button');
  enterBtn.className='fs-btn'; enterBtn.type='button'; enterBtn.textContent='⛶ Full screen';
  var exitBtn=document.createElement('button');
  exitBtn.className='fs-exit'; exitBtn.type='button'; exitBtn.setAttribute('aria-label','Exit full screen'); exitBtn.textContent='✕';

  function nativeOn(){
    var el=document.documentElement;
    try{ if(el.requestFullscreen) el.requestFullscreen(); else if(el.webkitRequestFullscreen) el.webkitRequestFullscreen(); }catch(e){}
  }
  function nativeOff(){
    try{ if(document.fullscreenElement||document.webkitFullscreenElement){ if(document.exitFullscreen) document.exitFullscreen(); else if(document.webkitExitFullscreen) document.webkitExitFullscreen(); } }catch(e){}
  }
  function enter(){
    var h=host(); if(h) h.classList.add('pm-host');
    document.body.classList.add('play-mode');
    nativeOn();
    window.scrollTo(0,0);
    window.dispatchEvent(new Event('resize'));
  }
  function exit(){
    document.body.classList.remove('play-mode');
    var h=document.querySelector('.pm-host'); if(h) h.classList.remove('pm-host');
    nativeOff();
    window.dispatchEvent(new Event('resize'));
  }
  enterBtn.addEventListener('click',enter);
  exitBtn.addEventListener('click',exit);
  // keep CSS mode in sync if the user leaves native fullscreen with a system gesture
  function onFsChange(){ if(!(document.fullscreenElement||document.webkitFullscreenElement) && document.body.classList.contains('play-mode')){ /* stay in CSS mode; do nothing */ } }
  document.addEventListener('fullscreenchange',onFsChange);
  document.addEventListener('webkitfullscreenchange',onFsChange);

  document.body.appendChild(enterBtn);
  document.body.appendChild(exitBtn);
})();
