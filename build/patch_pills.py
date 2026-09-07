"""One rule for the pills that come out when the Layers panel is folded away, in both pages:
they sit in a row immediately alongside the folded pill, on whichever side has room.
Run once; it is kept here only as a record of the change."""
import os

BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..')

PILL_CSS = """
/* the pills that come out when the sidebar is folded away */
.floatbtn{
  position:absolute;display:none;z-index:4;height:30px;padding:0 13px;border-radius:14px;
  background:var(--panel);border:1px solid var(--panel-brd);box-shadow:var(--shadow);
  backdrop-filter:blur(18px) saturate(140%);-webkit-backdrop-filter:blur(18px) saturate(140%);
  font-size:10px;letter-spacing:.12em;text-transform:uppercase;color:var(--ink-faint);
}
.floatbtn:hover{background:rgba(255,255,255,.07);color:var(--ink)}
.floatbtn.on{background:rgba(142,208,255,.20);border-color:rgba(142,208,255,.45);color:var(--accent)}"""

PILL_JS = """/* The pills sit in a row beside the folded Layers pill, running towards the middle of the screen,
   so they land in the same place relative to it whatever corner the panel happens to fold into. */
function placePills() {
  var panel = document.getElementById('controls');
  var min = panel.classList.contains('min');
  var list = pillList();
  list.forEach(function (el) { el.style.display = min ? 'block' : 'none'; });
  if (!min || !list.length) return;
  var r = panel.getBoundingClientRect();
  var leftwards = (r.left + r.width / 2) > window.innerWidth / 2;
  var edge = leftwards ? r.left : r.right, gap = 8;
  for (var i = 0; i < list.length; i++) {
    var el = list[i], w = el.offsetWidth;
    var x = leftwards ? (edge - gap - w) : (edge + gap);
    if (x < 6 || x + w > window.innerWidth - 6) { el.style.display = 'none'; continue; }
    el.style.left = Math.round(x) + 'px';
    el.style.right = 'auto';
    el.style.top = Math.round(r.top) + 'px';
    edge = leftwards ? x : x + w;
  }
}"""


def patch(path, edits):
    s = open(path, encoding='utf-8').read()
    for old, new, n in edits:
        assert s.count(old) == n, (os.path.basename(path), s.count(old), old[:70])
        s = s.replace(old, new)
    open(path, 'w', encoding='utf-8', newline='\n').write(s)


# ------------------------------------------------------------------ celestial globe
cg = os.path.join(BASE, 'celestial-globe', 'index.html')
old_place = open(cg, encoding='utf-8').read()
i = old_place.index('/* The pills that come out when the sidebar is folded away')
j = old_place.index('function applyProjection() {')
patch(cg, [
    (old_place[i:j], PILL_JS + '\n', 1),
    ("  placeFloatReset();\n  var mast = document.getElementById('masthead')",
     "  placePills();\n  var mast = document.getElementById('masthead')", 1),
    ("  placeFloatReset();\n}", "  placePills();\n}", 1),
    ("""  var pf = document.getElementById('pointfloat');""", """  var pf = document.getElementById('pointfloat');""", 0),
    ("""  <button class="btn floatbtn" id="pointfloat" title="Hold the sky still, or let it follow the phone again">Freeze</button>""",
     """  <button class="btn floatbtn" id="pointfloat" title="Hold the sky still, or let it follow the phone again">Freeze</button>""", 1),
])
# the list of pills this page offers, nearest the panel first
patch(cg, [(PILL_JS, PILL_JS + """
function pillList() {
  var out = [document.getElementById('resetfloat')];
  if (pointAvailable) out.push(document.getElementById('pointfloat'));
  return out.filter(Boolean);
}""", 1)])

# ------------------------------------------------------------------ world clock
wc = os.path.join(BASE, 'world-clock-site', 'index.html')
patch(wc, [
    # styles
    ("#hint{\n  position:absolute;left:50%;", PILL_CSS + "\n\n#hint{\n  position:absolute;left:50%;", 1),
    # markup: the pill, after the controls panel so it can be found and placed
    ("""  <div class="panel" id="legend">""",
     """  <button class="btn floatbtn" id="resetfloat" title="Recentre and fit the globe">Reset view</button>

  <div class="panel" id="legend">""", 1),
    # placement, wired into resize and the panel toggle
    ("""function resize() {
  DPR = Math.min(window.devicePixelRatio || 1, 2);""",
     PILL_JS + """
function pillList() { return [document.getElementById('resetfloat')].filter(Boolean); }

function resize() {
  placePills();
  DPR = Math.min(window.devicePixelRatio || 1, 2);""", 1),
    ("""        if (!min && smallScreen()) foldPanels(p);
        if (p.id === 'scrubber') { timeSlider.paint(); dateSlider.paint(); }""",
     """        if (!min && smallScreen()) foldPanels(p);
        if (p.id === 'scrubber') { timeSlider.paint(); dateSlider.paint(); }
        placePills();""", 1),
    ("""document.getElementById('resetview').addEventListener('click', function () { resetView(); });""",
     """document.getElementById('resetview').addEventListener('click', function () { resetView(); });
document.getElementById('resetfloat').addEventListener('click', function (e) { e.stopPropagation(); resetView(); });""", 1),
])
# the folding helper must place the pills too
patch(wc, [("""function foldPanels(except) {
  document.querySelectorAll('.panel').forEach(function (p) {
    if (p !== except && !p.classList.contains('min')) {
      p.classList.add('min');
      var b = p.querySelector('.pmin');
      if (b) b.title = 'Restore';
    }
  });
}""",
"""function foldPanels(except) {
  document.querySelectorAll('.panel').forEach(function (p) {
    if (p !== except && !p.classList.contains('min')) {
      p.classList.add('min');
      var b = p.querySelector('.pmin');
      if (b) b.title = 'Restore';
    }
  });
  placePills();
}""", 1)])
print('pills unified across both pages')
