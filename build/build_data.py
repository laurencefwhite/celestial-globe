"""Assemble the embedded data block for the celestial globe.

Downloads the sources into build/cache (only when missing), compacts them, and
splices a <script> block into ../index.html between the CG_DATA markers. Run it
again to refresh the satellite snapshot or the asteroid elements:

    python build_data.py            # rebuild the data block
    python build_data.py --refresh  # also re-download the live sources (TLEs, JPL)

Sources
  HYG star database v4.1 (David Nash, CC BY-SA 4.0)
  d3-celestial data (Olaf Frohn, BSD-3): star names, constellations, DSOs, Milky Way, planets
  JPL SBDB (asteroid elements), JPL Horizons (moon state vectors)
  CelesTrak GP elements (satellites)
  World clock city list (this repo's sibling project)
"""
import base64, csv, json, math, os, re, struct, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(HERE, 'cache')
INDEX = os.path.join(HERE, '..', 'index.html')
REFRESH = '--refresh' in sys.argv
os.makedirs(CACHE, exist_ok=True)

D3C = 'https://raw.githubusercontent.com/ofrohn/d3-celestial/master/data/'
SOURCES = {
    'hygdata_v41.csv': 'https://raw.githubusercontent.com/astronexus/HYG-Database/main/hyg/CURRENT/hygdata_v41.csv',
    'starnames.json': D3C + 'starnames.json',
    'constellations.json': D3C + 'constellations.json',
    'constellations.lines.json': D3C + 'constellations.lines.json',
    'constellations.bounds.json': D3C + 'constellations.bounds.json',
    'dsos.14.json': D3C + 'dsos.14.json',
    'messier.json': D3C + 'messier.json',
    'dsonames.json': D3C + 'dsonames.json',
    'mw.json': D3C + 'mw.json',
    'planets.json': D3C + 'planets.json',
}
LIVE = {
    'sat_visual.json': 'https://celestrak.org/NORAD/elements/gp.php?GROUP=visual&FORMAT=json',
    'sat_stations.json': 'https://celestrak.org/NORAD/elements/gp.php?GROUP=stations&FORMAT=json',
    'sat_science.json': 'https://celestrak.org/NORAD/elements/gp.php?GROUP=science&FORMAT=json',
    'sat_gnss.json': 'https://celestrak.org/NORAD/elements/gp.php?GROUP=gnss&FORMAT=json',
    'sbdb.json': ('https://ssd-api.jpl.nasa.gov/sbdb_query.api?fields=full_name,diameter,H,epoch,e,a,i,om,w,ma'
                  '&sb-kind=a&sb-cdata=%7B%22AND%22%3A%5B%22diameter%7CGT%7C100%22%5D%7D'),
    'comets.json': ('https://ssd-api.jpl.nasa.gov/sbdb_query.api?fields=full_name,e,q,i,om,w,tp,epoch,M1,K1,per'
                    '&sb-kind=c&sb-cdata=%7B%22AND%22%3A%5B%22q%7CLT%7C4.5%22%5D%7D'),
}
MOONS = {401: 'Phobos', 402: 'Deimos', 501: 'Io', 502: 'Europa', 503: 'Ganymede', 504: 'Callisto',
         601: 'Mimas', 602: 'Enceladus', 603: 'Tethys', 604: 'Dione', 605: 'Rhea', 606: 'Titan', 607: 'Hyperion', 608: 'Iapetus',
         705: 'Miranda', 701: 'Ariel', 702: 'Umbriel', 703: 'Titania', 704: 'Oberon',
         801: 'Triton', 808: 'Proteus', 901: 'Charon'}
MOON_PHYS = {  # mean radius km, typical apparent magnitude
    'Phobos': (11.1, 11.4), 'Deimos': (6.2, 12.5), 'Io': (1821.6, 5.0), 'Europa': (1560.8, 5.3), 'Ganymede': (2634.1, 4.6),
    'Callisto': (2410.3, 5.7), 'Mimas': (198.2, 12.9), 'Enceladus': (252.1, 11.7), 'Tethys': (531.1, 10.2), 'Dione': (561.4, 10.4),
    'Rhea': (763.8, 9.7), 'Titan': (2574.7, 8.3), 'Hyperion': (135, 14.1), 'Iapetus': (734.5, 11.0), 'Miranda': (235.8, 16.5),
    'Ariel': (578.9, 14.4), 'Umbriel': (584.7, 15.0), 'Titania': (788.4, 13.9), 'Oberon': (761.4, 14.1), 'Triton': (1353.4, 13.5),
    'Proteus': (210, 19.7), 'Charon': (606, 16.8)}
GM = {4: 42828.375, 5: 126712764.1, 6: 37940584.8, 7: 5794556.4, 8: 6836527.1, 9: 975.5}  # km^3/s^2, planetary systems
MOON_EPOCH_JD = 2461284.5   # 2026-09-01 00:00


def fetch(name, url, insecure=False):
    path = os.path.join(CACHE, name)
    if os.path.exists(path) and not (REFRESH and (name in LIVE or name.startswith('vec_'))):
        return path
    print('  fetching', name)
    args = ['curl', '-sS', '-g', '-o', path, url]
    if insecure:
        args.insert(1, '-k')          # JPL's chain does not validate on this machine
    subprocess.run(args, check=True)
    return path


def load(name, url, insecure=False):
    with open(fetch(name, url, insecure), encoding='utf-8') as f:
        return json.load(f)


GREEK = {'Alp': 'α', 'Bet': 'β', 'Gam': 'γ', 'Del': 'δ', 'Eps': 'ε', 'Zet': 'ζ', 'Eta': 'η', 'The': 'θ', 'Iot': 'ι', 'Kap': 'κ',
         'Lam': 'λ', 'Mu': 'μ', 'Nu': 'ν', 'Xi': 'ξ', 'Omi': 'ο', 'Pi': 'π', 'Rho': 'ρ', 'Sig': 'σ', 'Tau': 'τ', 'Ups': 'υ',
         'Phi': 'φ', 'Chi': 'χ', 'Psi': 'ψ', 'Ome': 'ω'}
SUP = {'1': '¹', '2': '²', '3': '³', '4': '⁴', '5': '⁵', '6': '⁶', '7': '⁷', '8': '⁸', '9': '⁹'}


def bayer(s):
    if not s:
        return ''
    m = re.match(r'([A-Za-z]+)(?:-(\d))?$', s)
    if not m or m.group(1) not in GREEK:
        return ''
    return GREEK[m.group(1)] + (SUP.get(m.group(2), '') if m.group(2) else '')


def dist_code(pc):
    """distance in parsecs -> 16 bits; 0 means the parallax was too poor to say"""
    if not pc or pc >= 100000 or pc <= 0:
        return 0
    return max(1, min(65535, int(round(math.log10(pc) * 6000)) + 20000))


def build_stars():
    print('stars')
    iau = {int(k): v['name'] for k, v in load('starnames.json', SOURCES['starnames.json']).items() if v.get('name')}
    rows = []
    with open(fetch('hygdata_v41.csv', SOURCES['hygdata_v41.csv']), encoding='utf-8') as f:
        for r in csv.DictReader(f):
            mag = float(r['mag'])
            if mag > 8.0 or r['id'] == '0':
                continue
            rows.append(r)
    rows.sort(key=lambda r: float(r['mag']))
    buf = bytearray()
    names, spectra, spectIdx, variables = [], [], {}, []
    for idx, r in enumerate(rows):
        ra = float(r['ra']) * 15.0
        dec = float(r['dec'])
        mag = float(r['mag'])
        ci = float(r['ci']) if r['ci'] else 0.6
        sp = (r['spect'] or '').strip()
        if sp and sp not in spectIdx:
            spectra.append(sp)
            spectIdx[sp] = len(spectra)          # 1-based; 0 means unknown
        buf += struct.pack('<iiBbHH', int(round(ra * 1e5)), int(round(dec * 1e5)),
                           max(0, min(255, int(round((mag + 2) * 20)))), max(-127, min(127, int(round(ci * 50)))),
                           spectIdx.get(sp, 0), dist_code(float(r['dist']) if r['dist'] else 0))
        hip = int(r['hip']) if r['hip'] else 0
        proper = iau.get(hip) or r['proper']
        by = bayer(r['bayer'])
        fl = r['flam']
        if proper or by or (fl and mag < 6.0):
            names.append([idx, proper or '', by, fl if mag < 6.0 else '', r['con']])
        try:
            lo, hi = float(r['var_max']), float(r['var_min'])       # HYG: var_max is the brighter figure
            if hi - lo >= 0.1:
                variables.append([idx, r['var'] or '', round(lo, 2), round(hi, 2)])
        except (TypeError, ValueError):
            pass
    print('  ', len(rows), 'stars,', len(names), 'designations,', len(spectra), 'spectral types,', len(variables), 'variables')
    return {'stars': base64.b64encode(bytes(buf)).decode('ascii'), 'nstars': len(rows), 'starnames': names,
            'spectra': spectra, 'starvar': variables}


def r2(x):
    return round(x, 2)


def build_constellations():
    print('constellations')
    con = load('constellations.json', SOURCES['constellations.json'])
    lines = load('constellations.lines.json', SOURCES['constellations.lines.json'])
    bounds = load('constellations.bounds.json', SOURCES['constellations.bounds.json'])
    out = {'con': [], 'conlines': {}, 'conbounds': {}}
    for f in con['features']:
        p = f['properties']
        c = f['geometry']['coordinates']
        gen = {'Cru': 'Crucis'}.get(f['id'], p['gen'])       # the source has Crux's genitive wrong
        out['con'].append([f['id'], p['name'], gen, r2(c[0]), r2(c[1]), int(p['rank'])])
    for f in lines['features']:
        out['conlines'][f['id']] = [[[r2(a), r2(b)] for a, b in seg] for seg in f['geometry']['coordinates']]
    for f in bounds['features']:
        out['conbounds'][f['id']] = [[round(a, 3), round(b, 3)] for a, b in f['geometry']['coordinates'][0]]
    return out


def parse_dim(dim):
    try:
        parts = str(dim).lower().replace('′', '').split('x')
        a = float(parts[0])
        b = float(parts[1]) if len(parts) > 1 else a
        return round(a, 1), round(b, 1)
    except (ValueError, IndexError):
        return 0, 0


def wiki_title(ident):
    m = re.match(r'^(M|NGC|IC)\s*(\d+)$', ident)
    if not m:
        return ''
    return {'M': 'Messier_', 'NGC': 'NGC_', 'IC': 'IC_'}[m.group(1)] + m.group(2)


def build_dsos():
    print('deep sky objects')
    dn = load('dsonames.json', SOURCES['dsonames.json'])
    names = {k.replace(' ', ''): v['name'] for k, v in dn.items() if v.get('name') and re.match(r'^(NGC|IC|M|C|Cr|Mel|Sh2|B|LDN)', k)}
    ok = {'oc', 'gc', 'pn', 'bn', 'en', 'rn', 'sfr', 'snr', 's', 'e', 'i', 's0', 'sd', 'g', 'gg'}
    out, seen = [], set()
    for f in load('messier.json', SOURCES['messier.json'])['features']:
        p = f['properties']
        ident = f['id']                      # 'M31'
        key = ident.replace(' ', '')
        seen.add(key)
        seen.add(p['desig'].replace(' ', ''))
        a, b = parse_dim(p['dim'])
        typ = p['type'] if p['type'] in ok else ('oc' if p['type'] == 'pos' else p['type'])
        c = f['geometry']['coordinates']
        out.append([ident, p.get('alt') or '', typ, float(p['mag']) if p['mag'] not in ('', None) else 99, a, b,
                    round(c[0], 4), round(c[1], 4), wiki_title(ident), p['desig']])
    for f in load('dsos.14.json', SOURCES['dsos.14.json'])['features']:
        p = f['properties']
        if p['type'] not in ok:
            continue
        ident = f['id']
        key = ident.replace(' ', '')
        if key in seen:
            continue
        try:
            mag = float(p['mag'])
        except (TypeError, ValueError):
            mag = 99
        a, b = parse_dim(p['dim'])
        if not ((mag <= 10 and a >= 1.5) or key in names):
            continue
        seen.add(key)
        c = f['geometry']['coordinates']
        out.append([ident, names.get(key, ''), p['type'], mag if mag < 99 else 99, a, b, round(c[0], 4), round(c[1], 4), wiki_title(ident), ''])
    print('  ', len(out), 'objects')
    return {'dso': out}


def thin(ring, tol):
    out = [ring[0]]
    for p in ring[1:]:
        q = out[-1]
        if abs(p[0] - q[0]) + abs(p[1] - q[1]) >= tol:
            out.append(p)
    if len(out) > 2 and out[-1] != ring[-1]:
        out.append(ring[-1])
    return out


def build_mw():
    print('milky way')
    mw = load('mw.json', SOURCES['mw.json'])
    out, n = [], 0
    for f in mw['features']:
        polys = []
        for poly in f['geometry']['coordinates']:
            rings = []
            for ring in poly:
                t = thin(ring, 0.35)
                if len(t) >= 4:
                    rings.append([[r2(a), r2(b)] for a, b in t])
                    n += len(t)
            if rings:
                polys.append(rings)
        out.append(polys)
    print('  ', n, 'points')
    return {'mw': out}


def build_planets():
    print('planets')
    p = load('planets.json', SOURCES['planets.json'])
    keys = ['mer', 'ven', 'ter', 'mar', 'jup', 'sat', 'ura', 'nep', 'plu']
    out = {}
    for k in keys:
        e = p[k]['elements'][0]
        out[k] = {kk: e[kk] for kk in ('a', 'e', 'i', 'L', 'W', 'N', 'da', 'de', 'di', 'dL', 'dW', 'dN')}
    return {'planets': out}


def vec_url(mid, planet):
    return ('https://ssd.jpl.nasa.gov/api/horizons.api?format=text&COMMAND=%27{m}%27&OBJ_DATA=%27NO%27&MAKE_EPHEM=%27YES%27'
            '&EPHEM_TYPE=%27VECTORS%27&CENTER=%27500@{p}%27&REF_PLANE=%27FRAME%27&VEC_TABLE=%272%27&OUT_UNITS=%27KM-S%27'
            '&CSV_FORMAT=%27YES%27&TLIST=%27{jd}%27').format(m=mid, p=planet, jd=MOON_EPOCH_JD)


def series_url(mid, planet):
    return ('https://ssd.jpl.nasa.gov/api/horizons.api?format=text&COMMAND=%27{m}%27&OBJ_DATA=%27NO%27&MAKE_EPHEM=%27YES%27'
            '&EPHEM_TYPE=%27VECTORS%27&CENTER=%27500@{p}%27&REF_PLANE=%27FRAME%27&VEC_TABLE=%272%27&OUT_UNITS=%27KM-S%27'
            '&CSV_FORMAT=%27YES%27&START_TIME=%272025-03-01%27&STOP_TIME=%272028-03-01%27&STEP_SIZE=%2715d%27').format(m=mid, p=planet)


def parse_vectors(txt):
    m = re.search(r'\$\$SOE\s*(.*?)\s*\$\$EOE', txt, re.S)
    if not m:
        return []
    out = []
    for ln in m.group(1).strip().split('\n'):
        row = [x.strip() for x in ln.split(',')]
        if len(row) < 8:
            continue
        out.append((float(row[0]), [float(row[2]), float(row[3]), float(row[4])], [float(row[5]), float(row[6]), float(row[7])]))
    return out


def vdot(a, b):
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]


def vcross(a, b):
    return [a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0]]


def build_moons():
    """Keplerian elements from the epoch state vector (a, e, orientation), with the mean motion and
    epoch mean anomaly fitted by least squares to three years of Horizons positions. The fit absorbs
    the oblateness term that a plain GM mean motion misses - for Io that is a quarter turn a year."""
    print('moons')
    out = []
    for mid, name in MOONS.items():
        planet = (mid // 100) * 100 + 99
        anchor = parse_vectors(open(fetch('vec_%d.txt' % mid, vec_url(mid, planet), insecure=True), encoding='utf-8').read())
        series = parse_vectors(open(fetch('ser_%d.txt' % mid, series_url(mid, planet), insecure=True), encoding='utf-8').read())
        if not anchor or len(series) < 10:
            print('   no vectors for', name)
            continue
        jd0, r, v = anchor[0]
        mu = GM[mid // 100]
        rn = math.sqrt(vdot(r, r))
        v2 = vdot(v, v)
        a = 1.0 / (2.0 / rn - v2 / mu)
        h = vcross(r, v)
        hn = math.sqrt(vdot(h, h))
        hh = [x / hn for x in h]
        rv = vdot(r, v)
        evec = [((v2 - mu / rn) * r[k] - rv * v[k]) / mu for k in range(3)]
        e = math.sqrt(vdot(evec, evec))
        pp = [x / e for x in evec] if e > 1e-6 else [x / rn for x in r]
        qq = vcross(hh, pp)
        n_kep = math.sqrt(mu / a ** 3) * 86400 * 180 / math.pi

        def mean_anomaly(rvec):
            x, y = vdot(rvec, pp), vdot(rvec, qq)
            nu = math.atan2(y, x)
            E = 2 * math.atan(math.sqrt((1 - e) / (1 + e)) * math.tan(nu / 2))
            return math.degrees(E - e * math.sin(E))

        ts, Ms = [], []
        prev_t, prev_M, turns = None, None, 0
        for (t, rr, vv) in series:
            M = mean_anomaly(rr)
            if prev_t is not None:
                expected = prev_M + n_kep * (t - prev_t)
                turns += round((expected - (M + turns * 360)) / 360)
            ts.append(t - jd0)
            Ms.append(M + turns * 360)
            prev_t, prev_M = t, M + turns * 360
        N = len(ts)
        st, sM = sum(ts), sum(Ms)
        stt = sum(t * t for t in ts)
        stM = sum(t * M for t, M in zip(ts, Ms))
        n = (N * stM - st * sM) / (N * stt - st * st)
        M0 = (sM - n * st) / N
        resid = max(abs(M - (M0 + n * t)) for t, M in zip(ts, Ms))
        radius, mag = MOON_PHYS[name]
        print('   %-10s a=%9.0f km  e=%.4f  n=%.6f deg/d (Kepler %.6f)  fit residual %.2f deg' % (name, a, e, n, n_kep, resid))
        out.append({'name': name, 'planet': {4: 'mar', 5: 'jup', 6: 'sat', 7: 'ura', 8: 'nep', 9: 'plu'}[mid // 100],
                    'a': round(a, 1), 'e': round(e, 6), 'n': round(n, 8), 'M0': round(M0 % 360, 5),
                    'p': [round(x, 7) for x in pp], 'q': [round(x, 7) for x in qq], 'jd0': jd0, 'R': radius, 'mag': mag})
    return {'moons': out}


TNO = {  # diameter km (literature), H; elements come from SBDB
    'Eris': (2326, -1.26), 'Makemake': (1430, -0.25), 'Haumea': (1560, 0.14), 'Gonggong': (1230, 1.82),
    'Quaoar': (1090, 2.41), 'Sedna': (995, 1.50), 'Orcus': (910, 2.13)}


def build_asteroids():
    print('asteroids')
    d = load('sbdb.json', LIVE['sbdb.json'], insecure=True)
    out = []
    for row in d['data']:
        full, diam, H, epoch, e, a, i, om, w, ma = row[:10]
        m = re.match(r'^\s*(\d+)\s+(.*?)\s*(\(.*\))?\s*$', full)
        num, name = (m.group(1), m.group(2).strip()) if m else ('', full.strip())
        if not name and m and m.group(3):
            name = m.group(3).strip('() ')
        out.append([int(num) if num else 0, name, float(diam), float(H) if H else 10, float(epoch), float(e), float(a), float(i), float(om), float(w), float(ma)])
    have = set(r[1] for r in out)
    for name, (diam, H) in TNO.items():
        if name in have:
            continue
        j = load('sbdb_%s.json' % name, 'https://ssd-api.jpl.nasa.gov/sbdb.api?sstr=' + name + '&full-prec=1', insecure=True)
        el = {x['name']: float(x['value']) for x in j['orbit']['elements']}
        m = re.match(r'^\s*(\d+)', j['object']['fullname'])
        out.append([int(m.group(1)) if m else 0, name, diam, H, float(j['orbit']['epoch']), el['e'], el['a'], el['i'], el['om'], el['w'], el['ma']])
    out.sort(key=lambda r: -r[2])
    print('  ', len(out), 'asteroids and dwarf planets over 100 km')
    return {'asteroids': out}


def build_comets():
    """Comets that could come within reach of a small telescope, with their orbits as
    perihelion distance and time rather than a mean anomaly. Long-period comets are kept only
    while their perihelion passage is near the present; short-period ones propagate from any
    recent apparition."""
    print('comets')
    d = load('comets.json', LIVE['comets.json'], insecure=True)
    F = {n: i for i, n in enumerate(d['fields'])}
    import datetime
    now_jd = datetime.datetime.now(datetime.timezone.utc).timestamp() / 86400 + 2440587.5
    out = []
    for r in d['data']:
        if not r[F['M1']]:
            continue
        e, q, tp = float(r[F['e']]), float(r[F['q']]), float(r[F['tp']])
        per = float(r[F['per']]) / 365.25 if r[F['per']] else None
        if e < 1 and per and per < 200:
            if abs(tp - now_jd) / 365.25 > 60:
                continue
        elif abs(tp - now_jd) / 365.25 > 4:
            continue
        M1 = float(r[F['M1']])
        K1 = float(r[F['K1']]) if r[F['K1']] else 10.0
        if M1 + 5 * math.log10(max(q - 0.7, 0.1)) + K1 * math.log10(q) > 13:
            continue
        name = r[F['full_name']].strip()
        out.append([name, round(e, 6), round(q, 6), round(float(r[F['i']]), 4), round(float(r[F['om']]), 4),
                    round(float(r[F['w']]), 4), round(tp, 5), round(M1, 2), round(K1, 2)])
    out.sort(key=lambda c: c[0])
    print('  ', len(out), 'comets')
    return {'comets': out}


# Major visual meteor showers: radiant (J2000 degrees) at the peak, the peak's solar longitude,
# the radiant's daily drift in degrees per degree of solar longitude, the meteors' speed in km/s
# and the zenithal hourly rate. Values follow the IAU Meteor Data Center shower list and the
# International Meteor Organization's working list of visual showers; -1 marks a variable rate.
SHOWERS = [
    # code, name, ra, dec, sol.long, drift ra, drift dec, km/s, zhr, from, to, parent
    ['QUA', 'Quadrantids', 230.0, 49.0, 283.15, 0.56, -0.25, 41, 110, 281.0, 285.5, '(196256) 2003 EH1'],
    ['ACE', 'Alpha Centaurids', 210.0, -59.0, 319.2, 1.90, -0.50, 56, 6, 315.0, 325.0, ''],
    ['GNO', 'Gamma Normids', 239.0, -50.0, 353.0, 0.90, -0.25, 56, 6, 340.0, 5.0, ''],
    ['LYR', 'April Lyrids', 271.0, 34.0, 32.32, 0.66, 0.02, 49, 18, 29.0, 35.0, 'C/1861 G1 Thatcher'],
    ['PPU', 'Pi Puppids', 110.0, -45.0, 33.5, 0.40, -0.10, 18, -1, 30.0, 38.0, '26P/Grigg-Skjellerup'],
    ['ETA', 'Eta Aquariids', 338.0, -1.0, 45.5, 0.92, 0.37, 66, 50, 35.0, 60.0, '1P/Halley'],
    ['ELY', 'Eta Lyrids', 291.0, 43.0, 50.0, 0.56, 0.14, 43, 3, 44.0, 55.0, 'C/1983 H1 IRAS-Araki-Alcock'],
    ['JBO', 'June Bootids', 224.0, 48.0, 95.7, 0.40, -0.20, 18, -1, 91.0, 100.0, '7P/Pons-Winnecke'],
    ['CAP', 'Alpha Capricornids', 307.0, -10.0, 127.0, 0.97, 0.24, 23, 5, 110.0, 140.0, '169P/NEAT'],
    ['SDA', 'Southern Delta Aquariids', 340.0, -16.0, 127.0, 0.75, 0.21, 41, 25, 105.0, 145.0, '96P/Machholz'],
    ['PER', 'Perseids', 48.0, 58.0, 140.0, 1.40, 0.26, 59, 100, 122.0, 145.5, '109P/Swift-Tuttle'],
    ['KCG', 'Kappa Cygnids', 286.0, 59.0, 145.0, 0.40, 0.05, 25, 3, 138.0, 153.0, ''],
    ['AUR', 'Aurigids', 91.0, 39.0, 158.6, 1.24, -0.01, 66, 6, 155.0, 162.0, 'C/1911 N1 Kiess'],
    ['SPE', 'September Epsilon Perseids', 47.0, 40.0, 166.7, 1.17, 0.26, 64, 5, 160.0, 172.0, ''],
    ['DRA', 'October Draconids', 262.0, 54.0, 195.4, 0.34, -0.05, 20, -1, 194.5, 196.5, '21P/Giacobini-Zinner'],
    ['STA', 'Southern Taurids', 52.0, 15.0, 197.0, 0.82, 0.29, 27, 5, 170.0, 230.0, '2P/Encke'],
    ['ORI', 'Orionids', 95.0, 16.0, 208.0, 1.03, -0.05, 66, 20, 195.0, 220.0, '1P/Halley'],
    ['NTA', 'Northern Taurids', 58.0, 22.0, 230.0, 1.03, 0.26, 29, 5, 200.0, 245.0, '2P/Encke'],
    ['LEO', 'Leonids', 152.0, 22.0, 235.27, 0.99, -0.36, 71, 15, 230.0, 241.0, '55P/Tempel-Tuttle'],
    ['NOO', 'November Orionids', 91.0, 16.0, 246.0, 1.03, -0.01, 41, 3, 240.0, 254.0, ''],
    ['PHO', 'Phoenicids', 18.0, -53.0, 250.0, 0.80, -0.20, 18, -1, 246.0, 256.0, '289P/Blanpain'],
    ['MON', 'December Monocerotids', 100.0, 8.0, 257.0, 0.97, -0.09, 41, 3, 245.0, 265.0, ''],
    ['HYD', 'Sigma Hydrids', 125.0, 2.0, 257.0, 0.92, -0.28, 58, 7, 245.0, 270.0, ''],
    ['GEM', 'Geminids', 112.0, 33.0, 262.2, 1.15, -0.16, 35, 150, 255.0, 266.0, '(3200) Phaethon'],
    ['COM', 'Comae Berenicids', 175.0, 18.0, 264.0, 0.96, -0.39, 65, 3, 250.0, 280.0, ''],
    ['DLM', 'December Leonis Minorids', 161.0, 30.0, 268.0, 0.86, 0.43, 64, 5, 255.0, 295.0, ''],
    ['URS', 'Ursids', 217.0, 76.0, 270.7, 0.05, -0.31, 33, 10, 268.0, 274.0, '8P/Tuttle'],
]


def build_showers():
    print('meteor showers')
    print('  ', len(SHOWERS), 'showers')
    return {'showers': SHOWERS}


SAT_FIELDS = ['OBJECT_NAME', 'OBJECT_ID', 'EPOCH', 'MEAN_MOTION', 'ECCENTRICITY', 'INCLINATION', 'RA_OF_ASC_NODE',
              'ARG_OF_PERICENTER', 'MEAN_ANOMALY', 'EPHEMERIS_TYPE', 'CLASSIFICATION_TYPE', 'NORAD_CAT_ID', 'ELEMENT_SET_NO',
              'REV_AT_EPOCH', 'BSTAR', 'MEAN_MOTION_DOT', 'MEAN_MOTION_DDOT']


def build_sats():
    print('satellites')
    groups = {}
    for g in ('visual', 'stations', 'science', 'gnss'):
        rows = load('sat_%s.json' % g, LIVE['sat_%s.json' % g])
        groups[g] = [{k: r[k] for k in SAT_FIELDS} for r in rows]
        print('  ', g, len(rows))
    import datetime
    return {'sats': {'fetched': datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M UTC'), 'groups': groups}}


def build_cities():
    print('cities')
    wc = os.path.join(HERE, '..', '..', 'world-clock-site', 'index.html')
    s = open(wc, encoding='utf-8').read()
    i = s.find('window.WTZ_DATA=')
    j = s.find('</script>', i)
    d = json.loads(s[i + len('window.WTZ_DATA='):j].strip().rstrip(';'))
    cities = [[c[0], c[1], c[2], c[3], c[4], c[5]] for c in d['cities']]
    return {'cities': cities}


def main():
    data = {}
    for fn in (build_stars, build_constellations, build_dsos, build_mw, build_planets, build_moons, build_asteroids,
               build_comets, build_showers, build_sats, build_cities):
        data.update(fn())
    payload = json.dumps(data, ensure_ascii=False, separators=(',', ':'))
    payload = payload.replace('</', '<\\/')
    block = '<!--CG_DATA_START-->\n<script>\nwindow.CG_DATA=' + payload + ';\n</script>\n<!--CG_DATA_END-->'
    html = open(INDEX, encoding='utf-8').read()
    pat = re.compile(r'<!--CG_DATA_START-->.*?<!--CG_DATA_END-->', re.S)
    if not pat.search(html):
        raise SystemExit('index.html has no CG_DATA markers')
    html = pat.sub(lambda m: block, html)
    open(INDEX, 'w', encoding='utf-8', newline='\n').write(html)
    print('data block: %.0f KB; index.html: %.0f KB' % (len(payload.encode('utf-8')) / 1024, len(html.encode('utf-8')) / 1024))


if __name__ == '__main__':
    main()
