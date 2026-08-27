#!/usr/bin/env python3
"""
cont_v3.py — continuation-override screen (Kenneth).

Entry = a TRIGGER LEVEL ABOVE price: the nearest overhead resistance the stock
must reclaim to continue. Never a demand-zone limit below price.

v3 fixes vs v2:
  * trigger = NEAREST overhead level (min of pivot highs above spot, 10d high,
    20d high) — v2 took the most recent pivot, which was often the highest and
    blew the stop out past 3 ATR.
  * stop = most recent swing low (finer k=2 pivots), risk capped at 3.5 ATR.
"""
import csv, glob, os

def load(p):
    out = []
    with open(p) as f:
        for r in csv.DictReader(f):
            try: out.append((r['Date'], float(r['Open']), float(r['High']),
                             float(r['Low']), float(r['Close'])))
            except (ValueError, KeyError): pass
    return out

def sma(v,n): return [None]*(n-1)+[sum(v[i-n+1:i+1])/n for i in range(n-1,len(v))]

def atr_series(bars,n=14):
    tr=[]
    for i,b in enumerate(bars):
        if i==0: tr.append(b[2]-b[3]); continue
        pc=bars[i-1][4]; tr.append(max(b[2]-b[3],abs(b[2]-pc),abs(b[3]-pc)))
    return [None]*(n-1)+[sum(tr[i-n+1:i+1])/n for i in range(n-1,len(tr))]

def pivots(bars,k):
    hi,lo=[],[]
    for i in range(k,len(bars)-k):
        w=bars[i-k:i+k+1]
        if bars[i][2]==max(x[2] for x in w): hi.append(i)
        if bars[i][3]==min(x[3] for x in w): lo.append(i)
    return hi,lo

def scan(path):
    sym=os.path.basename(path).replace('.csv','')
    bars=load(path)
    if len(bars)<60: return None
    C=[b[4] for b in bars]; H=[b[2] for b in bars]; L=[b[3] for b in bars]; n=len(bars)
    s20,s50=sma(C,20),sma(C,50); s100=sma(C,100) if n>=100 else [None]*n
    A=atr_series(bars); spot,atr=C[-1],A[-1]
    if atr is None or s50[-1] is None: return None
    lm = s100[-1] if s100[-1] is not None else s50[-1]

    # 1) confirmed uptrend: MAs stacked, price above the long MA
    if not (spot > lm and s50[-1] > lm*0.99 and spot > s50[-1]*0.94): return None
    # 2) not extended / no chasing
    ext_atr=(spot-s20[-1])/atr; ext50=(spot/s50[-1]-1)*100
    if ext_atr > 2.2 or ext50 > 12.0: return None
    # 3) contraction present
    look=min(126,n-15); ap=[A[i]/C[i]*100 for i in range(n-look,n) if A[i]]
    atrpct=atr/spot*100
    atr_pctl=sum(1 for x in ap if x<atrpct)/len(ap)
    b1=max(H[-20:])-min(L[-20:]); b2=max(H[-40:-20])-min(L[-40:-20])
    rcomp=b1/b2 if b2 else 9.9
    if atr_pctl>0.75 and rcomp>=1.15: return None

    # 4) TRIGGER = nearest overhead resistance
    ph3,_=pivots(bars,3); ph2,pl2=pivots(bars,2)
    levels=[H[i] for i in set(ph3+ph2) if i>=n-70 and H[i]>spot*1.002]
    for w in (10,20):
        h=max(H[-w:])
        if h>spot*1.002: levels.append(h)
    if not levels: return None
    trig=min(levels)                       # the first wall overhead
    if trig/spot-1 > 0.10: return None     # must be a reachable alert

    # 5) stop under the most recent swing low
    rp=[i for i in pl2 if i>=n-25]
    hl=L[max(rp)] if rp else min(L[-10:])
    hl=min(hl,min(L[-3:]))
    stop=hl-0.25*atr
    risk=trig-stop
    if risk<=0: return None
    if not (0.8 <= risk/atr <= 3.0): return None

    # higher-low structure check
    prior=[L[i] for i in pl2 if i < n-25]
    higher_low = (hl > min(prior[-10:])) if len(prior)>=3 else True

    # 6) projected target: measured move of the impulse leg, floored by prior high + ATR
    base_low=min(L[-20:]); base_h=trig-base_low
    prior_high=max(C[-120:]) if n>=120 else max(C)   # highest CLOSE: robust to rejection wicks
    t1 = prior_high+0.5*atr if trig < prior_high*0.998 else trig+base_h
    t2 = t1 + base_h
    target=t1; rr=(t1-trig)/risk; rr2=(t2-trig)/risk
    if rr < 2.0: return None
    score=0
    score += 2 if ext50<4 else (1 if ext50<7 else 0)
    score += 2 if rr>=3 else 1
    score += 2 if (s100[-1] and spot>s100[-1] and s50[-1]>s100[-1]) else 1
    score += 2 if higher_low else 0
    score += 1 if (atr_pctl<=0.35 or rcomp<=0.85) else 0

    return dict(sym=sym,asof=bars[-1][0],spot=round(spot,2),trig=round(trig,2),
        dist=round((trig/spot-1)*100,1),stop=round(stop,2),risk=round(risk,2),
        risk_atr=round(risk/atr,2),target=round(t1,2),t2=round(t2,2),rr=round(rr,2),rr2=round(rr2,2),score=score,
        atr_pctl=round(atr_pctl,2),rcomp=round(rcomp,2),ext50=round(ext50,1),
        atrpct=round(atrpct,2),hl=higher_low,base_h=round(base_h,2),prior_high=round(prior_high,2))

rows=[r for r in (scan(p) for p in sorted(glob.glob('/home/user/swing-idea-engine/work/csv/*.csv'))) if r]
rows.sort(key=lambda r:(-r['score'],-r['rr']))
h=f"{'SYM':6}{'asof':11}{'spot':>9}{'TRIG':>9}{'d%':>6}{'stop':>9}{'risk':>7}{'xATR':>6}{'T1':>10}{'R:R':>6}{'T2':>10}{'R2':>6}{'core':>5}{'atrP':>6}{'rcmp':>6}{'ex50':>6}{'HL':>4}"
print(h); print('-'*len(h))
for r in rows:
    print(f"{r['sym']:6}{r['asof']:11}{r['spot']:>9}{r['trig']:>9}{r['dist']:>6}{r['stop']:>9}"
          f"{r['risk']:>7}{r['risk_atr']:>6}{r['target']:>10}{r['rr']:>6}{r['t2']:>10}{r['rr2']:>6}{r['score']:>5}"
          f"{r['atr_pctl']:>6}{r['rcomp']:>6}{r['ext50']:>6}{'Y' if r['hl'] else 'n':>4}")
print(f"\n{len(rows)} pass of {len(glob.glob('/home/user/swing-idea-engine/work/csv/*.csv'))} scanned")
