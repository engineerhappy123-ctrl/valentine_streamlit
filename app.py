import base64
from pathlib import Path
import streamlit as st

st.set_page_config(page_title="Meera ❤ Zeel — Valentine Journey", layout="wide")

# ----------------------------
# 1) STAGES DATA - Update with your own info
# ----------------------------
stages = [
    dict(id="req",  date="(No date)", title="Instagram Request 💌",
         desc="Zeel sent request… Meera accepted ✅"),
    dict(id="d17",  date="17 Dec 2023", title="First Meet ✨",
         desc="Commerce Six Road Metro Station"),
    dict(id="d26",  date="26 Dec 2023", title="Second Date 😍",
         desc="Our second meet — more comfort, more smiles"),
    dict(id="jan6", date="06 Jan 2024", title="Ajay's Cafe ☕",
         desc="Coffee + talks + vibes"),
    dict(id="feb14",date="14 Feb 2024", title="Ahmedabad Gufa 💗",
         desc="Valentine day + Zeel met Hiral"),
    dict(id="mar6", date="06 Mar 2024", title="Parimal Garden 🌿",
         desc="First time exploring Parimal together"),
    dict(id="mar8", date="08 Mar 2024", title="First Kiss 😘",
         desc="A sweet moment that changed everything"),
    dict(id="mar28",date="28 Mar 2024", title="Cheek Bite 😂",
         desc="Funny-cute moment… Meera bit Zeel's cheek"),
    dict(id="mar29",date="29 Mar 2024", title="Bounce Up 🎉",
         desc="Meera + Zeel + Hiral + Ujjaval (Bounce Up)"),
    dict(id="mar30",date="30 Mar 2024", title="Parimal (Group) 🌳",
         desc="Meera + Zeel + Hiral + Ujjaval at Parimal"),
    dict(id="mar31",date="31 Mar 2024", title="Bye + Movie + Garden 🎬",
         desc="Bye to Hiral + movie seat + Parimal garden"),
    dict(id="apr5", date="05 Apr 2024", title="Parimal Again 💞",
         desc="Same place, new feelings"),
    dict(id="apr6", date="06 Apr 2024", title="Unlimited + Real Paprika 🍕",
         desc="179 salad vs 279 salad+pizza — love story started ❤️"),
]

# Positive messages for gifts
love_messages = [
    "❤️ Every love story is beautiful, but yours is my favorite! ❤️",
    "💕 You two are proof that soulmates exist! 💕",
    "✨ May your love shine brighter than the stars! ✨",
    "💖 Together is the most beautiful place to be! 💖",
    "🌟 Your love story gives us all hope! 🌟",
    "💝 Two hearts, one beautiful journey! 💝",
    "🌈 Love is not about how many days, but how much! 🌈",
    "🎉 Celebrate every moment of your beautiful love! 🎉",
    "💫 You complete each other in the most magical way! 💫",
    "🌺 May your love bloom forever and ever! 🌺",
    "💞 True love isn't found, it's built together! 💞",
    "🌟 You are each other's greatest adventure! 🌟",
    "💝 Love is the bridge between two hearts! 💝",
    "🌈 Every day with you is a beautiful gift! 🌈",
]

# ----------------------------
# 2) Streamlit UI shell
# ----------------------------
st.markdown(
    """
    <style>
      .block-container { padding-top: 0.8rem; padding-bottom: 0.8rem; max-width: 100% !important; }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("## ✈️ Meera ❤ Zeel — Valentine Journey")

# ----------------------------
# 3) Full animated frontend in one HTML
# ----------------------------
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

  /* Animated waves background */
  .waves-container {{
    position:fixed;
    inset:0;
    z-index:0;
    overflow:hidden;
    background: linear-gradient(180deg, #0a1628 0%, #1a3a6a 30%, #2a5a8a 60%, #1a3a6a 100%);
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
      rgba(100,200,255,0.03) 50px,
      rgba(100,200,255,0.03) 51px
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
      rgba(100,200,255,0.05) 80px,
      rgba(100,200,255,0.05) 81px
    );
  }}
  
  .wave:nth-child(3) {{
    animation-duration: 25s;
    animation-delay: -10s;
    background: repeating-linear-gradient(
      90deg,
      transparent,
      transparent 120px,
      rgba(100,200,255,0.02) 120px,
      rgba(100,200,255,0.02) 121px
    );
  }}
  
  @keyframes waveMove {{
    0% {{ transform: translateX(0); }}
    100% {{ transform: translateX(50%); }}
  }}

  /* Floating particles */
  .particles {{
    position:fixed;
    inset:0;
    z-index:1;
    pointer-events:none;
  }}
  
  .particle {{
    position:absolute;
    width:3px;
    height:3px;
    background: rgba(150,220,255,0.3);
    border-radius:50%;
    animation: floatParticle 15s infinite linear;
  }}
  
  @keyframes floatParticle {{
    0% {{ transform: translateY(100vh) translateX(0px); opacity:0; }}
    10% {{ opacity:0.5; }}
    90% {{ opacity:0.5; }}
    100% {{ transform: translateY(-100vh) translateX(100px); opacity:0; }}
  }}

  /* Road with wave effect */
  .road-container {{
    position:fixed;
    bottom:100px;
    left:0;
    right:0;
    z-index:2;
    padding:0 20px;
  }}
  
  .road {{
    position:relative;
    height:6px;
    background: rgba(100,200,255,0.15);
    border-radius:3px;
    overflow:hidden;
    box-shadow: 0 0 30px rgba(100,200,255,0.1);
  }}
  
  .road-wave {{
    position:absolute;
    top:0;
    left:0;
    right:0;
    bottom:0;
    background: repeating-linear-gradient(
      90deg,
      rgba(100,200,255,0.3) 0px,
      rgba(100,200,255,0.3) 20px,
      transparent 20px,
      transparent 40px
    );
    animation: roadWave 3s linear infinite;
    border-radius:3px;
  }}
  
  @keyframes roadWave {{
    0% {{ transform: translateX(0); }}
    100% {{ transform: translateX(40px); }}
  }}

  /* Stations */
  .stations {{
    position:fixed;
    bottom:70px;
    left:0;
    right:0;
    z-index:3;
    display:flex;
    justify-content:space-around;
    padding:0 10px;
    pointer-events:none;
  }}
  
  .station {{
    display:flex;
    flex-direction:column;
    align-items:center;
    gap:4px;
    opacity:0.5;
    transition: all 0.5s ease;
    cursor:pointer;
    pointer-events:auto;
    position:relative;
  }}
  
  .station:hover {{
    opacity:0.8;
    transform: scale(1.1);
  }}
  
  .station.active {{
    opacity:1;
  }}
  
  .station .dot {{
    width:16px;
    height:16px;
    border-radius:50%;
    background: radial-gradient(circle, rgba(150,220,255,0.6), rgba(80,180,255,0.2));
    border:2px solid rgba(150,220,255,0.4);
    transition: all 0.5s ease;
    box-shadow: 0 0 20px rgba(100,200,255,0.1);
  }}
  
  .station.active .dot {{
    background: radial-gradient(circle, rgba(255,200,100,0.9), rgba(255,150,50,0.5));
    border-color: rgba(255,200,100,0.8);
    box-shadow: 0 0 30px rgba(255,200,100,0.4);
    transform: scale(1.3);
  }}
  
  .station .label {{
    font-size:9px;
    color: rgba(255,255,255,0.5);
    font-weight:600;
    letter-spacing:0.3px;
    white-space:nowrap;
    text-shadow: 0 2px 8px rgba(0,0,0,0.5);
    transition: all 0.3s ease;
  }}
  
  .station.active .label {{
    color: rgba(255,255,255,0.9);
  }}

  /* HUD */
  .hud {{
    position:fixed;
    left:14px;
    right:14px;
    top:10px;
    z-index:10;
    display:flex;
    gap:10px;
    justify-content:space-between;
    align-items:center;
  }}
  
  .pill {{
    backdrop-filter: blur(10px);
    background: rgba(255,255,255,0.08);
    border: 1px solid rgba(255,255,255,0.15);
    border-radius:999px;
    padding:8px 14px;
    box-shadow:0 10px 30px rgba(0,0,0,0.25);
    display:flex;
    gap:10px;
    align-items:center;
    min-height:38px;
    white-space:nowrap;
  }}
  
  .title {{ font-weight:700; letter-spacing:.2px; font-size:13px; color:rgba(255,255,255,0.9); }}
  .tiny {{ font-size:11px; color:rgba(255,255,255,0.6); }}
  
  .btn {{
    cursor:pointer;
    user-select:none;
    border:1px solid rgba(255,255,255,0.18);
    background: rgba(255,255,255,0.08);
    color:rgba(255,255,255,0.9);
    padding:7px 12px;
    border-radius:999px;
    font-weight:700;
    font-size:13px;
    transition: all 0.2s ease;
  }}
  
  .btn:hover {{ background: rgba(255,255,255,0.16); transform: scale(1.05); }}

  /* Progress track with plane */
  .wrap {{
    position:fixed;
    inset:0;
    padding-top:65px;
    padding-bottom:130px;
    display:flex;
    flex-direction:column;
    z-index:2;
  }}
  
  .track {{
    margin: 0 14px;
    height:8px;
    border-radius:999px;
    background: rgba(255,255,255,0.06);
    border: 1px solid rgba(255,255,255,0.1);
    position: relative;
    overflow:hidden;
  }}
  
  .progress {{
    height:100%;
    width:0%;
    border-radius:999px;
    background: linear-gradient(90deg, rgba(255,105,180,0.6), rgba(130,220,255,0.6));
    transition: width 1s cubic-bezier(.4,0,.2,1);
  }}
  
  .plane {{
    position:absolute;
    top:50%;
    left:0%;
    transform: translate(-50%,-50%);
    transition: left 1s cubic-bezier(.4,0,.2,1);
    font-size:22px;
    filter: drop-shadow(0 4px 20px rgba(100,200,255,0.3));
    z-index:5;
  }}
  
  .plane-flying {{
    animation: planeFly 0.5s ease;
  }}
  
  @keyframes planeFly {{
    0% {{ transform: translate(-50%,-50%) scale(1) rotate(0deg); }}
    25% {{ transform: translate(-50%,-80%) scale(1.15) rotate(-8deg); }}
    75% {{ transform: translate(-50%,-20%) scale(1.15) rotate(8deg); }}
    100% {{ transform: translate(-50%,-50%) scale(1) rotate(0deg); }}
  }}

  /* Floating gifts container */
  .gifts-container {{
    position:fixed;
    top:0;
    left:0;
    right:0;
    bottom:0;
    z-index:1;
    pointer-events:none;
    overflow:hidden;
  }}
  
  .floating-gift {{
    position:absolute;
    font-size:30px;
    animation: giftFloat 10s ease-in-out infinite;
    opacity:0.15;
    pointer-events:none;
  }}
  
  @keyframes giftFloat {{
    0% {{ transform: translateY(100vh) rotate(0deg) scale(0.5); opacity:0; }}
    10% {{ opacity:0.15; }}
    90% {{ opacity:0.15; }}
    100% {{ transform: translateY(-100vh) rotate(720deg) scale(1.5); opacity:0; }}
  }}

  /* Journey cards */
  .journey {{
    flex:1;
    margin-top:10px;
    overflow-x:auto;
    overflow-y:hidden;
    display:flex;
    gap:16px;
    padding: 10px 14px 18px;
    scroll-snap-type:x mandatory;
    -webkit-overflow-scrolling: touch;
  }}
  
  .journey::-webkit-scrollbar {{ height:4px; }}
  .journey::-webkit-scrollbar-track {{ background: rgba(255,255,255,0.05); border-radius:999px; }}
  .journey::-webkit-scrollbar-thumb {{ background: rgba(255,255,255,0.1); border-radius:999px; }}

  .stage {{
    scroll-snap-align:start;
    min-width: min(85vw, 360px);
    max-width:360px;
    height:100%;
    border-radius:18px;
    backdrop-filter: blur(12px);
    background: linear-gradient(180deg, rgba(255,255,255,0.08), rgba(255,255,255,0.03));
    border: 1px solid rgba(255,255,255,0.12);
    box-shadow: 0 18px 60px rgba(0,0,0,0.3);
    position: relative;
    overflow:hidden;
    padding:14px;
    display:flex;
    flex-direction:column;
    gap:8px;
  }}
  
  .stage::before {{
    content:"";
    position:absolute;
    inset:-60px;
    pointer-events:none;
    background:
      radial-gradient(600px 240px at 20% 20%, rgba(255,105,180,0.08), transparent 55%),
      radial-gradient(600px 240px at 80% 30%, rgba(120,210,255,0.08), transparent 55%);
    transform: rotate(8deg);
  }}
  
  .row {{ position:relative; display:flex; justify-content:space-between; gap:10px; }}
  
  .badge {{
    font-size:10px;
    color: rgba(255,255,255,0.7);
    background: rgba(0,0,0,0.2);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius:999px;
    padding:4px 10px;import base64
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
# STAGES (26 Dec REMOVED)
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

# Optional: quick check (comment out if you don't want any messages)
missing = []
for s in stages:
    p = ASSETS / s["ai"]
    if not p.exists():
        missing.append(str(p))
if missing:
    st.error("Missing images in assets folder:\n" + "\n".join(missing))

payload = [{**s, "img": to_data_uri(ASSETS / s["ai"])} for s in stages]
payload_json = json.dumps(payload)

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

  /* Red glitter hearts across full background */
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

  /* MAP box = SOFT LIGHT BLUE GLASS */
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
  }}

  /* Stops */
  .stop{{
    position:absolute;
    width: 44px; height:44px;
    border-radius: 999px;
    transform: translate(-50%, -50%);
    display:grid;
    place-items:center;
    cursor:pointer;
    user-select:none;
    background: rgba(255,255,255,.78);
    border: 1px solid rgba(255,255,255,.92);
    box-shadow: 0 16px 40px rgba(160, 50, 100, .10);
    transition: transform .15s ease, background .15s ease, outline .15s ease;
    z-index:5;
  }}
  .stop:hover{{ transform: translate(-50%, -50%) scale(1.06); background: rgba(255,255,255,.92); }}
  .stop .n{{ font-weight: 980; font-size: 12px; color: rgba(70, 20, 50, .92); }}
  .stop.active{{ outline: 4px solid rgba(255, 0, 90, .14); background: rgba(255,255,255,.98); }}
  .stop.opened{{ border-color: rgba(255,0,90,.20); background: rgba(255,245,252,.98); }}

  .hint{{
    position:absolute;
    left: 50%;
    top: -36px;
    transform: translateX(-50%);
    background: rgba(255,255,255,.95);
    border: 1px solid rgba(255,255,255,.95);
    padding: 6px 10px;
    border-radius: 999px;
    font-size: 12px;
    color: rgba(75, 22, 55, .82);
    opacity: 0;
    white-space: nowrap;
    transition: opacity .15s ease;
    box-shadow: 0 12px 30px rgba(160,50,100,.10);
    pointer-events:none;
  }}
  .stop:hover .hint{{ opacity: 1; }}

  /* Plane */
  .plane{{
    position:absolute;
    font-size: 34px;
    transform: translate(-50%, -50%);
    z-index: 20;
    filter: drop-shadow(0 18px 25px rgba(160,50,100,.10));
    will-change: left, top;
  }}

  /* Bottom current event */
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
    font-weight: 980;
    font-size: 14px;
    padding: 6px 12px;
    border-radius: 999px;
    background: rgba(255,255,255,.86);
    border: 1px solid rgba(255,255,255,.95);
    width: fit-content;
    color: rgba(65, 15, 40, .95);
  }}
  .nowSub{{ font-size: 12px; color: rgba(200,220,255,0.8); }}

  /* Falling gifts */
  .giftFall{{
    position:fixed;
    top:-70px;
    width: 46px; height: 46px;
    border-radius: 16px;
    background: rgba(255,255,255,.86);
    border: 1px solid rgba(255,255,255,.94);
    box-shadow: 0 16px 40px rgba(160,50,100,.08);
    display:grid;
    place-items:center;
    z-index: 60;
    cursor:pointer;
    user-select:none;
    animation: fall linear forwards;
    transform: translateX(-50%);
  }}
  @keyframes fall{{
    from{{ transform: translateX(-50%) translateY(0) rotate(0deg); }}
    to  {{ transform: translateX(-50%) translateY(130vh) rotate(14deg); }}
  }}

  /* blast particles */
  .burst{{
    position:fixed;
    width: 10px; height: 10px;
    border-radius: 999px;
    background: rgba(255,0,90,.85);
    box-shadow: 0 0 10px rgba(255,0,90,.28);
    pointer-events:none;
    z-index: 500;
    animation: burst .85s ease forwards;
  }}
  @keyframes burst{{
    from{{ transform: translate(-50%,-50%) scale(.7); opacity: .95; }}
    to  {{ transform: translate(calc(-50% + var(--dx)), calc(-50% + var(--dy))) scale(0.2); opacity: 0; }}
  }}

  /* Memory overlay */
  .overlay{{
    position:fixed; inset:0;
    display:none;
    align-items:center; justify-content:center;
    background: rgba(10, 20, 40, .6);
    backdrop-filter: blur(10px);
    z-index: 120;
    padding: 18px;
  }}
  .card{{
    width: min(880px, 96vw);
    border-radius: 26px;
    background: rgba(255,255,255,.82);
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
    font-weight: 980;
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
  .head{{ font-size: 24px; font-weight: 980; line-height: 1.08; color: rgba(65,15,40,.95); }}
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
    background: rgba(10, 20, 40, .6);
    backdrop-filter: blur(10px);
    z-index: 200;
    padding: 18px;
  }}
  .envelope{{
    width: min(560px, 94vw);
    border-radius: 26px;
    background: rgba(255,255,255,.86);
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
    font-weight: 980;
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
  .wishLine1{{ font-weight: 980; font-size: 16px; }}
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
        <div class="brandTop">Let's Travel Love Story ✈️💖 — Meera ❤ Zeel</div>
        <div class="brandSub">Tap any stop • gifts rain = surprise wishes</div>
      </div>
    </div>
    <div class="pill">
      <div class="tiny" id="counter">0 opened</div>
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
        <div class="nowTitle" id="nowTitle">Current: —</div>
        <div class="nowSub" id="nowSub">Tap any stop</div>
      </div>
      <div class="tiny">💝 Tap falling gifts too</div>
    </div>
  </div>

  <div class="overlay" id="overlay">
    <div class="card" id="card">
      <div class="cardTop">
        <div style="display:flex; gap:10px; align-items:center;">
          <div class="date" id="cDate"></div>
          <div style="font-weight:980; color:rgba(65,15,40,.90);" id="cSmall"></div>
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
          <div class="tiny" style="margin-top:auto;">(tap outside to close)</div>
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
    "May your love be sweet like chocolate 🍫 and warm like hugs 🤗💗"
  ];
  const GIFT_EMOJI = ["🎁","💝","🎁","💝","🎀"];

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

  const POS = [
    {{x:50, y:8}},
    {{x:40, y:15}},
    {{x:58, y:22}},
    {{x:44, y:30}},
    {{x:62, y:38}},
    {{x:48, y:46}},
    {{x:64, y:54}},
    {{x:46, y:62}},
    {{x:60, y:70}},
    {{x:45, y:78}},
    {{x:62, y:86}},
    {{x:50, y:93}},
    {{x:55, y:97}},
  ].slice(0, STAGES.length);

  let idx = 0;
  let planePos = {{ x: Math.max(6, POS[0].x - 12), y: POS[0].y }};
  let anim = null;

  function updateCounter(){{
    counter.textContent = `${{opened.size}} / ${{STAGES.length}} opened`;
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

    const btn = stopsLayer.querySelectorAll(".stop")[idx];
    if(btn) btn.classList.add("opened");

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
    nowTitle.textContent = `Current: Stop ${{idx+1}} — ${{s.title}}`;
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
          setTimeout(()=> openMemory(), 260);
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
      b.addEventListener("click", ()=>{{
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
    for(let i=0;i<18;i++){{
      const p = document.createElement("div");
      p.className = "burst";
      p.style.left = clientX + "px";
      p.style.top  = clientY + "px";
      p.style.setProperty("--dx", ((Math.random()*260)-130) + "px");
      p.style.setProperty("--dy", ((Math.random()*220)-110) + "px");
      document.body.appendChild(p);
      setTimeout(()=> p.remove(), 900);
    }}
  }}

  function spawnFallingGift(){{
    const g = document.createElement("div");
    g.className = "giftFall";
    g.style.left = (Math.random()*100) + "vw";
    g.style.animationDuration = (3.8 + Math.random()*3.6) + "s";
    g.innerHTML = `<div style="font-size:22px;">${{GIFT_EMOJI[Math.floor(Math.random()*GIFT_EMOJI.length)]}}</div>`;
    g.addEventListener("click", (e)=>{{
      e.stopPropagation();
      blastAt(e.clientX, e.clientY);
      openWish();
      g.remove();
    }});
    document.body.appendChild(g);
    setTimeout(()=> g.remove(), 9000);
  }}
  setInterval(spawnFallingGift, 700);

  // Init
  buildStops();
  plane.style.left = planePos.x + "%";
  plane.style.top  = planePos.y + "%";
  nowTitle.textContent = `Current: Stop 1 — ${{STAGES[0].title}}`;
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
    "• Click on station dots to fly the plane\n"
    "• Click on falling gifts for surprise wishes\n"
    "• Each stop opens a memory with photo\n"
    "• Beautiful light blue wave background"
)
    width:fit-content;
  }}
  
  h2 {{ margin:4px 0 0; font-size:17px; line-height:1.15; color:rgba(255,255,255,0.9); }}
  p {{ margin:0; color: rgba(255,255,255,0.6); font-size:12px; line-height:1.4; }}

  .gift-area {{
    margin-top:4px;
    display:flex;
    justify-content:center;
    align-items:center;
    min-height:180px;
    position:relative;
  }}
  
  .gift-btn {{
    width:130px;
    height:130px;
    border:0;
    background:transparent;
    cursor:pointer;
    position:relative;
    transition: transform 0.3s ease;
    filter: drop-shadow(0 10px 30px rgba(0,0,0,0.2));
  }}
  
  .gift-btn:hover {{
    transform: scale(1.08);
  }}
  
  .gift-box {{
    width:100%;
    height:100%;
    position:relative;
    transition: all 0.5s ease;
  }}
  
  .box-base {{
    position:absolute;
    left:20px;
    right:20px;
    bottom:15px;
    height:72px;
    border-radius:12px;
    background: linear-gradient(180deg, rgba(255,215,0,0.2), rgba(255,180,0,0.1));
    border:2px solid rgba(255,215,0,0.25);
    box-shadow: inset 0 2px 20px rgba(255,215,0,0.05);
  }}
  
  .box-lid {{
    position:absolute;
    left:14px;
    right:14px;
    bottom:70px;
    height:42px;
    border-radius:12px;
    background: linear-gradient(180deg, rgba(255,215,0,0.25), rgba(255,180,0,0.15));
    border:2px solid rgba(255,215,0,0.3);
    transform-origin:left bottom;
    transition: transform 0.7s cubic-bezier(.2,.9,.2,1);
  }}
  
  .ribbon-v {{
    position:absolute;
    left:50%;
    transform:translateX(-50%);
    bottom:15px;
    width:14px;
    height:98px;
    border-radius:999px;
    background: linear-gradient(180deg, rgba(255,50,50,0.8), rgba(200,50,200,0.8));
    opacity:0.9;
  }}
  
  .ribbon-h {{
    position:absolute;
    left:20px;
    right:20px;
    bottom:46px;
    height:14px;
    border-radius:999px;
    background: linear-gradient(90deg, rgba(255,50,50,0.8), rgba(200,50,200,0.8));
    opacity:0.9;
  }}
  
  .bow {{
    position:absolute;
    left:50%;
    bottom:98px;
    transform:translateX(-50%);
    width:44px;
    height:24px;
    display:flex;
    gap:4px;
    align-items:center;
    justify-content:center;
  }}
  
  .bow span {{
    width:20px;
    height:16px;
    border-radius:999px 999px 999px 6px;
    background: linear-gradient(135deg, rgba(255,50,50,0.8), rgba(200,50,200,0.8));
    transform: rotate(12deg);
    border:1px solid rgba(255,255,255,0.1);
  }}
  
  .bow span:last-child {{
    border-radius:999px 999px 6px 999px;
    background: linear-gradient(225deg, rgba(255,50,50,0.8), rgba(200,50,200,0.8));
    transform: rotate(-12deg);
  }}

  .opened .box-lid {{
    transform: rotate(-48deg) translate(-4px,-4px);
    border-color: rgba(255,215,0,0.5);
  }}
  
  .opened .box-base {{
    border-color: rgba(255,215,0,0.5);
    background: linear-gradient(180deg, rgba(255,215,0,0.3), rgba(255,180,0,0.2));
  }}

  /* Gift opening animation */
  .gift-box.falling {{
    animation: giftFall 0.8s ease forwards;
  }}
  
  @keyframes giftFall {{
    0% {{ transform: translateY(-100px) rotate(-15deg); opacity:0; }}
    60% {{ transform: translateY(8px) rotate(3deg); opacity:1; }}
    80% {{ transform: translateY(-4px) rotate(-2deg); }}
    100% {{ transform: translateY(0) rotate(0deg); opacity:1; }}
  }}

  /* Burst effects */
  .burst-layer {{
    position:absolute;
    inset:0;
    pointer-events:none;
    overflow:hidden;
    z-index:10;
  }}
  
  .burst-particle {{
    position:absolute;
    width:8px;
    height:8px;
    border-radius:50%;
    animation: burstOut 1.2s ease forwards;
  }}
  
  @keyframes burstOut {{
    0% {{ transform: translate(0,0) scale(1); opacity:1; }}
    100% {{ transform: translate(var(--dx), var(--dy)) scale(0); opacity:0; }}
  }}

  .heart-particle {{
    position:absolute;
    font-size:20px;
    animation: heartFloat 1.5s ease forwards;
  }}
  
  @keyframes heartFloat {{
    0% {{ transform: translate(0,0) scale(1) rotate(0deg); opacity:1; }}
    100% {{ transform: translate(var(--dx), var(--dy)) scale(0.5) rotate(720deg); opacity:0; }}
  }}

  /* Love message popup */
  .love-msg {{
    position:fixed;
    top:50%;
    left:50%;
    transform:translate(-50%,-50%) scale(0);
    z-index:100;
    background: rgba(20,20,40,0.92);
    backdrop-filter: blur(20px);
    border: 2px solid rgba(255,215,0,0.3);
    border-radius:24px;
    padding:30px 40px;
    max-width:500px;
    text-align:center;
    box-shadow: 0 30px 100px rgba(0,0,0,0.6);
    pointer-events:none;
    transition: all 0.5s cubic-bezier(.4,0,.2,1);
  }}
  
  .love-msg.show {{
    transform:translate(-50%,-50%) scale(1);
  }}
  
  .love-msg .msg-text {{
    color: rgba(255,255,255,0.95);
    font-size:20px;
    font-weight:700;
    line-height:1.6;
    text-shadow: 0 2px 20px rgba(255,215,0,0.2);
  }}
  
  .love-msg .msg-hearts {{
    font-size:30px;
    margin-top:10px;
    animation: heartBeat 1s ease infinite;
  }}
  
  @keyframes heartBeat {{
    0%, 100% {{ transform: scale(1); }}
    50% {{ transform: scale(1.2); }}
  }}

  /* Modal */
  .modal-back {{
    position:fixed;
    inset:0;
    display:none;
    z-index:50;
    background: rgba(0,0,0,0.6);
    backdrop-filter: blur(8px);
    align-items:center;
    justify-content:center;
    padding:18px;
  }}
  
  .modal {{
    width: min(520px, 94vw);
    border-radius:20px;
    border: 1px solid rgba(255,255,255,0.15);
    background: linear-gradient(135deg, rgba(20,30,50,0.9), rgba(30,20,40,0.9));
    box-shadow: 0 30px 90px rgba(0,0,0,0.5);
    overflow:hidden;
    animation: modalIn 0.4s ease;
  }}
  
  @keyframes modalIn {{
    from {{ transform: scale(0.9) translateY(20px); opacity:0; }}
    to {{ transform: scale(1) translateY(0); opacity:1; }}
  }}
  
  .modal-top {{
    display:flex;
    align-items:center;
    justify-content:space-between;
    gap:12px;
    padding:12px 16px;
    background: rgba(255,255,255,0.05);
    border-bottom: 1px solid rgba(255,255,255,0.08);
  }}
  
  .modal-top b {{ font-size:14px; color:rgba(255,255,255,0.9); }}
  
  .close-btn {{
    border:1px solid rgba(255,255,255,0.15);
    background: rgba(255,255,255,0.06);
    color:rgba(255,255,255,0.8);
    padding:6px 12px;
    border-radius:999px;
    cursor:pointer;
    font-weight:700;
    font-size:13px;
    transition: all 0.2s ease;
  }}
  
  .close-btn:hover {{ background: rgba(255,255,255,0.12); }}
  
  .modal-body {{
    padding:16px;
    display:flex;
    gap:14px;
    align-items:flex-start;
  }}
  
  .modal-icon {{
    font-size:60px;
    line-height:1;
    text-align:center;
    min-width:80px;
  }}
  
  .modal-text {{
    display:flex;
    flex-direction:column;
    gap:4px;
    flex:1;
  }}
  
  .modal-text .d {{ font-size:12px; color:rgba(255,255,255,0.5); }}
  .modal-text .t {{ font-size:18px; font-weight:900; color:rgba(255,255,255,0.95); line-height:1.2; }}
  .modal-text .p {{ font-size:13px; color:rgba(255,255,255,0.7); line-height:1.4; }}
</style>
</head>
<body>
  <!-- Waves Background -->
  <div class="waves-container">
    <div class="wave"></div>
    <div class="wave"></div>
    <div class="wave"></div>
  </div>
  
  <!-- Particles -->
  <div class="particles" id="particles"></div>
  
  <!-- Floating Gifts -->
  <div class="gifts-container" id="giftsContainer"></div>

  <!-- Road -->
  <div class="road-container">
    <div class="road">
      <div class="road-wave"></div>
    </div>
  </div>
  
  <!-- Stations -->
  <div class="stations" id="stations"></div>

  <!-- HUD -->
  <div class="hud">
    <div class="pill">
      <div class="title">🎁 Open gifts to unlock stages</div>
      <div class="tiny" id="counter">0 / {len(stages)} opened</div>
    </div>
    <div class="pill">
      <button class="btn" id="left">⬅️</button>
      <button class="btn" id="right">➡️</button>
      <button class="btn" id="reset">↺</button>
    </div>
  </div>

  <!-- Progress -->
  <div class="wrap">
    <div class="track">
      <div class="progress" id="progress"></div>
      <div class="plane" id="plane">✈️</div>
    </div>
    <div class="journey" id="journey"></div>
  </div>

  <!-- Love Message Popup -->
  <div class="love-msg" id="loveMsg">
    <div class="msg-text" id="msgText">💕 Your love is beautiful!</div>
    <div class="msg-hearts">❤️💕💗</div>
  </div>

  <!-- Modal -->
  <div class="modal-back" id="modalBack">
    <div class="modal">
      <div class="modal-top">
        <b>💝 Memory Unlocked</b>
        <button class="close-btn" id="close">✕</button>
      </div>
      <div class="modal-body">
        <div class="modal-icon">💝</div>
        <div class="modal-text">
          <div class="d" id="mDate"></div>
          <div class="t" id="mHead"></div>
          <div class="p" id="mDesc"></div>
        </div>
      </div>
    </div>
  </div>

<script>
  const STAGES = {stages};
  const LOVE_MESSAGES = {love_messages};
  
  // State
  const KEY = "mz_valentine_opened_v2";
  let opened = new Set(JSON.parse(localStorage.getItem(KEY) || "[]"));
  let currentStageIndex = 0;

  // DOM refs
  const journey = document.getElementById("journey");
  const counter = document.getElementById("counter");
  const progress = document.getElementById("progress");
  const plane = document.getElementById("plane");
  const stationsContainer = document.getElementById("stations");
  const loveMsg = document.getElementById("loveMsg");
  const msgText = document.getElementById("msgText");

  // Create particles
  function createParticles() {{
    const container = document.getElementById("particles");
    for(let i=0;i<30;i++) {{
      const p = document.createElement("div");
      p.className = "particle";
      p.style.left = Math.random() * 100 + "%";
      p.style.animationDelay = Math.random() * 15 + "s";
      p.style.animationDuration = (10 + Math.random() * 20) + "s";
      container.appendChild(p);
    }}
  }}

  // Create floating gifts
  function createFloatingGifts() {{
    const container = document.getElementById("giftsContainer");
    const emojis = ["🎁", "💝", "💕", "❤️", "💗", "🎀"];
    for(let i=0;i<15;i++) {{
      const g = document.createElement("div");
      g.className = "floating-gift";
      g.textContent = emojis[i % emojis.length];
      g.style.left = Math.random() * 100 + "%";
      g.style.fontSize = (20 + Math.random() * 30) + "px";
      g.style.animationDelay = Math.random() * 10 + "s";
      g.style.animationDuration = (8 + Math.random() * 12) + "s";
      container.appendChild(g);
    }}
  }}

  function save() {{
    localStorage.setItem(KEY, JSON.stringify(Array.from(opened)));
    updateHUD();
  }}

  function updateHUD() {{
    const total = STAGES.length;
    const n = opened.size;
    counter.textContent = `${{n}} / ${{total}} opened`;
    const pct = total === 0 ? 0 : Math.round((n/total)*100);
    progress.style.width = pct + "%";
    plane.style.left = pct + "%";
    plane.textContent = pct >= 100 ? "🛬" : "✈️";
    
    // Update stations
    const stationDots = stationsContainer.querySelectorAll(".station");
    const activeIndex = Math.min(Math.floor((n/total) * (stationDots.length - 1)), stationDots.length - 1);
    stationDots.forEach((dot, i) => {{
      dot.classList.toggle("active", i <= activeIndex);
    }});
  }}

  // Fly plane to specific station
  function flyToStation(index) {{
    const total = STAGES.length;
    const pct = total === 0 ? 0 : Math.round((index/total) * 100);
    progress.style.width = pct + "%";
    plane.style.left = pct + "%";
    plane.classList.add("plane-flying");
    setTimeout(() => plane.classList.remove("plane-flying"), 500);
  }}

  // Show love message
  function showLoveMessage(msg) {{
    msgText.textContent = msg;
    loveMsg.classList.add("show");
    clearTimeout(loveMsg._timeout);
    loveMsg._timeout = setTimeout(() => {{
      loveMsg.classList.remove("show");
    }}, 4000);
  }}

  // Burst effect
  function burst(element) {{
    const colors = ["#ff6b6b", "#ffd93d", "#6bcb77", "#4d96ff", "#ff6bb5", "#a66bff"];
    const emojis = ["❤️", "💕", "💗", "✨", "🌟", "💫"];
    
    for(let i=0;i<20;i++) {{
      const p = document.createElement("div");
      p.className = "burst-particle";
      const angle = (Math.PI * 2 * i) / 20;
      const dist = 80 + Math.random() * 120;
      p.style.setProperty("--dx", Math.cos(angle) * dist + "px");
      p.style.setProperty("--dy", Math.sin(angle) * dist + "px");
      p.style.background = colors[Math.floor(Math.random() * colors.length)];
      p.style.width = (4 + Math.random() * 6) + "px";
      p.style.height = p.style.width;
      p.style.animationDelay = Math.random() * 0.2 + "s";
      element.appendChild(p);
    }}
    
    for(let i=0;i<8;i++) {{
      const h = document.createElement("div");
      h.className = "heart-particle";
      h.textContent = emojis[i % emojis.length];
      const angle = (Math.PI * 2 * i) / 8 + Math.random() * 0.5;
      const dist = 60 + Math.random() * 80;
      h.style.setProperty("--dx", Math.cos(angle) * dist + "px");
      h.style.setProperty("--dy", Math.sin(angle) * dist - 50 + "px");
      h.style.animationDelay = Math.random() * 0.3 + "s";
      element.appendChild(h);
    }}
    
    setTimeout(() => element.innerHTML = "", 1800);
  }}

  // Modal
  const modalBack = document.getElementById("modalBack");
  const closeBtn = document.getElementById("close");
  const mDate = document.getElementById("mDate");
  const mHead = document.getElementById("mHead");
  const mDesc = document.getElementById("mDesc");

  function openModal(s) {{
    mDate.textContent = s.date;
    mHead.textContent = s.title;
    mDesc.textContent = s.desc;
    modalBack.style.display = "flex";
  }}
  
  function closeModal(){{ modalBack.style.display="none"; }}
  closeBtn.addEventListener("click", closeModal);
  modalBack.addEventListener("click", (e)=>{{ if(e.target === modalBack) closeModal(); }});

  // Create stations
  function createStations() {{
    stationsContainer.innerHTML = "";
    STAGES.forEach((s, i) => {{
      const div = document.createElement("div");
      div.className = "station";
      div.dataset.index = i;
      div.innerHTML = `
        <div class="dot"></div>
        <div class="label">${{i+1}}</div>
      `;
      div.addEventListener("click", () => {{
        // Fly to this station
        flyToStation(i);
        // Scroll to this stage
        const cards = journey.querySelectorAll(".stage");
        if(cards[i]) {{
          cards[i].scrollIntoView({{ behavior: "smooth", block: "center", inline: "center" }});
        }}
        // Update current
        currentStageIndex = i;
      }});
      stationsContainer.appendChild(div);
    }});
  }}

  function stageCard(s, idx) {{
    const card = document.createElement("div");
    card.className = "stage";
    card.dataset.stageId = s.id;

    const top = document.createElement("div");
    top.className = "row";
    top.innerHTML = `
      <div>
        <div class="badge">Stage ${{idx+1}} / ${{STAGES.length}}</div>
        <h2>${{s.title}}</h2>
        <p>${{s.desc}}</p>
      </div>
      <div class="badge">${{s.date}}</div>
    `;

    const giftArea = document.createElement("div");
    giftArea.className = "gift-area";

    const giftBtn = document.createElement("button");
    giftBtn.className = "gift-btn";

    const isOpen = opened.has(s.id);

    giftBtn.innerHTML = `
      <div class="gift-box ${{isOpen ? "opened" : "falling"}}">
        <div class="box-lid"></div>
        <div class="box-base"></div>
        <div class="ribbon-v"></div>
        <div class="ribbon-h"></div>
        <div class="bow"><span></span><span></span></div>
      </div>
    `;

    setTimeout(() => {{
      const box = giftBtn.querySelector(".gift-box");
      if(box) box.classList.remove("falling");
    }}, 900);

    const burstLayer = document.createElement("div");
    burstLayer.className = "burst-layer";

    giftBtn.addEventListener("click", ()=> {{
      const box = giftBtn.querySelector(".gift-box");
      
      if(!opened.has(s.id)) {{
        opened.add(s.id);
        box.classList.add("opened");
        burst(burstLayer);
        
        // Show random love message
        const msg = LOVE_MESSAGES[Math.floor(Math.random() * LOVE_MESSAGES.length)];
        showLoveMessage(msg);
        
        // Fly plane
        const total = STAGES.length;
        const pct = Math.round((opened.size/total) * 100);
        progress.style.width = pct + "%";
        plane.style.left = pct + "%";
        plane.classList.add("plane-flying");
        setTimeout(() => plane.classList.remove("plane-flying"), 500);
        
        save();
      }}
      
      openModal(s);
      
      // Auto scroll
      setTimeout(()=> {{
        const rect = card.getBoundingClientRect();
        const containerRect = journey.getBoundingClientRect();
        if(rect.right > containerRect.right - 50) {{
          journey.scrollBy({{left: 320, behavior:"smooth"}});
        }}
      }}, 400);
    }});

    giftArea.appendChild(giftBtn);
    giftArea.appendChild(burstLayer);

    card.appendChild(top);
    card.appendChild(giftArea);
    return card;
  }}

  function build() {{
    journey.innerHTML = "";
    STAGES.forEach((s,i)=> journey.appendChild(stageCard(s,i)));
    createStations();
    updateHUD();
  }}

  // Controls
  document.getElementById("left").addEventListener("click", ()=> {{
    const scrollAmount = 340;
    journey.scrollBy({{left: -scrollAmount, behavior:"smooth"}});
    // Update current station
    const cards = journey.querySelectorAll(".stage");
    let minDist = Infinity;
    let closest = 0;
    cards.forEach((c, i) => {{
      const rect = c.getBoundingClientRect();
      const dist = Math.abs(rect.left - window.innerWidth/2);
      if(dist < minDist) {{
        minDist = dist;
        closest = i;
      }}
    }});
    currentStageIndex = closest;
    flyToStation(closest);
  }});
  
  document.getElementById("right").addEventListener("click", ()=> {{
    const scrollAmount = 340;
    journey.scrollBy({{left: scrollAmount, behavior:"smooth"}});
    const cards = journey.querySelectorAll(".stage");
    let minDist = Infinity;
    let closest = 0;
    cards.forEach((c, i) => {{
      const rect = c.getBoundingClientRect();
      const dist = Math.abs(rect.left - window.innerWidth/2);
      if(dist < minDist) {{
        minDist = dist;
        closest = i;
      }}
    }});
    currentStageIndex = closest;
    flyToStation(closest);
    plane.classList.add("plane-flying");
    setTimeout(() => plane.classList.remove("plane-flying"), 500);
  }});
  
  document.getElementById("reset").addEventListener("click", ()=> {{
    if(confirm("Reset all progress?")) {{
      localStorage.removeItem(KEY);
      opened = new Set();
      build();
    }}
  }});

  // Init
  createParticles();
  createFloatingGifts();
  build();
</script>
</body>
</html>
"""

st.components.v1.html(html, height=780, scrolling=False)

st.info(
    "💝 **Meera & Zeel's Valentine Journey**\n\n"
    "• Click on gifts to unlock memories\n"
    "• Click on station dots to fly there\n"
    "• Watch the plane move along the road\n"
    "• Each gift gives a beautiful love message!"
)
