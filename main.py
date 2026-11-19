import json,os,sys,urllib.request,urllib.error
U=os.environ.get("MAKEFUN_ENV_URL") or sys.exit(1)
V=[0,100,320,330,500,900,0]
ND=(14,18,31,33,-14,-18,-31,-33);KD=(1,15,16,17,-1,-15,-16,-17)
BD=(15,17,-15,-17);RD=(1,16,-1,-16)
Z=[];x=987654321
for _ in range(1561):
 x=(x*6364136223846793005+1442695040888963407)&0xFFFFFFFFFFFFFFFF;Z.append(x)
b=[0]*128;sd=0;cs=0;ep=-1;hf=0;hs=0;KS=[4,116]
T={};KL=[[0,0] for _ in range(64)];PH=set()
N=0;BUD=80000;MATE=100000
class AB(Exception):pass
def zi(p):return (abs(p)-1)*2+(p<0)
def sqn(s):return "abcdefgh"[s&7]+str((s>>4)+1)
def uci(m):
 s=sqn(m&127)+sqn(m>>7&127);p=m>>14
 return s+("nbrq"[p-2] if p else "")
def parse(f):
 global b,sd,cs,ep,hf,hs,KS,CNT
 p=f.split();b=[0]*128;hs=0
 for i,r in enumerate(p[0].split("/")):
  q=0
  for c in r:
   if c.isdigit():q+=int(c)
   else:
    v="PNBRQK".index(c.upper())+1
    if c.islower():v=-v
    s=(7-i)*16+q;b[s]=v;hs^=Z[zi(v)*128+s];q+=1
 sd=0 if p[1]=="w" else 1
 cs=0
 for c in p[2]:
  if c=="K":cs|=1
  elif c=="Q":cs|=2
  elif c=="k":cs|=4
  elif c=="q":cs|=8
 ep=-1 if p[3]=="-" else (ord(p[3][0])-97)+(int(p[3][1])-1)*16
 hf=int(p[4]);hs^=Z[1537+cs]
 if ep>=0:hs^=Z[1553+(ep&7)]
 if sd:hs^=Z[1536]
 KS=[0,0]
 for s in range(128):
  if b[s]==6:KS[0]=s
  elif b[s]==-6:KS[1]=s
 CNT=sum(1 for s in range(128) if b[s] and abs(b[s])>1 and abs(b[s])<6)
def atk(s,w):
 if w:
  for d in (-15,-17):
   t=s+d
   if not t&0x88 and b[t]==1:return 1
 else:
  for d in (15,17):
   t=s+d
   if not t&0x88 and b[t]==-1:return 1
 for d in ND:
  t=s+d
  if not t&0x88 and b[t]==(2 if w else -2):return 1
 for d in KD:
  t=s+d
  if not t&0x88 and b[t]==(6 if w else -6):return 1
 for d in BD:
  t=s+d
  while not t&0x88:
   p=b[t]
   if p:
    if p==(3 if w else -3) or p==(5 if w else -5):return 1
    break
   t+=d
 for d in RD:
  t=s+d
  while not t&0x88:
   p=b[t]
   if p:
    if p==(4 if w else -4) or p==(5 if w else -5):return 1
    break
   t+=d
 return 0
def gen(cap):
 ms=[]
 for s in range(128):
  if s&0x88:continue
  p=b[s]
  if not p or (p>0)==bool(sd):continue
  w=p>0;t=abs(p)
  if t==1:
   d=16 if w else -16;one=s+d
   if not one&0x88 and not b[one]:
    if (one>>4)==(7 if w else 0):
     for pr in (2,3,4,5):ms.append(s|(one<<7)|(pr<<14))
    else:
     ms.append(s|(one<<7))
     two=s+2*d
     if ((s>>4)==(1 if w else 6)) and not b[two]:ms.append(s|(two<<7))
   for dd in (d-1,d+1):
    to=s+dd
    if to&0x88:continue
    q=b[to]
    if q and (q>0)!=w:
     if (to>>4)==(7 if w else 0):
      for pr in (2,3,4,5):ms.append(s|(to<<7)|(pr<<14))
     else:ms.append(s|(to<<7))
    elif to==ep and ep>=0:ms.append(s|(to<<7))
  elif t==2 or t==6:
   for d in (ND if t==2 else KD):
    to=s+d
    if to&0x88:continue
    q=b[to]
    if not q or (q>0)!=w:ms.append(s|(to<<7))
   if t==6:
    if w and s==4:
     if cs&1 and not b[5] and not b[6] and b[7]==4 and not atk(4,0) and not atk(5,0) and not atk(6,0):ms.append(4|(6<<7))
     if cs&2 and not b[3] and not b[2] and not b[1] and b[0]==4 and not atk(4,0) and not atk(3,0) and not atk(2,0):ms.append(4|(2<<7))
    elif not w and s==116:
     if cs&4 and not b[117] and not b[118] and b[119]==-4 and not atk(116,1) and not atk(117,1) and not atk(118,1):ms.append(116|(118<<7))
     if cs&8 and not b[115] and not b[114] and not b[113] and b[112]==-4 and not atk(116,1) and not atk(115,1) and not atk(114,1):ms.append(116|(114<<7))
  else:
   for d in (BD if t==3 else RD if t==4 else BD+RD):
    to=s+d
    while not to&0x88:
     q=b[to]
     if not q:ms.append(s|(to<<7))
     else:
      if (q>0)!=w:ms.append(s|(to<<7))
      break
     to+=d
 if cap:
  return [m for m in ms if b[(m>>7)&127] or (m>>14) or (m>>7)&127==ep]
 return ms
def make(m):
 global cs,ep,hf,sd,hs,CNT
 f=m&127;t=m>>7&127;pr=m>>14;p=b[f];w=p>0;cap=b[t];cq=-1
 o=cs;e0=ep;h0=hf;s0=hs;k0=KS[0];k1=KS[1]
 if abs(p)==1 and t==ep and ep>=0:
  cq=t-16 if w else t+16;cap=b[cq];b[cq]=0;hs^=Z[zi(cap)*128+cq]
 if cap and abs(cap)>1:CNT-=1
 if pr:CNT+=1
 hs^=Z[zi(p)*128+f]
 if cap:hs^=Z[zi(cap)*128+t]
 b[f]=0;q=pr*(1 if w else -1) if pr else p;b[t]=q;hs^=Z[zi(q)*128+t]
 if abs(p)==6:
  KS[0 if w else 1]=t
  if abs(t-f)==2:
   rs,rd=(7,5) if t>f else (0,3)
   if not w:rs+=112;rd+=112
   r=b[rs];b[rs]=0;b[rd]=r;hs^=Z[zi(r)*128+rs];hs^=Z[zi(r)*128+rd]
 if f==4:cs&=~3
 elif f==116:cs&=~12
 elif f==0:cs&=~2
 elif f==7:cs&=~1
 elif f==112:cs&=~8
 elif f==119:cs&=~4
 if t==0:cs&=~2
 elif t==7:cs&=~1
 elif t==112:cs&=~8
 elif t==119:cs&=~4
 if cs!=o:hs^=Z[1537+o];hs^=Z[1537+cs]
 if ep>=0:hs^=Z[1553+(ep&7)]
 ep=f+16 if p==1 and t-f==32 else f-16 if p==-1 and f-t==32 else -1
 if ep>=0:hs^=Z[1553+(ep&7)]
 hf=0 if abs(p)==1 or cap else hf+1
 sd^=1;hs^=Z[1536]
 return (f,t,pr,cap,cq,o,e0,h0,s0,k0,k1)
def unmake(u):
 global cs,ep,hf,sd,hs,KS,CNT
 f,t,pr,cap,cq,cs,ep,hf,hs,KS[0],KS[1]=u
 p=b[t];w=p>0
 if cap and abs(cap)>1:CNT+=1
 if pr:CNT-=1
 b[t]=0;b[f]=pr and 0 or p
 if pr:b[f]=1 if w else -1
 if abs(p)==6 and abs(t-f)==2:
  rs,rd=(7,5) if t>f else (0,3)
  if not w:rs+=112;rd+=112
  b[rs]=b[rd];b[rd]=0
 if cq>=0:b[cq]=cap
 elif cap:b[t]=cap
 sd^=1
def ev():
 s=0;ph=0;km=0;ke=0;np=0;mn=0;rq=0;nk=0;bc=0;bp=[0,0]
 for q in range(128):
  if q&0x88:continue
  p=b[q]
  if not p:continue
  t=abs(p);w=p>0;f=q&7;r=q>>4;rr=r if w else 7-r
  v=V[t];c=(7-abs(2*f-7)-abs(2*r-7))
  if t==1:
   np+=1;v+=6*rr+(6 if f in (3,4) else 2 if f in (2,5) else 0)
  elif t==2:nk+=1;mn+=1;ph+=1;v+=c*3
  elif t==3:mn+=1;ph+=1;v+=c*2;bp[0 if w else 1]+=1;bc|=1<<((q&1)^((q>>4)&1))
  elif t==4:rq+=1;ph+=2;v+=12 if rr==6 else 0
  elif t==5:rq+=1;ph+=4;v+=c
  elif t==6:
   mg=-10*rr+(10 if q in (2,6,114,118) else 0);eg=c*4
   if w:km+=mg;ke+=eg
   else:km-=mg;ke-=eg
   continue
  s+=v if w else -v
 if np==0 and rq==0 and mn<=1:return 0
 if np==0 and rq==0 and nk==0 and bc in (1,2):return 0
 s+=28*(bp[0]-bp[1])
 if ph>24:ph=24
 s+=(km*ph+ke*(24-ph))//24
 return s if sd==0 else -s
def order(ms,ttm,pl):
 def k(m):
  if m==ttm:return 1<<20
  t=m>>7&127;v=b[t]
  if v:return 10000+V[abs(v)]*10-V[abs(b[m&127])]
  if m>>14:return 9000
  if m==KL[pl][0]:return 5000
  if m==KL[pl][1]:return 4000
  return 0
 ms.sort(key=k,reverse=True);return ms
def qs(a,be,pl):
 global N
 N+=1
 if N>BUD:raise AB
 if hf>=100:return 0
 ck=atk(KS[sd],sd)
 if ck:
  bes=-MATE
  if pl>10:
   for m in gen(0):
    u=make(m)
    if atk(KS[sd^1],1-sd):unmake(u);continue
    unmake(u);return ev()-50
   return -MATE+pl
  for m in order(gen(0),0,pl):
   u=make(m)
   if atk(KS[sd^1],1-sd):unmake(u);continue
   v=-qs(-be,-a,pl+1);unmake(u)
   if v>bes:bes=v
   if v>a:a=v
   if a>=be:return be
  return bes if bes>-MATE else -MATE+pl
 st=ev()
 if st>=be:return be
 if st>a:a=st
 if pl>16:return a
 for m in order(gen(1),0,pl):
  t=(m>>7)&127
  if st+V[abs(b[t])]+(900 if m>>14 else 0)+150<a:continue
  u=make(m)
  if atk(KS[sd^1],1-sd):unmake(u);continue
  v=-qs(-be,-a,pl+1);unmake(u)
  if v>=be:return be
  if v>a:a=v
 return a
def null():
 global ep,hf,sd,hs
 u=(ep,hf,hs)
 if ep>=0:hs^=Z[1553+(ep&7)]
 ep=-1;hf+=1;sd^=1;hs^=Z[1536]
 return u
def unnull(u):
 global ep,hf,sd,hs
 ep,hf,hs=u;sd^=1
CNT=14
def sr(a,be,d,pl):
 global N
 N+=1
 if N>BUD:raise AB
 if hf>=100:return 0
 if hs in PH:return 0
 e=T.get(hs)
 if e and e[0]>=d:
  if e[1]==0:return e[2]
  if e[1]==1 and e[2]>=be:return e[2]
  if e[1]==2 and e[2]<=a:return e[2]
 if d<=0:return qs(a,be,pl)
 PH.add(hs)
 try:
  ck=atk(KS[sd],sd);al=a;bes=-MATE;bm=0;fl=2
  if d>=3 and not ck and CNT>=2:
   u2=null();v=-sr(-be,-be+1,d-3,pl+1);unnull(u2)
   if v>=be:return be
  ms=order(gen(0),e[3] if e else 0,pl)
  for i,m in enumerate(ms):
   t=(m>>7)&127;quiet=not b[t] and not(m>>14) and t!=ep
   u=make(m)
   if atk(KS[sd^1],1-sd):unmake(u);continue
   if d>=3 and i>=3 and quiet and not ck:
    v=-sr(-be,-al,d-2,pl+1)
    if v>al:v=-sr(-be,-al,d-1,pl+1)
   else:
    v=-sr(-be,-al,d-1,pl+1)
   unmake(u)
   if v>bes:bes=v;bm=m
   if v>al:al=v
   if al>=be:
    if quiet:KL[pl][1]=KL[pl][0];KL[pl][0]=m
    fl=1;break
  if bes==-MATE:return -MATE+pl if ck else 0
  if bes<=a:fl=2
  elif bes>=be:fl=1
  else:fl=0
  T[hs]=(d,fl,bes,bm)
  return bes
 finally:PH.discard(hs)
def root(d,best):
 global N
 ms=order([pm(m) for m in RT],best,0)
 bes=-MATE;bm=ms[0];a=-MATE
 for m in ms:
  u=make(m);v=-sr(-MATE,MATE,d-1,1);unmake(u)
  if v>bes:bes=v;bm=m
  if v>a:a=v
 return bes,bm
def pm(u):
 f=(ord(u[0])-97)+(int(u[1])-1)*16;t=(ord(u[2])-97)+(int(u[3])-1)*16
 pr="nbrq".index(u[4])+2 if len(u)==5 else 0
 return f|(t<<7)|(pr<<14)
RT=[]
def choose(fen,legal):
 global N,RT,BUD
 parse(fen)
 if len(legal)==1:return legal[0]
 RT=legal;bes=0;best=pm(legal[0])
 for d in range(1,21):
  N=0;PH.clear();PH.add(hs);BUD=300000 if d==1 else 80000
  try:
   _,bm=root(d,best);best=bm
  except AB:break
 return uci(best)
def post(p,d):
 r=urllib.request.Request(U+p,data=json.dumps(d).encode(),headers={"content-type":"application/json"})
 try:
  with urllib.request.urlopen(r,timeout=9) as x:return json.load(x)
 except urllib.error.HTTPError as e:return {"_err":e.code}
 except Exception:return {"_err":0}
if __name__=="__main__":
 while True:
  g=post("/game",{})
  if g.get("status")=="done":break
  if "_err" in g:sys.exit(1)
  while g.get("status")=="your_move":
   lg=g["legal_moves"]
   try:mv=choose(g["fen"],lg)
   except Exception:mv=lg[0]
   r=post("/move",{"game":g["game"],"move":mv})
   if "_err" in r:
    for m in lg:
     if m==mv:continue
     r=post("/move",{"game":g["game"],"move":m})
     if "_err" not in r:break
    if "_err" in r:post("/resign",{"game":g["game"]});g=post("/game",{});break
   g=r
  print(f"game {g.get('game')}: {g.get('outcome')} by {g.get('reason')}",file=sys.stderr)
 print(f"done: {g.get('wins')} won, {g.get('draws')} drawn, {g.get('losses')} lost",file=sys.stderr)
