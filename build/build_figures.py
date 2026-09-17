import csv, json, os, re, shutil, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(HERE, 'cache', 'figures')
OUT = os.path.join(HERE, '..', 'figures')
PAGE = os.path.join(HERE, '..', 'index.html')
HYG = os.path.join(HERE, 'cache', 'hygdata_v41.csv')
BASE = 'https://raw.githubusercontent.com/Stellarium/stellarium-skycultures/master/western/'
START, END = '/*CG_FIGURES_START*/', '/*CG_FIGURES_END*/'

def get(name, refresh):
    dest = os.path.join(CACHE, os.path.basename(name))
    if refresh or not os.path.exists(dest):
        subprocess.run(['curl', '-s', '-f', '-o', dest, BASE + name], check=True)
    return dest

def main():
    refresh = '--refresh' in sys.argv
    os.makedirs(CACHE, exist_ok=True)
    os.makedirs(OUT, exist_ok=True)
    index = json.load(open(get('index.json', refresh), encoding='utf-8'))
    hip = {}
    with open(HYG, encoding='utf-8') as f:
        for r in csv.DictReader(f):
            if r['hip']:
                hip[int(r['hip'])] = (float(r['ra']) * 15, float(r['dec']))
    figs = []
    for con in index['constellations']:
        im = con.get('image')
        if not im:
            continue
        pts = []
        for a in im['anchors']:
            if a['hip'] not in hip:
                pts = None
                break
            ra, dec = hip[a['hip']]
            pts.append([a['pos'][0], a['pos'][1], round(ra, 4), round(dec, 4)])
        if not pts:
            print('skipped, anchor star not in HYG:', con['id'])
            continue
        src = get(im['file'], refresh)
        name = os.path.basename(im['file'])
        shutil.copyfile(src, os.path.join(OUT, name))
        figs.append({'id': con['id'].split()[-1], 'f': name, 'w': im['size'][0], 'h': im['size'][1], 'a': pts})
    block = START + 'window.CG_FIGURES=' + json.dumps(figs, separators=(',', ':')) + ';' + END
    page = open(PAGE, encoding='utf-8', newline='').read()
    if START not in page:
        sys.exit('the CG_FIGURES markers are not in index.html')
    page = re.sub(re.escape(START) + '.*?' + re.escape(END), lambda m: block, page, flags=re.S)
    open(PAGE, 'w', encoding='utf-8', newline='').write(page)
    print(len(figs), 'figures,', len(block), 'bytes in the page,',
          sum(os.path.getsize(os.path.join(OUT, f['f'])) for f in figs), 'bytes of pictures')

main()
