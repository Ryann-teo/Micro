
// Auto-open concept card and scroll to it when navigated to
function openConcept(slug) {
  var el = document.getElementById('concept-' + slug);
  if (el) {
    el.open = true;
    // Open ancestor sections too
    var parent = el.parentElement;
    while (parent) {
      if (parent.tagName === 'DETAILS') parent.open = true;
      parent = parent.parentElement;
    }
    setTimeout(function() { el.scrollIntoView({ behavior: 'smooth', block: 'start' }); }, 60);
  }
}
function openAnchor(id) {
  var el = document.getElementById(id);
  if (el) {
    var node = el;
    while (node) {
      if (node.tagName === 'DETAILS') node.open = true;
      node = node.parentElement;
    }
    setTimeout(function() { el.scrollIntoView({ behavior: 'smooth', block: 'start' }); }, 60);
  }
}

document.addEventListener('DOMContentLoaded', function() {
  // Initial hash open
  if (window.location.hash) {
    var id = window.location.hash.substring(1);
    if (id.startsWith('concept-')) openConcept(id.substring('concept-'.length));
    else openAnchor(id);
  }
  // Sidebar links: scroll + auto-open target
  document.querySelectorAll('.side-link').forEach(function(a) {
    a.addEventListener('click', function(e) {
      var anchor = a.getAttribute('data-anchor');
      if (anchor) {
        if (anchor.startsWith('concept-')) openConcept(anchor.substring('concept-'.length));
        else openAnchor(anchor);
      }
    });
  });
  // Top nav links: scroll smoothly
  document.querySelectorAll('.topnav a').forEach(function(a) {
    a.addEventListener('click', function(e) {
      var href = a.getAttribute('href');
      if (href && href.startsWith('#')) {
        e.preventDefault();
        openAnchor(href.substring(1));
      }
    });
  });
  // Wiki links inside QT content: auto-open concept on click (also handled inline)
  document.querySelectorAll('a.wikilink[href^="#concept-"]').forEach(function(a) {
    a.addEventListener('click', function(e) {
      var href = a.getAttribute('href');
      if (href) {
        var slug = href.substring('#concept-'.length);
        openConcept(slug);
      }
    });
  });

  // Search
  var s = document.getElementById('search');
  if (s) {
    s.addEventListener('input', function() {
      var q = s.value.toLowerCase().trim();
      // Sidebar concept links
      document.querySelectorAll('.side-list .side-link').forEach(function(a) {
        var n = (a.getAttribute('data-name') || a.textContent).toLowerCase();
        var li = a.parentElement;
        if (q === '' || n.indexOf(q) >= 0) li.classList.remove('hidden');
        else li.classList.add('hidden');
      });
      // Concept cards
      document.querySelectorAll('.concept-card').forEach(function(card) {
        var name = (card.querySelector('.concept-name')||{}).textContent || '';
        var bodyTxt = (card.querySelector('.concept-body')||{}).textContent || '';
        var hay = (name + ' ' + bodyTxt).toLowerCase();
        if (q === '' || hay.indexOf(q) >= 0) card.classList.remove('hidden');
        else card.classList.add('hidden');
      });
    });
  }

  // Open the topic section in the sidebar matching the URL hash on load
  if (window.location.hash) {
    var hash = window.location.hash;
    var m = hash.match(/^#concept-(.+)$/);
    if (m) {
      var card = document.getElementById('concept-' + m[1]);
      if (card) {
        var topic = card.getAttribute('data-topic');
        var side = document.querySelector('.side-topic[data-topic-id="' + topic + '"]');
        if (side) side.open = true;
      }
    }
  }
});
