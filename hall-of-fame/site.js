/* Pickleball Hall of Fame concept: motion layer.
   Everything is visible without JS. html.anim only hides what an observer will reveal,
   and three nets (observer, 1.5s in-view sweep, 8s backstop) make sure nothing stays hidden. */
(function () {
  var root = document.documentElement;
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (!reduce && 'IntersectionObserver' in window) root.classList.add('anim');

  /* split headlines into masked words */
  document.querySelectorAll('.split').forEach(function (el) {
    var delay = 0;
    (function walk(node) {
      Array.prototype.slice.call(node.childNodes).forEach(function (n) {
        if (n.nodeType === 3) {
          var frag = document.createDocumentFragment();
          n.textContent.split(/(\s+)/).forEach(function (part) {
            if (!part) return;
            if (/^\s+$/.test(part)) { frag.appendChild(document.createTextNode(part)); return; }
            var w = document.createElement('span'); w.className = 'w';
            var s = document.createElement('span'); s.textContent = part;
            s.style.transitionDelay = (delay += 0.07).toFixed(2) + 's';
            w.appendChild(s); frag.appendChild(w);
          });
          n.parentNode.replaceChild(frag, n);
        } else if (n.nodeType === 1 && n.tagName !== 'BR') walk(n);
      });
    })(el);
  });

  /* reveal */
  var items = document.querySelectorAll('.rv,.split,.honor,.growth,.step,.stage');
  function show(el) { el.classList.add('in'); }
  if (root.classList.contains('anim')) {
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (e) { if (e.isIntersecting) { show(e.target); io.unobserve(e.target); } });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });
    items.forEach(function (el) { io.observe(el); });
    setTimeout(function () {
      items.forEach(function (el) { var r = el.getBoundingClientRect(); if (r.top < innerHeight && r.bottom > 0) show(el); });
    }, 1500);
    setTimeout(function () { items.forEach(show); }, 8000);
  } else items.forEach(show);

  /* header + mobile drawer */
  var hdr = document.querySelector('.hdr');
  function onHdr() { if (hdr) hdr.classList.toggle('solid', scrollY > 40); }
  var burger = document.querySelector('.burger');
  if (burger) burger.addEventListener('click', function () {
    var open = document.body.classList.toggle('menu-open');
    burger.setAttribute('aria-expanded', open ? 'true' : 'false');
  });

  /* count-ups */
  function countUp(el) {
    var end = parseFloat(el.dataset.count), start = parseFloat(el.dataset.from || 0);
    var plus = el.dataset.plus || '', dur = 1800, t0 = null;
    var fmt = function (v) { return el.hasAttribute('data-plain') ? String(v) : v.toLocaleString('en-US'); };
    if (reduce) { el.textContent = fmt(end) + plus; return; }
    function tick(t) {
      if (!t0) t0 = t;
      var k = Math.min(1, (t - t0) / dur), e = 1 - Math.pow(1 - k, 4);
      el.textContent = fmt(Math.round(start + (end - start) * e)) + (k === 1 ? plus : '');
      if (k < 1) requestAnimationFrame(tick);
    }
    requestAnimationFrame(tick);
  }
  var counts = document.querySelectorAll('[data-count]');
  if ('IntersectionObserver' in window) {
    var cio = new IntersectionObserver(function (es) {
      es.forEach(function (e) { if (e.isIntersecting) { countUp(e.target); cio.unobserve(e.target); } });
    }, { threshold: 0.5 });
    counts.forEach(function (el) { cio.observe(el); });
  }

  /* mission words light up with scroll */
  var words = [];
  document.querySelectorAll('.words').forEach(function (p) {
    var html = '';
    p.textContent.trim().split(/\s+/).forEach(function (w) {
      var gold = /^\*/.test(w); w = w.replace(/\*/g, '');
      html += '<span class="wd' + (gold ? ' gold' : '') + '">' + w + '</span> ';
    });
    p.innerHTML = html;
    words.push(p);
  });

  /* scroll-linked pieces */
  var hall = document.querySelector('.hall'), track = hall && hall.querySelector('.track');
  var rails = document.querySelectorAll('[data-rail]');
  function prog(el, a, b) {
    var r = el.getBoundingClientRect();
    var start = innerHeight * a, span = r.height + innerHeight * (b - a);
    return Math.max(0, Math.min(1, (start - r.top) / span));
  }
  function frame() {
    onHdr();
    words.forEach(function (p) {
      var r = p.getBoundingClientRect();
      var k = Math.max(0, Math.min(1, (innerHeight * 0.85 - r.top) / (r.height + innerHeight * 0.35)));
      var spans = p.children, lit = Math.round(k * spans.length);
      for (var i = 0; i < spans.length; i++) spans[i].classList.toggle('on', i < lit);
    });
    if (hall && track && innerWidth > 760) {
      var r = hall.getBoundingClientRect();
      var k = Math.max(0, Math.min(1, -r.top / (r.height - innerHeight)));
      var max = track.scrollWidth - innerWidth + parseFloat(getComputedStyle(track).paddingLeft);
      track.style.transform = 'translate3d(' + (-k * Math.max(0, max)) + 'px,0,0)';
      hall.style.setProperty('--p', k.toFixed(4));
    }
    rails.forEach(function (el) { el.style.setProperty('--p', prog(el, 0.6, 0.2).toFixed(4)); });
  }
  var ticking = false;
  function req() { if (!ticking) { ticking = true; requestAnimationFrame(function () { ticking = false; frame(); }); } }
  addEventListener('scroll', req, { passive: true });
  addEventListener('resize', req);
  frame();

  /* inductee filters */
  var chips = document.querySelectorAll('.chip');
  var cards = document.querySelectorAll('.card');
  var countEl = document.querySelector('.count');
  var state = { cat: 'all', year: 'all' };
  chips.forEach(function (c) {
    c.addEventListener('click', function () {
      var kind = c.dataset.kind;
      state[kind] = c.dataset.val;
      document.querySelectorAll('.chip[data-kind="' + kind + '"]').forEach(function (o) { o.setAttribute('aria-pressed', o === c ? 'true' : 'false'); });
      var n = 0;
      cards.forEach(function (card) {
        var ok = (state.cat === 'all' || card.dataset.cat.indexOf(state.cat) > -1) && (state.year === 'all' || card.dataset.year === state.year);
        card.classList.toggle('out', !ok);
        if (ok) n++;
      });
      if (countEl) countEl.textContent = n + (n === 1 ? ' inductee' : ' inductees');
    });
  });

  /* gentle 3D tilt on cards (pointer devices only) */
  if (!reduce && window.matchMedia('(hover:hover)').matches) {
    document.querySelectorAll('.card,.plaque').forEach(function (card) {
      var inner = card.querySelector('.in3d') || card;
      card.addEventListener('pointermove', function (e) {
        var r = card.getBoundingClientRect();
        var x = (e.clientX - r.left) / r.width - 0.5, y = (e.clientY - r.top) / r.height - 0.5;
        inner.style.transform = 'perspective(900px) rotateY(' + (x * 8).toFixed(2) + 'deg) rotateX(' + (-y * 8).toFixed(2) + 'deg)';
      });
      card.addEventListener('pointerleave', function () { inner.style.transform = ''; });
    });
  }
})();
