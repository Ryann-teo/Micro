
// Search across sidebar and visible content
document.addEventListener('DOMContentLoaded', function() {
  var search = document.getElementById('search');
  if (!search) return;
  search.addEventListener('input', function() {
    var q = search.value.toLowerCase().trim();
    var nodes = document.querySelectorAll('.sidebar-concept');
    nodes.forEach(function(a) {
      var n = (a.getAttribute('data-name') || a.textContent).toLowerCase();
      var parent = a.parentElement;
      if (q === '' || n.indexOf(q) >= 0) {
        if (parent) parent.classList.remove('hidden');
      } else {
        if (parent) parent.classList.add('hidden');
      }
    });
    // Hide topic sections with no visible concepts
    document.querySelectorAll('.sidebar-section').forEach(function(sec) {
      var visible = sec.querySelectorAll('.sidebar-concepts li:not(.hidden)').length;
      if (q === '' || visible > 0 || sec.querySelector('.sidebar-link')) {
        sec.classList.remove('hidden');
      } else {
        sec.classList.add('hidden');
      }
    });
    // Index page: filter all-concepts list
    document.querySelectorAll('.all-concepts .concept-list li').forEach(function(li) {
      var t = li.textContent.toLowerCase();
      if (q === '' || t.indexOf(q) >= 0) li.classList.remove('hidden');
      else li.classList.add('hidden');
    });
  });
});
