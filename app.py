import base64
import json
from pathlib import Path
import streamlit as st

st.set_page_config(page_title="Meera ❤ Zeel — Love River Flight", layout="wide")

ASSETS = Path(__file__).parent / "assets"

def to_data_uri(path: Path) -> str:
    if not path.exists():
        return ""
    ext = path.suffix.lower().replace(".", "")
    if ext in ("jpg", "jpeg"):
        mime = "jpeg"
    else:
        mime = "png"
    return f"data:image/{mime};base64," + base64.b64encode(path.read_bytes()).decode("utf-8")

# -----------------------
# STAGES
# -----------------------
stages = [
    {"id":"req","date":"(No date)","title":"Instagram Request 💌",
     "desc":"Zeel sent request… Meera accepted ✅",
     "ai":"ai_00_request.png"},

    {"id":"d17","date":"17 Dec 2023","title":"First Meet ✨",
     "desc":"Commerce Six Road Metro Station",
     "ai":"ai_01_17dec.png"},

    {"id":"jan6","date":"06 Jan 2024","title":"Ajay's Cafe ☕",
     "desc":"Coffee + talks + vibes",
     "ai":"ai_03_06jan.png"},

    {"id":"feb14","date":"14 Feb 2024","title":"Ahmedabad Gufa 💗",
     "desc":"Meera met Zeel with her friend Hiral at Ahmedabad Gufa",
     "ai":"ai_04_14feb.png"},

    {"id":"mar6","date":"06 Mar 2024","title":"Parimal Garden 🌿",
     "desc":"First time exploring Parimal together",
     "ai":"ai_05_06mar.png"},

    {"id":"mar8","date":"08 Mar 2024","title":"First Kiss 😘",
     "desc":"First kiss moment in Parimal garden",
     "ai":"ai_06_08mar.png"},

    {"id":"mar28","date":"28 Mar 2024","title":"Cheek Bite 😂",
     "desc":"Funny cute moment — bite on cheek (not ear 😄)",
     "ai":"ai_07_28mar.png"},

    {"id":"mar29","date":"29 Mar 2024","title":"Bounce Up 🎉",
     "desc":"Meera + Zeel + Hiral + Ujjaval at adventure jump park",
     "ai":"ai_08_29mar.png"},

    {"id":"mar30","date":"30 Mar 2024","title":"Parimal (Group) 🌳",
     "desc":"All four spending quality time together at Parimal",
     "ai":"ai_09_30mar.png"},

    {"id":"mar31","date":"31 Mar 2024","title":"Bye + Movie Date 🎬",
     "desc":"Meera & Zeel together saying bye to Hiral (bus) + sleeping sofa movie date",
     "ai":"ai_10_31mar.png"},

    {"id":"apr5","date":"05 Apr 2024","title":"Parimal Again 💞",
     "desc":"Best friend bond + date vibes (quality time)",
     "ai":"ai_11_05apr.png"},

    {"id":"apr6","date":"06 Apr 2024","title":"Unlimited + Real Paprika 🍕",
     "desc":"Real Paprika date — love story started ❤️",
     "ai":"ai_12_06apr.png"},

    {"id":"promise","date":"After that ❤️","title":"Promise Bond 🤝💖",
     "desc":"Best friends → future life partners",
     "ai":"ai_13_promise.png"},
]

# Check for missing images
missing = []
for s in stages:
    p = ASSETS / s["ai"]
    if not p.exists():
        missing.append(str(p))
if missing:
    st.warning("Missing images in assets folder:\n" + "\n".join(missing))

payload = [{**s, "img": to_data_uri(ASSETS / s["ai"])} for s in stages]
payload_json = json.dumps(payload)

# Streamlit UI
st.markdown(
    """
    <style>
      .block-container { padding-top: 0.8rem; padding-bottom: 0.8rem; max-width: 100% !important; }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("## ✈️ Meera ❤ Zeel — Love River Flight")

html = f"""
<!doctype html>
<html>
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1"/>
<style>
  *{{ box-sizing:border-box; margin:0; padding:0; }}
  body{{ 
    margin:0; 
    font-family: system-ui,-apple-system,Segoe UI,Roboto,Arial; 
    overflow:hidden; 
    height:100vh;
    background: linear-gradient(180deg, #0a1628, #1a3a6a, #2a5a8a, #1a3a6a);
  }}

  /* LIGHT BLUE WAVE BACKGROUND */
  .waves-container {{
    position:fixed;
    inset:0;
    z-index:0;
    overflow:hidden;
    background: linear-gradient(180deg, #0a1628 0%, #1a4a7a 30%, #2a6a9a 60%, #1a4a7a 100%);
  }}
  
  .wave {{
    position:absolute;
    bottom:0;
    left:-50%;
    width:200%;
    height:100%;
    background: repeating-linear-gradient(
      90deg,
      transparent,
      transparent 50px,
      rgba(100,200,255,0.04) 50px,
      rgba(100,200,255,0.04) 51px
    );
    animation: waveMove 20s linear infinite;
  }}
  
  .wave:nth-child(2) {{
    animation-duration: 15s;
    animation-delay: -5s;
    background: repeating-linear-gradient(
      90deg,
      transparent,
      transparent 80px,
      rgba(100,200,255,0.06) 80px,
      rgba(100,200,255,0.06) 81px
    );
  }}
  
  .wave:nth-child(3) {{
    animation-duration: 25s;
    animation-delay: -10s;
    background: repeating-linear-gradient(
      90deg,
      transparent,
      transparent 120px,
      rgba(100,200,255,0.03) 120px,
      rgba(100,200,255,0.03) 121px
    );
  }}
  
  @keyframes waveMove {{
    0% {{ transform: translateX(0); }}
    100% {{ transform: translateX(50%); }}
  }}

  /* Red glitter hearts */
  .heart{{
    position:fixed;
    bottom:-40px;
    opacity: 0;
    z-index:1;
    pointer-events:none;
    animation: floatUp linear infinite;
    filter: drop-shadow(0 10px 14px rgba(0,0,0,.10));
  }}
  .heart::after{{
    content:"❤";
    display:block;
    background: linear-gradient(180deg, #ff0a54, #ff3d7f, #ff0a54);
    -webkit-background-clip: text;
    background-clip: text;
    color: transparent;
    text-shadow:
      0 0 6px rgba(255,0,80,.45),
      0 0 12px rgba(255,0,80,.18);
  }}
  @keyframes floatUp{{
    0%   {{ transform: translateY(0) translateX(0) scale(.75) rotate(0deg); opacity: 0; }}
    12%  {{ opacity: .88; }}
    100% {{ transform: translateY(-125vh) translateX(var(--dx)) scale(1.35) rotate(18deg); opacity: 0; }}
  }}

  /* sparkles */
  .spark{{
    position:fixed;
    width: 5px; height: 5px;
    border-radius: 999px;
    background: rgba(255, 40, 120, .85);
    box-shadow:
      0 0 10px rgba(255,0,90,.30),
      0 0 18px rgba(255,0,90,.14);
    opacity: 0;
    z-index:1;
    pointer-events:none;
    animation: twinkle ease-in-out infinite;
  }}
  @keyframes twinkle{{
    0%,100% {{ transform: scale(.7); opacity: 0; }}
    45%     {{ opacity: .85; }}
    60%     {{ transform: scale(1.35); opacity: .95; }}
  }}

  /* HUD */
  .hud{{
    position:fixed; left: 14px; right:14px; top:12px;
    z-index:30;
    display:flex; justify-content:space-between; align-items:center; gap:12px;
  }}
  .pill{{
    background: rgba(255,255,255,.62);
    border: 1px solid rgba(255,255,255,.82);
    border-radius: 999px;
    padding: 10px 14px;
    backdrop-filter: blur(10px);
    box-shadow: 0 14px 50px rgba(170, 40, 95, .10);
    display:flex; gap:10px; align-items:center;
    min-height: 44px;
    white-space: nowrap;
  }}
  .brand{{
    display:flex;
    flex-direction:column;
    gap:2px;
  }}
  .brandTop{{
    font-weight: 980;
    letter-spacing:.2px;
    color: rgba(255,255,255,0.95);
  }}
  .brandSub{{
    font-size: 12px;
    color: rgba(200,220,255,0.72);
    margin-top:-2px;
  }}
  .tiny{{ font-size: 12px; color: rgba(200,220,255,0.72); }}

  .wrap{{
    position:fixed; inset:0;
    padding: 78px 12px 14px;
    display:flex;
    flex-direction:column;
    gap: 12px;
    z-index:2;
  }}

  /* MAP box */
  .map{{
    flex:1;
    position:relative;
    border-radius: 28px;
    background: rgba(100, 180, 255, .15);
    border: 1px solid rgba(255,255,255,.25);
    overflow:hidden;
    box-shadow: var(--shadow);
    backdrop-filter: blur(5px);
  }}
  .riverSvg{{
    position:absolute; inset:0;
    width:100%; height:100%;
    opacity: .95;
    pointer-events:none;
  }}

  /* STOPS - BIG, BRIGHT, VISIBLE */
  .stop{{
    position:absolute;
    width: 60px; 
    height: 60px;
    border-radius: 50%;
    transform: translate(-50%, -50%);
    display:flex;
    align-items:center;
    justify-content:center;
    cursor:pointer;
    user-select:none;
    background: radial-gradient(circle, #ffffff, #f0e6d0);
    border: 4px solid #ffd700;
    box-shadow: 
      0 0 30px rgba(255, 215, 0, 0.6),
      0 0 60px rgba(255, 215, 0, 0.3),
      inset 0 2px 10px rgba(255,215,0,0.2);
    transition: all 0.3s ease;
    z-index:10;
    font-weight: 900;
    color: #4a1a2a;
    font-size: 18px;
    text-shadow: 0 1px 2px rgba(255,255,255,0.5);
  }}
  .stop::before {{
    content: '';
    position: absolute;
    inset: -8px;
    border-radius: 50%;
    background: rgba(255, 215, 0, 0.2);
    animation: pulse 2s ease-in-out infinite;
    z-index: -1;
  }}
  @keyframes pulse {{
    0%, 100% {{ transform: scale(1); opacity: 0.5; }}
    50% {{ transform: scale(1.3); opacity: 0.2; }}
  }}
  .stop:hover{{ 
    transform: translate(-50%, -50%) scale(1.2); 
    box-shadow: 
      0 0 50px rgba(255, 215, 0, 0.8),
      0 0 80px rgba(255, 215, 0, 0.4);
    border-color: #ffaa00;
    z-index:15;
  }}
  .stop .n{{ 
    font-weight: 900; 
    font-size: 20px; 
    color: #4a1a2a;
    z-index:2;
    position:relative;
  }}
  .stop.active{{ 
    border-color: #ff1493;
    box-shadow: 
      0 0 40px rgba(255, 20, 147, 0.7),
      0 0 80px rgba(255, 20, 147, 0.3);
    transform: translate(-50%, -50%) scale(1.15);
    background: radial-gradient(circle, #fff5f5, #ffe0e8);
  }}
  .stop.opened{{ 
    border-color: #ff6b6b;
    background: radial-gradient(circle, #fff5f5, #ffe8e8);
    box-shadow: 
      0 0 40px rgba(255, 107, 107, 0.5),
      0 0 80px rgba(255, 107, 107, 0.2);
  }}
  .stop.opened::after {{
    content: '✓';
    position: absolute;
    top: -8px;
    right: -8px;
    font-size: 14px;
    background: #4CAF50;
    color: white;
    border-radius: 50%;
    width: 22px;
    height: 22px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: bold;
    box-shadow: 0 2px 10px rgba(76, 175, 80, 0.4);
  }}

  .hint{{
    position:absolute;
    left: 50%;
    top: -48px;
    transform: translateX(-50%);
    background: rgba(0,0,0,0.9);
    border: 1px solid rgba(255,255,255,0.2);
    padding: 6px 14px;
    border-radius: 999px;
    font-size: 11px;
    color: rgba(255,255,255,0.95);
    opacity: 0;
    white-space: nowrap;
    transition: opacity 0.3s ease;
    box-shadow: 0 12px 30px rgba(0,0,0,0.5);
    pointer-events:none;
    font-weight: 600;
    z-index:20;
  }}
  .stop:hover .hint{{ opacity: 1; }}

  /* Plane */
  .plane{{
    position:absolute;
    font-size: 44px;
    transform: translate(-50%, -50%);
    z-index: 20;
    filter: drop-shadow(0 18px 30px rgba(255,200,100,0.5));
    will-change: left, top;
    transition: none;
    pointer-events:none;
  }}

  /* Bottom bar */
  .bar{{
    background: rgba(255,255,255,.15);
    border: 1px solid rgba(255,255,255,.25);
    border-radius: 18px;
    padding: 10px 12px;
    backdrop-filter: blur(10px);
    box-shadow: 0 14px 50px rgba(170, 40, 95, .08);
    display:flex;
    justify-content:space-between;
    align-items:center;
    gap: 12px;
  }}
  .nowTitle{{
    font-weight: 900;
    font-size: 15px;
    padding: 8px 16px;
    border-radius: 999px;
    background: rgba(255,255,255,.9);
    border: 1px solid rgba(255,255,255,.95);
    width: fit-content;
    color: rgba(65, 15, 40, .95);
  }}
  .nowSub{{ font-size: 13px; color: rgba(200,220,255,0.9); font-weight: 600; }}

  /* Falling gifts */
  .giftFall{{
    position:fixed;
    top:-70px;
    width: 54px; 
    height: 54px;
    border-radius: 16px;
    background: linear-gradient(135deg, #fff5f5, #ffffff);
    border: 2px solid rgba(255,215,0,0.7);
    box-shadow: 0 16px 40px rgba(255,200,100,0.3);
    display:grid;
    place-items:center;
    z-index: 60;
    cursor:pointer;
    user-select:none;
    animation: fall linear forwards;
    transform: translateX(-50%);
    font-size: 28px;
    transition: transform 0.2s ease;
  }}
  .giftFall:hover{{
    transform: translateX(-50%) scale(1.15);
    box-shadow: 0 20px 50px rgba(255,200,100,0.5);
  }}
  @keyframes fall{{
    from{{ transform: translateX(-50%) translateY(0) rotate(0deg); }}
    to  {{ transform: translateX(-50%) translateY(130vh) rotate(360deg); }}
  }}

  /* blast particles */
  .burst{{
    position:fixed;
    pointer-events:none;
    z-index: 500;
    animation: burst .9s ease forwards;
    border-radius: 50%;
  }}
  @keyframes burst{{
    from{{ transform: translate(-50%,-50%) scale(0.5); opacity: 1; }}
    to  {{ transform: translate(calc(-50% + var(--dx)), calc(-50% + var(--dy))) scale(0); opacity: 0; }}
  }}

  /* Memory overlay */
  .overlay{{
    position:fixed; inset:0;
    display:none;
    align-items:center; justify-content:center;
    background: rgba(10, 20, 40, .7);
    backdrop-filter: blur(10px);
    z-index: 120;
    padding: 18px;
  }}
  .card{{
    width: min(880px, 96vw);
    border-radius: 26px;
    background: rgba(255,255,255,.92);
    border: 1px solid rgba(255,255,255,.95);
    box-shadow: 0 22px 90px rgba(160, 50, 100, .14);
    overflow:hidden;
    transform: scale(.98);
    animation: pop .16s ease forwards;
  }}
  @keyframes pop{{ to{{ transform: scale(1); }} }}

  .cardTop{{
    display:flex; justify-content:space-between; align-items:center; gap:12px;
    padding: 12px 14px;
    background: rgba(255,255,255,.66);
    border-bottom: 1px solid rgba(255,255,255,.90);
  }}
  .x{{
    cursor:pointer;
    border-radius: 999px;
    border: 1px solid rgba(255,255,255,.95);
    background: rgba(255,255,255,.86);
    color: rgba(65, 15, 40, .95);
    padding: 8px 12px;
    font-weight: 900;
  }}

  .cardBody{{
    display:grid;
    grid-template-columns: 1.1fr 1fr;
    gap: 14px;
    padding: 14px;
  }}

  .photo3d{{
    position:relative;
    border-radius: 22px;
    transform-style: preserve-3d;
    perspective: 900px;
  }}
  .midImg{{
    width: 100%;
    height: clamp(270px, 42vh, 410px);
    object-fit: cover;
    border-radius: 22px;
    border: 1px solid rgba(255,255,255,.95);
    background: rgba(255,255,255,.70);
    transform: translateZ(16px);
    box-shadow: 0 18px 55px rgba(160,50,100,.10);
    display:block;
  }}
  .shine{{
    position:absolute;
    inset:0;
    border-radius: 22px;
    background: radial-gradient(600px 220px at var(--mx,50%) var(--my,30%), rgba(255,0,90,.14), transparent 60%);
    mix-blend-mode: multiply;
    pointer-events:none;
    opacity:.75;
  }}

  .info{{ display:flex; flex-direction:column; gap:10px; }}
  .date{{
    width:fit-content;
    padding: 7px 10px;
    border-radius: 999px;
    background: rgba(255,255,255,.90);
    border: 1px solid rgba(255,255,255,.95);
    font-size: 12px;
    color: rgba(105, 30, 70, .72);
  }}
  .head{{ font-size: 24px; font-weight: 900; line-height: 1.08; color: rgba(65,15,40,.95); }}
  .desc{{ font-size: 14px; line-height: 1.6; color: rgba(85,25,55,.84); }}

  @media (max-width: 860px){{
    .cardBody{{ grid-template-columns: 1fr; }}
    .midImg{{ height: clamp(250px, 36vh, 350px); }}
  }}

  /* Wish Envelope */
  .wishBack{{
    position:fixed; inset:0;
    display:none;
    align-items:center; justify-content:center;
    background: rgba(10, 20, 40, .7);
    backdrop-filter: blur(10px);
    z-index: 200;
    padding: 18px;
  }}
  .envelope{{
    width: min(560px, 94vw);
    border-radius: 26px;
    background: rgba(255,255,255,.92);
    border: 1px solid rgba(255,255,255,.95);
    box-shadow: 0 24px 90px rgba(160,50,100,.14);
    overflow:hidden;
    transform: translateY(10px) scale(.98);
    animation: envPop .18s ease forwards;
  }}
  @keyframes envPop{{ to{{ transform: translateY(0) scale(1); }} }}
  .envTop{{
    padding: 12px 14px;
    display:flex; align-items:center; justify-content:space-between;
    background: rgba(255,255,255,.70);
    border-bottom: 1px solid rgba(255,255,255,.92);
  }}
  .envTitle{{
    font-weight: 900;
    color: rgba(65,15,40,.92);
    display:flex; gap:8px; align-items:center;
  }}
  .envBody{{ padding: 16px 16px 18px; }}
  .wishCard{{
    border-radius: 18px;
    background: linear-gradient(135deg, rgba(255,220,235,.70), rgba(255,255,255,.82));
    border: 1px solid rgba(255,255,255,.92);
    padding: 14px 14px;
    color: rgba(65,15,40,.90);
    box-shadow: 0 14px 40px rgba(160,50,100,.08);
  }}
  .wishLine1{{ font-weight: 900; font-size: 16px; }}
  .wishLine2{{ margin-top: 8px; font-size: 14px; line-height: 1.6; color: rgba(85,25,55,.84); }}
</style>
</head>

<body>
<script>
  // hearts + sparkles
  const heartCount = 56;
  for(let i=0;i<heartCount;i++){{
    const h = document.createElement("div");
    h.className = "heart";
    h.style.left = (Math.random()*100) + "vw";
    h.style.animationDuration = (6 + Math.random()*8) + "s";
    h.style.fontSize = (14 + Math.random()*20) + "px";
    h.style.setProperty("--dx", ((Math.random()*180)-90) + "px");
    h.style.animationDelay = (Math.random()*6) + "s";
    document.body.appendChild(h);
  }}
  const sparkCount = 34;
  for(let i=0;i<sparkCount;i++){{
    const s = document.createElement("div");
    s.className = "spark";
    s.style.left = (Math.random()*100) + "vw";
    s.style.top  = (Math.random()*100) + "vh";
    s.style.animationDuration = (2.0 + Math.random()*3.0) + "s";
    s.style.animationDelay = (Math.random()*2.5) + "s";
    document.body.appendChild(s);
  }}
</script>

  <div class="hud">
    <div class="pill">
      <div class="brand">
        <div class="brandTop">✈️ Meera ❤ Zeel — Love River Flight</div>
        <div class="brandSub">Click on gold station dots • Plane flies to each stop</div>
      </div>
    </div>
    <div class="pill">
      <div class="tiny" id="counter">0 / 13 opened</div>
    </div>
  </div>

  <div class="wrap">
    <div class="map" id="map">
      <svg class="riverSvg" viewBox="0 0 100 100" preserveAspectRatio="none">
        <path d="M50,5
                 C30,12 72,18 50,25
                 C28,32 74,40 52,48
                 C30,56 70,63 50,72
                 C30,80 72,88 50,95"
              fill="none" stroke="rgba(255,255,255,.40)" stroke-width="12" stroke-linecap="round"/>
        <path d="M50,5
                 C30,12 72,18 50,25
                 C28,32 74,40 52,48
                 C30,56 70,63 50,72
                 C30,80 72,88 50,95"
              fill="none" stroke="rgba(115, 205, 255, .40)" stroke-width="8" stroke-linecap="round"/>
        <path d="M50,5
                 C30,12 72,18 50,25
                 C28,32 74,40 52,48
                 C30,56 70,63 50,72
                 C30,80 72,88 50,95"
              fill="none" stroke="rgba(255,255,255,.40)" stroke-width="1.3" stroke-dasharray="3 4" stroke-linecap="round"/>
      </svg>

      <div class="plane" id="plane">✈️</div>
      <div id="stopsLayer"></div>
    </div>

    <div class="bar">
      <div>
        <div class="nowTitle" id="nowTitle">📍 Stop 1: Instagram Request 💌</div>
        <div class="nowSub" id="nowSub">✨ Click any gold dot to fly there</div>
      </div>
      <div class="tiny" style="font-size:14px; background:rgba(255,255,255,0.2); padding:6px 14px; border-radius:999px;">
        🎁 Click falling gifts!
      </div>
    </div>
  </div>

  <div class="overlay" id="overlay">
    <div class="card" id="card">
      <div class="cardTop">
        <div style="display:flex; gap:10px; align-items:center;">
          <div class="date" id="cDate"></div>
          <div style="font-weight:900; color:rgba(65,15,40,.90);" id="cSmall"></div>
        </div>
        <button class="x" id="close">✕</button>
      </div>

      <div class="cardBody">
        <div class="photo3d" id="photo3d">
          <img class="midImg" id="cImg" src="" alt="memory"/>
          <div class="shine" id="shine"></div>
        </div>

        <div class="info">
          <div class="head" id="cHead"></div>
          <div class="desc" id="cDesc"></div>
          <div style="margin-top:auto; font-size:12px; color:rgba(85,25,55,.5);">(tap outside to close)</div>
        </div>
      </div>
    </div>
  </div>

  <div class="wishBack" id="wishBack">
    <div class="envelope">
      <div class="envTop">
        <div class="envTitle">💌 Valentine Wish</div>
        <button class="x" id="wishClose">✕</button>
      </div>
      <div class="envBody">
        <div class="wishCard">
          <div class="wishLine1" id="wishL1">To Meera ❤ Zeel</div>
          <div class="wishLine2" id="wishL2">...</div>
        </div>
      </div>
    </div>
  </div>

<script>
  const STAGES = {payload_json};

  const WISHES = [
    "Happy Valentine's Day! 💖 You two are the cutest love story — keep choosing each other every day.",
    "Your bond feels like home 🏡💞. May your love stay soft, silly, and strong forever.",
    "To Meera ❤ Zeel: May your smiles stay in sync and your hearts stay in one team 💘",
    "Love is not perfect — it's beautiful because you both try 💗 Happy Valentine's Day!",
    "You both are the kind of couple that makes love look easy 😄💖 Stay happy always!",
    "From first meet to forever vibes ✨💘 Keep flying together!",
    "May your love be sweet like chocolate 🍫 and warm like hugs 🤗💗",
    "Two hearts, one beautiful journey 💕 Keep soaring high together!",
    "Every love story is beautiful, but yours is my favorite ❤️",
    "May your love shine brighter than all the stars ✨🌟"
  ];
  const GIFT_EMOJI = ["🎁","💝","🎁","💝","🎀","💕","❤️"];

  const KEY = "mz_love_river_v3";
  let opened = new Set(JSON.parse(localStorage.getItem(KEY) || "[]"));

  const counter = document.getElementById("counter");
  const nowTitle = document.getElementById("nowTitle");
  const nowSub = document.getElementById("nowSub");

  const stopsLayer = document.getElementById("stopsLayer");
  const plane = document.getElementById("plane");

  const overlay = document.getElementById("overlay");
  const closeBtn = document.getElementById("close");
  const cImg = document.getElementById("cImg");
  const cDate = document.getElementById("cDate");
  const cSmall = document.getElementById("cSmall");
  const cHead = document.getElementById("cHead");
  const cDesc = document.getElementById("cDesc");

  const photo3d = document.getElementById("photo3d");
  const shine = document.getElementById("shine");

  const wishBack = document.getElementById("wishBack");
  const wishClose = document.getElementById("wishClose");
  const wishL1 = document.getElementById("wishL1");
  const wishL2 = document.getElementById("wishL2");

  // STATION POSITIONS - spread out along the river
  const POS = [
    {{x:50, y:8}},
    {{x:35, y:16}},
    {{x:60, y:25}},
    {{x:40, y:34}},
    {{x:63, y:43}},
    {{x:45, y:52}},
    {{x:65, y:60}},
    {{x:42, y:68}},
    {{x:60, y:76}},
    {{x:40, y:83}},
    {{x:62, y:88}},
    {{x:50, y:93}},
    {{x:55, y:97}},
  ].slice(0, STAGES.length);

  let idx = 0;
  let planePos = {{ x: Math.max(6, POS[0].x - 12), y: POS[0].y }};
  let anim = null;

  function updateCounter(){{
    const total = STAGES.length;
    const openedCount = opened.size;
    counter.textContent = `${{openedCount}} / ${{total}} opened`;
  }}
  
  function save(){{
    localStorage.setItem(KEY, JSON.stringify(Array.from(opened)));
    updateCounter();
  }}
  
  function setActiveStop(i){{
    [...stopsLayer.querySelectorAll(".stop")].forEach((b, j)=>{{
      b.classList.toggle("active", j === i);
    }});
  }}

  function closeMemory(){{ overlay.style.display = "none"; }}
  
  function openMemory(){{
    const s = STAGES[idx];

    opened.add(s.id);
    save();

    const btns = stopsLayer.querySelectorAll(".stop");
    if(btns[idx]) btns[idx].classList.add("opened");

    cImg.src = s.img || "";
    cDate.textContent = s.date;
    cSmall.textContent = `Stage ${{idx+1}} / ${{STAGES.length}}`;
    cHead.textContent = s.title;
    cDesc.textContent = s.desc;

    overlay.style.display = "flex";
  }}
  
  closeBtn.addEventListener("click", closeMemory);
  overlay.addEventListener("click", (e)={{ if(e.target === overlay) closeMemory(); }});

  function flyTo(targetIdx, openAfter=false){{
    targetIdx = Math.max(0, Math.min(STAGES.length-1, targetIdx));

    if(targetIdx === idx){{
      if(openAfter) openMemory();
      return;
    }}

    const from = {{x: planePos.x, y: planePos.y}};
    const to = POS[targetIdx];

    if(anim) cancelAnimationFrame(anim);

    idx = targetIdx;
    setActiveStop(idx);

    const s = STAGES[idx];
    nowTitle.textContent = `📍 Stop ${{idx+1}}: ${{s.title}}`;
    nowSub.textContent = s.date;

    const dx = (to.x - from.x), dy = (to.y - from.y);
    const dist = Math.sqrt(dx*dx + dy*dy);
    const dur = Math.min(1250, Math.max(650, dist * 26));
    const start = performance.now();
    const ease = (t) => 1 - Math.pow(1 - t, 3);
    const arc = Math.max(1.8, Math.min(6, dist/5));

    function step(now){{
      const t = Math.min(1, (now - start) / dur);
      const e = ease(t);

      const x = from.x + (to.x - from.x) * e;
      const y = from.y + (to.y - from.y) * e - Math.sin(Math.PI * e) * arc;

      plane.style.left = x + "%";
      plane.style.top  = y + "%";

      if(t < 1){{
        anim = requestAnimationFrame(step);
      }}else{{
        planePos = {{x: to.x, y: to.y}};
        plane.style.left = to.x + "%";
        plane.style.top  = to.y + "%";
        if(openAfter){{
          setTimeout(()=> openMemory(), 300);
        }}
      }}
    }}
    anim = requestAnimationFrame(step);
  }}

  function buildStops(){{
    stopsLayer.innerHTML = "";
    STAGES.forEach((s, i)=>{{
      const p = POS[i];
      const b = document.createElement("div");
      b.className = "stop" + (opened.has(s.id) ? " opened" : "");
      b.style.left = p.x + "%";
      b.style.top  = p.y + "%";
      b.innerHTML = `
        <div class="hint">${{s.date}} • ${{s.title}}</div>
        <div class="n">${{i+1}}</div>
      `;
      b.addEventListener("click", (e)=>{{
        e.stopPropagation();
        closeMemory();
        flyTo(i, true);
      }});
      stopsLayer.appendChild(b);
    }});
    updateCounter();
    setActiveStop(0);
  }}

  function resetTilt(){{
    photo3d.style.transform = "rotateX(0deg) rotateY(0deg)";
    shine.style.setProperty("--mx", "50%");
    shine.style.setProperty("--my", "30%");
  }}
  
  photo3d.addEventListener("mousemove", (e)=>{{
    const r = photo3d.getBoundingClientRect();
    const x = (e.clientX - r.left) / r.width;
    const y = (e.clientY - r.top) / r.height;
    const rotY = (x - 0.5) * 14;
    const rotX = (0.5 - y) * 10;
    photo3d.style.transform = `rotateX(${{rotX}}deg) rotateY(${{rotY}}deg)`;
    shine.style.setProperty("--mx", (x*100).toFixed(1) + "%");
    shine.style.setProperty("--my", (y*100).toFixed(1) + "%");
  }});
  photo3d.addEventListener("mouseleave", resetTilt);

  function openWish(){{
    wishL1.textContent = "To Meera ❤ Zeel";
    wishL2.textContent = WISHES[Math.floor(Math.random()*WISHES.length)];
    wishBack.style.display = "flex";
  }}
  
  function closeWish(){{ wishBack.style.display = "none"; }}
  wishClose.addEventListener("click", closeWish);
  wishBack.addEventListener("click", (e)={{ if(e.target === wishBack) closeWish(); }});

  function blastAt(clientX, clientY){{
    const colors = ["#ff6b6b", "#ffd93d", "#6bcb77", "#4d96ff", "#ff6bb5", "#a66bff", "#ff9f43", "#00d2d3"];
    for(let i=0;i<30;i++){{
      const p = document.createElement("div");
      p.className = "burst";
      const angle = (Math.PI * 2 * i) / 30 + Math.random() * 0.3;
      const dist = 60 + Math.random() * 120;
      p.style.left = clientX + "px";
      p.style.top  = clientY + "px";
      p.style.setProperty("--dx", Math.cos(angle) * dist + "px");
      p.style.setProperty("--dy", Math.sin(angle) * dist - 30 + "px");
      p.style.background = colors[Math.floor(Math.random() * colors.length)];
      p.style.width = (6 + Math.random() * 10) + "px";
      p.style.height = p.style.width;
      p.style.boxShadow = `0 0 20px ${{colors[Math.floor(Math.random() * colors.length)]}}40`;
      document.body.appendChild(p);
      setTimeout(()=> p.remove(), 900);
    }}
  }}

  function spawnFallingGift(){{
    const g = document.createElement("div");
    g.className = "giftFall";
    g.style.left = (Math.random()*100) + "vw";
    g.style.animationDuration = (4 + Math.random()*4) + "s";
    g.innerHTML = GIFT_EMOJI[Math.floor(Math.random()*GIFT_EMOJI.length)];
    g.addEventListener("click", (e)=>{{
      e.stopPropagation();
      blastAt(e.clientX, e.clientY);
      openWish();
      g.remove();
    }});
    document.body.appendChild(g);
    setTimeout(()=> g.remove(), 9000);
  }}
  
  // Spawn gifts every 500ms
  setInterval(spawnFallingGift, 500);

  // Init
  buildStops();
  plane.style.left = planePos.x + "%";
  plane.style.top  = planePos.y + "%";
  nowTitle.textContent = `📍 Stop 1: ${{STAGES[0].title}}`;
  nowSub.textContent = STAGES[0].date;
  resetTilt();
  updateCounter();
</script>
</body>
</html>
"""

st.components.v1.html(html, height=780, scrolling=False)

st.info(
    "💝 **Meera & Zeel's Love River Flight**\n\n"
    "• Click on the **gold numbered dots** (1-13) along the river\n"
    "• Watch the **plane fly** to each station with smooth animation\n"
    "• Each stop opens a **memory with photo**\n"
    "• Click **falling gifts** for surprise love wishes\n"
    "• Beautiful light blue wave background with floating hearts ✨"
)
