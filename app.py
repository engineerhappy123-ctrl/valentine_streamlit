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
    padding:4px 10px;
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
