import re, textwrap
from PIL import Image, ImageDraw, ImageFont

games = ["caca-a-mola","caca-o-rabo-do-macaco","copos-e-molas","corda-de-fogo",
         "corrida-de-cavaletes","desenho-magico","engenhos-de-agua","guerra-de-catapultas",
         "o-tripe-escutista","pesca-de-escuteiros","veste-o-balao"]
base = "content/games"
palettes = [((34,139,87),(20,90,60)),((46,134,193),(26,82,118)),((230,126,34),(160,80,20)),
            ((142,68,173),(91,44,111)),((22,160,133),(13,98,82)),((192,57,43),(120,40,30)),
            ((41,128,185),(23,78,113)),((211,84,0),(140,55,0)),((39,174,96),(24,106,59)),
            ((52,152,219),(33,97,140)),((155,89,182),(98,56,115))]

def font(sz):
    for p in ["/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
              "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"]:
        try: return ImageFont.truetype(p, sz)
        except: pass
    return ImageFont.load_default()

for i,slug in enumerate(games):
    md = open(f"{base}/{slug}/index.md", encoding="utf-8").read()
    m = re.search(r'title:\s*"([^"]+)"', md)
    title = m.group(1) if m else slug
    W=H=1024
    top,bot = palettes[i % len(palettes)]
    img = Image.new("RGB",(W,H)); px=img.load()
    for y in range(H):
        t=y/H
        row=tuple(int(top[c]+(bot[c]-top[c])*t) for c in range(3))
        for x in range(W): px[x,y]=row
    d=ImageDraw.Draw(img)
    white=(255,255,255)
    d.rounded_rectangle([80,80,W-80,H-80], radius=48, outline=white, width=6)
    # simple tent icon (triangle + door + ground line)
    cx=W//2; ty=210; base_y=360; half=120
    d.polygon([(cx,ty),(cx-half,base_y),(cx+half,base_y)], outline=white, width=8)
    d.line([(cx-half-30,base_y),(cx+half+30,base_y)], fill=white, width=8)      # ground
    d.polygon([(cx,ty+40),(cx-34,base_y),(cx+34,base_y)], fill=white)            # door
    d.line([(cx,ty-26),(cx,ty)], fill=white, width=6)                           # pole tip
    # title
    fmid=font(60)
    lines=textwrap.wrap(title, width=15)
    total=len(lines)*78
    y=500-total//2 + 39
    for ln in lines:
        d.text((cx,y), ln, font=fmid, fill=white, anchor="mm"); y+=78
    d.text((cx,H-250),"Imagem ilustrativa", font=font(34), fill=white, anchor="mm")
    d.text((cx,H-200),"placeholder — a substituir por imagem AI", font=font(26), fill=(235,235,235), anchor="mm")
    img.save(f"{base}/{slug}/action.jpg", "JPEG", quality=82)
print("done", len(games), "images")
