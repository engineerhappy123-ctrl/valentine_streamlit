import base64
from pathlib import Path
import streamlit as st

st.set_page_config(page_title="Meera ❤ Zeel — Valentine Journey", layout="wide")

ASSETS = Path(__file__).parent / "assets"

def b64(path: Path) -> str:
    data = path.read_bytes()
    return base64.b64encode(data).decode("utf-8")

# ----------------------------
# 1) UPDATE YOUR FILE NAMES HERE
# ----------------------------
background_files = [
    "bg1.jpg",
    "bg2.jpg",
    "bg3.jpg",
    "bg4.jpg",
    "bg5.jpg",
]

# Each stage: date text is shown BELOW in UI (not on photo)
stages = [
    dict(id="req",  date="(No date)", title="Instagram Request 💌",
         desc="Zeel sent request… Meera accepted ✅",
         ai="ai_00_request.png"),
    dict(id="d17",  date="17 Dec 2023", title="First Meet ✨",
         desc="Commerce Six Road Metro Station",
         ai="ai_01_17dec.png"),
    dict(id="d26",  date="26 Dec 2023", title="Second Date 😍",
         desc="Our second meet — more comfort, more smiles",
         ai="ai_02_26dec.png"),
    dict(id="jan6", date="06 Jan 2024", title="Ajay's Cafe ☕",
         desc="Coffee + talks + vibes",
         ai="ai_03_06jan.png"),
    dict(id="feb14",date="14 Feb 2024", title="Ahmedabad Gufa 💗",
         desc="Valentine day + Zeel met Hiral",
         ai="ai_04_14feb.png"),
    dict(id="mar6", date="06 Mar 2024", title="Parimal Garden 🌿",
         desc="First time exploring Parimal together",
         ai="ai_05_06mar.png"),
    dict(id="mar8", date="08 Mar 2024", title="First Kiss 😘",
         desc="A sweet moment that changed everything",
         ai="ai_06_08mar.png"),
    dict(id="mar28",date="28 Mar 2024", title="Cheek Bite 😂",
         desc="Funny-cute moment… Meera bit Zeel's cheek",
         ai="ai_07_28mar.png"),
    dict(id="mar29",date="29 Mar 2024", title="Bounce Up 🎉",
         desc="Meera + Zeel + Hiral + Ujjaval (Bounce Up)",
         ai="ai_08_29mar.png"),
    dict(id="mar30",date="30 Mar 2024", title="Parimal (Group) 🌳",
         desc="Meera + Zeel + Hiral + Ujjaval at Parimal",
         ai="ai_09_30mar.png"),
    dict(id="mar31",date="31 Mar 2024", title="Bye + Movie + Garden 🎬",
         desc="Bye to Hiral + movie seat + Parimal garden",
         ai="ai_10_31mar.png"),
    dict(id="apr5", date="05 Apr 2024", title="Parimal Again 💞",
         desc="Same place, new feelings",
         ai="ai_11_05apr.png"),
    dict(id="apr6", date="06 Apr 2024", title="Unlimited + Real Paprika 🍕",
         desc="179 salad vs 279 salad+pizza — love story started ❤️",
         ai="ai_12_06apr.png"),
]

# ----------------------------
# 2) Load assets as Base64 for HTML
# ----------------------------
bg_b64_list = []
for f in background_files:
    p = ASSETS / f
    if p.exists():
        bg_b64_list.append("data:image/jpeg;base64," + b64(p))

stage_payload = []
for s in stages:
    p = ASSETS / s["ai"]
    if p.exists():
        img_uri = "data:image/png;base64," + b64(p)
    else:
        img_uri = ""  # will show placeholder if missing
    stage_payload.append({**s, "img": img_uri})

# ----------------------------
# 3) Streamlit UI shell (title)
# ----------------------------
st.markdown(
    """
    <style>
      .block-container { padding-top: 0.8rem; padding-bottom: 0.8rem; }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("## ✈️ Meera ❤ Zeel — Valentine Journey (Game Style)")

# ----------------------------
# 4) Full animated frontend in one HTML
# ----------------------------
html = f"""
<!doctype html>
<html>
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1"/>
<style>
  :root {{
    --glass: rgba(255,255,255,.14);
    --stroke: rgba(255,255,255,.22);
    --text: rgba(255,255,255,.92);
    --muted: rgba(255,255,255,.72);
    --shadow: 0 18px 60px rgba(0,0,0,.35);
    --radius: 22px;
  }}
  *{{ box-sizing:border-box; }}
  body{{ margin:0; font-family: system-ui,-apple-system,Segoe UI,Roboto,Arial; color:var(--text); overflow:hidden; background:#0b0b16; }}

  /* Background with light blue theme */
  .bg{{ position:fixed; inset:0; z-index:-2; background: linear-gradient(135deg, #0a1628, #1a2a4a, #2a4a7a); overflow:hidden; }}
  .bg::after{{
    content:""; position:absolute; inset:0; z-index:2; pointer-events:none;
    background:
      radial-gradient(1200px 800px at 20% 10%, rgba(100,180,255,.15), transparent 60%),
      radial-gradient(900px 700px at 90% 30%, rgba(80,200,255,.12), transparent 60%),
      linear-gradient(to bottom, rgba(0,0,0,.2), rgba(0,0,0,.4));
  }}
  
  /* Road with station marks */
  .road{{ position:fixed; bottom:80px; left:0; right:0; z-index:1; }}
  .road-line{{
    position:relative;
    height:4px;
    background: rgba(100,200,255,.3);
    margin:0 20px;
    border-radius:2px;
    box-shadow: 0 0 20px rgba(100,200,255,.2);
  }}
  .road-line::before{{
    content:""; position:absolute; top:0; left:0; right:0; bottom:0;
    background: repeating-linear-gradient(90deg, rgba(100,200,255,.5) 0px, rgba(100,200,255,.5) 30px, transparent 30px, transparent 50px);
    border-radius:2px;
  }}
  
  .stations{{
    position:fixed; bottom:60px; left:0; right:0; z-index:3;
    display:flex; justify-content:space-around; padding:0 20px;
    pointer-events:none;
  }}
  .station{{
    display:flex; flex-direction:column; align-items:center; gap:4px;
    opacity:0.6;
    transition: all 0.5s ease;
  }}
  .station.active{{
    opacity:1;
  }}
  .station .dot{{
    width:14px; height:14px; border-radius:50%;
    background: radial-gradient(circle, rgba(150,220,255,.8), rgba(80,180,255,.4));
    border:2px solid rgba(150,220,255,.6);
    box-shadow: 0 0 20px rgba(100,200,255,.3);
    transition: all 0.5s ease;
  }}
  .station.active .dot{{
    background: radial-gradient(circle, rgba(255,200,100,.9), rgba(255,150,50,.6));
    border-color: rgba(255,200,100,.8);
    box-shadow: 0 0 30px rgba(255,200,100,.5);
    transform: scale(1.2);
  }}
  .station .label{{
    font-size:10px; color: rgba(255,255,255,.6);
    text-shadow: 0 2px 8px rgba(0,0,0,.5);
    font-weight:600;
    letter-spacing:0.5px;
    white-space:nowrap;
  }}
  .station.active .label{{
    color: rgba(255,255,255,.9);
  }}

  /* HUD */
  .hud{{
    position:fixed; left:14px; right:14px; top:10px; z-index:10;
    display:flex; gap:10px; justify-content:space-between; align-items:center;
  }}
  .pill{{
    backdrop-filter: blur(10px);
    background: rgba(255,255,255,.08);
    border: 1px solid rgba(255,255,255,.18);
    border-radius:999px;
    padding:10px 14px;
    box-shadow:0 10px 30px rgba(0,0,0,.25);
    display:flex; gap:10px; align-items:center;
    min-height:42px;
    white-space:nowrap;
  }}
  .title{{ font-weight:800; letter-spacing:.2px; font-size:14px; }}
  .tiny{{ font-size:12px; color:var(--muted); }}
  .btn{{
    cursor:pointer; user-select:none;
    border:1px solid rgba(255,255,255,.22);
    background: rgba(255,255,255,.08);
    color:var(--text);
    padding:9px 12px;
    border-radius:999px;
    font-weight:700;
    font-size:13px;
  }}
  .btn:hover{{ background: rgba(255,255,255,.16); }}

  /* Progress track with plane */
  .wrap{{ position:fixed; inset:0; padding-top:72px; padding-bottom:14px; display:flex; flex-direction:column; z-index:2; }}
  .track{{
    margin: 0 14px;
    height: 10px; border-radius:999px;
    background: rgba(255,255,255,.08);
    border: 1px solid rgba(255,255,255,.14);
    position: relative; overflow:hidden;
    box-shadow: inset 0 2px 10px rgba(0,0,0,.3);
  }}
  .progress{{ height:100%; width:0%; border-radius:999px;
    background: linear-gradient(90deg, rgba(255,105,180,.7), rgba(130,220,255,.7));
    transition: width .8s cubic-bezier(.4,0,.2,1);
  }}
  .plane{{
    position:absolute; top:50%; left:0%;
    transform: translate(-50%,-50%);
    transition: left .8s cubic-bezier(.4,0,.2,1);
    font-size:24px;
    filter: drop-shadow(0 4px 20px rgba(100,200,255,.4));
  }}
  .plane-fly{{
    animation: planeFly 0.3s ease;
  }}
  @keyframes planeFly{{
    0%{{ transform: translate(-50%,-50%) scale(1) rotate(0deg); }}
    25%{{ transform: translate(-50%,-70%) scale(1.1) rotate(-5deg); }}
    75%{{ transform: translate(-50%,-30%) scale(1.1) rotate(5deg); }}
    100%{{ transform: translate(-50%,-50%) scale(1) rotate(0deg); }}
  }}

  /* Journey cards */
  .journey{{
    flex:1;
    margin-top:30px;
    overflow-x:auto; overflow-y:hidden;
    display:flex; gap:16px;
    padding: 10px 14px 18px;
    scroll-snap-type:x mandatory;
    -webkit-overflow-scrolling: touch;
  }}
  .journey::-webkit-scrollbar{{ height:6px; }}
  .journey::-webkit-scrollbar-track{{ background: rgba(255,255,255,.05); border-radius:999px; }}
  .journey::-webkit-scrollbar-thumb{{ background: rgba(255,255,255,.15); border-radius:999px; }}

  .stage{{
    scroll-snap-align:start;
    min-width: min(86vw, 380px);
    max-width:380px;
    height:100%;
    border-radius: var(--radius);
    backdrop-filter: blur(12px);
    background: linear-gradient(180deg, rgba(255,255,255,.1), rgba(255,255,255,.05));
    border: 1px solid rgba(255,255,255,.15);
    box-shadow: var(--shadow);
    position: relative; overflow:hidden;
    padding:16px;
    display:flex; flex-direction:column; gap:10px;
  }}
  .stage::before{{
    content:""; position:absolute; inset:-60px; pointer-events:none;
    background:
      radial-gradient(600px 240px at 20% 20%, rgba(255,105,180,.15), transparent 55%),
      radial-gradient(600px 240px at 80% 30%, rgba(120,210,255,.12), transparent 55%);
    transform: rotate(8deg);
  }}
  .row{{ position:relative; display:flex; justify-content:space-between; gap:10px; }}
  .badge{{
    font-size:11px; color: rgba(255,255,255,.8);
    background: rgba(0,0,0,.25);
    border: 1px solid rgba(255,255,255,.12);
    border-radius:999px;
    padding:5px 10px; width:fit-content;
  }}
  h2{{ margin:6px 0 0; font-size:18px; line-height:1.15; }}
  p{{ margin:0; color: var(--muted); font-size:13px; line-height:1.5; }}

  /* Gift with falling animation */
  .giftArea{{ margin-top:6px; display:flex; justify-content:center; align-items:center; min-height:200px; position:relative; }}
  .giftBtn{{ width:150px; height:150px; border:0; background:transparent; cursor:pointer;
    filter: drop-shadow(0 18px 28px rgba(0,0,0,.35));
    position:relative;
    transition: transform 0.3s ease;
  }}
  .giftBtn:hover{{
    transform: scale(1.05);
  }}
  
  .gift{{
    width:100%; height:100%; position:relative;
    transition: all 0.5s ease;
  }}
  
  /* Gift box design */
  .boxBase{{ position:absolute; left:20px; right:20px; bottom:18px; height:82px; border-radius:14px;
    background: linear-gradient(180deg, rgba(255,215,0,.25), rgba(255,180,0,.15));
    border:2px solid rgba(255,215,0,.3);
    box-shadow: inset 0 2px 20px rgba(255,215,0,.1);
  }}
  .boxLid{{ position:absolute; left:14px; right:14px; bottom:80px; height:48px; border-radius:14px;
    background: linear-gradient(180deg, rgba(255,215,0,.3), rgba(255,180,0,.2));
    border:2px solid rgba(255,215,0,.35);
    transform-origin:left bottom;
    transition: transform .7s cubic-bezier(.2,.9,.2,1);
    box-shadow: inset 0 2px 20px rgba(255,215,0,.1);
  }}
  .ribbonV{{ position:absolute; left:50%; transform:translateX(-50%); bottom:18px; width:16px; height:112px; border-radius:999px;
    background: linear-gradient(180deg, rgba(255,50,50,.85), rgba(200,50,200,.85));
    opacity:.9;
    box-shadow: 0 0 20px rgba(255,50,50,.2);
  }}
  .ribbonH{{ position:absolute; left:20px; right:20px; bottom:52px; height:16px; border-radius:999px;
    background: linear-gradient(90deg, rgba(255,50,50,.85), rgba(200,50,200,.85));
    opacity:.9;
    box-shadow: 0 0 20px rgba(255,50,50,.2);
  }}
  .bow{{ position:absolute; left:50%; bottom:112px; transform:translateX(-50%); width:50px; height:28px; display:flex; gap:4px; align-items:center; justify-content:center; }}
  .bow span{{ width:22px; height:18px; border-radius:999px 999px 999px 6px; background: linear-gradient(135deg, rgba(255,50,50,.85), rgba(200,50,200,.85)); transform: rotate(12deg); border:1px solid rgba(255,255,255,.15); }}
  .bow span:last-child{{ border-radius:999px 999px 6px 999px; background: linear-gradient(225deg, rgba(255,50,50,.85), rgba(200,50,200,.85)); transform: rotate(-12deg); }}

  /* Best wishes text inside gift */
  .gift-wish{{
    position:absolute; top:50%; left:50%; transform:translate(-50%,-50%);
    font-size:11px; font-weight:800;
    color: rgba(255,215,0,.8);
    text-shadow: 0 2px 10px rgba(255,215,0,.2);
    opacity:0;
    transition: opacity 0.5s ease;
    text-align:center;
    line-height:1.3;
    letter-spacing:0.5px;
    z-index:5;
    pointer-events:none;
  }}
  .opened .gift-wish{{
    opacity:1;
  }}

  /* Gift opening animation - falling effect */
  .gift.falling{{
    animation: giftFall 0.8s ease forwards;
  }}
  @keyframes giftFall{{
    0%{{ transform: translateY(-120px) rotate(-10deg); opacity:0; }}
    60%{{ transform: translateY(10px) rotate(3deg); opacity:1; }}
    80%{{ transform: translateY(-5px) rotate(-2deg); }}
    100%{{ transform: translateY(0) rotate(0deg); opacity:1; }}
  }}
  
  .opened .boxLid{{
    transform: rotate(-48deg) translate(-6px,-6px);
    border-color: rgba(255,215,0,.5);
  }}
  .opened .boxBase{{
    border-color: rgba(255,215,0,.5);
    background: linear-gradient(180deg, rgba(255,215,0,.35), rgba(255,180,0,.2));
  }}

  /* Burst layer */
  .burstLayer{{ position:absolute; inset:0; pointer-events:none; overflow:hidden; z-index:10; }}
  .balloon{{ position:absolute; bottom:-40px; width:20px; height:26px; border-radius:999px;
    background: radial-gradient(circle, rgba(255,105,180,.8), rgba(200,50,150,.6));
    filter: drop-shadow(0 10px 18px rgba(0,0,0,.25));
    animation: floatUp 1.8s ease forwards;
    opacity:.9;
  }}
  .balloon::after{{ content:""; position:absolute; left:50%; bottom:-16px; width:1px; height:18px; background: rgba(255,255,255,.4);
    transform: translateX(-50%); opacity:.6;
  }}
  @keyframes floatUp{{ from{{ transform:translateY(0) translateX(0) scale(1); opacity:.9; }}
    to{{ transform:translateY(-280px) translateX(var(--dx)) scale(0.6); opacity:0; }} }}

  .conf{{ position:absolute; width:6px; height:10px; background: rgba(120,210,255,.9);
    top:45%; left:50%;
    transform: translate(-50%,-50%);
    animation: confetti 1.2s ease forwards;
    opacity:.9;
  }}
  @keyframes confetti{{ from{{ transform: translate(-50%,-50%) rotate(0deg); }}
    to{{ transform: translate(calc(-50% + var(--dx)), calc(-50% + var(--dy))) rotate(720deg); opacity:0; }} }}

  /* Modal */
  .modalBack{{
    position:fixed; inset:0; display:none; z-index:50;
    background: rgba(0,0,0,.6);
    backdrop-filter: blur(8px);
    align-items:center; justify-content:center;
    padding: 18px;
  }}
  .modal{{
    width: min(540px, 94vw);
    border-radius: 22px;
    border: 1px solid rgba(255,255,255,.18);
    background: linear-gradient(135deg, rgba(20,30,50,.85), rgba(30,20,40,.85));
    box-shadow: 0 30px 90px rgba(0,0,0,.6);
    overflow:hidden;
    animation: modalIn 0.4s ease;
  }}
  @keyframes modalIn{{
    from{{ transform: scale(0.9) translateY(20px); opacity:0; }}
    to{{ transform: scale(1) translateY(0); opacity:1; }}
  }}
  .modalTop{{
    display:flex; align-items:center; justify-content:space-between; gap:12px;
    padding: 12px 16px;
    background: rgba(255,255,255,.06);
    border-bottom: 1px solid rgba(255,255,255,.1);
  }}
  .modalTop b{{ font-size:15px; }}
  .closeBtn{{ border:1px solid rgba(255,255,255,.18); background: rgba(255,255,255,.08);
    color: var(--text); padding: 7px 12px; border-radius: 999px; cursor:pointer; font-weight:800; font-size:13px; }}
  .closeBtn:hover{{ background: rgba(255,255,255,.15); }}
  .modalBody{{ padding: 16px; display:flex; gap:14px; align-items:flex-start; }}
  .modalImg{{ width: 130px; height: 130px; border-radius: 18px; object-fit:cover; border:1px solid rgba(255,255,255,.15); background: rgba(255,255,255,.06); }}
  .modalText{{ display:flex; flex-direction:column; gap:5px; min-width:0; flex:1; }}
  .modalText .d{{ font-size:12px; color: var(--muted); }}
  .modalText .t{{ font-size:19px; font-weight:900; line-height:1.1; }}
  .modalText .p{{ font-size:13px; color: rgba(255,255,255,.82); line-height:1.45; }}
</style>
</head>
<body>
  <!-- Background with light blue theme -->
  <div class="bg" id="bg">
    <img id="bgA" alt="background A" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover;opacity:0;transition:opacity 1.6s ease;z-index:1;"/>
    <img id="bgB" alt="background B" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover;opacity:0;transition:opacity 1.6s ease;z-index:1;"/>
  </div>

  <!-- Road with stations -->
  <div class="road">
    <div class="road-line"></div>
  </div>
  <div class="stations" id="stations"></div>

  <!-- HUD -->
  <div class="hud">
    <div class="pill">
      <div class="title">🎁 Open gifts to unlock stages</div>
      <div class="tiny" id="counter">0 / {len(stage_payload)} opened</div>
    </div>
    <div class="pill">
      <button class="btn" id="left">⬅️</button>
      <button class="btn" id="right">➡️</button>
      <button class="btn" id="reset">↺</button>
    </div>
  </div>

  <!-- Progress and Plane -->
  <div class="wrap">
    <div class="track">
      <div class="progress" id="progress"></div>
      <div class="plane" id="plane">✈️</div>
    </div>

    <!-- Journey cards -->
    <div class="journey" id="journey"></div>
  </div>

  <!-- Modal -->
  <div class="modalBack" id="modalBack">
    <div class="modal">
      <div class="modalTop">
        <b id="mTitle">💝 Memory</b>
        <button class="closeBtn" id="close">✕</button>
      </div>
      <div class="modalBody">
        <img class="modalImg" id="mImg" src="" alt="memory"/>
        <div class="modalText">
          <div class="d" id="mDate"></div>
          <div class="t" id="mHead"></div>
          <div class="p" id="mDesc"></div>
        </div>
      </div>
    </div>
  </div>

<script>
  const BG = {bg_b64_list};
  const STAGES = {stage_payload};

  // State in localStorage
  const KEY = "mz_streamlit_valentine_opened_v1";
  let opened = new Set(JSON.parse(localStorage.getItem(KEY) || "[]"));

  const journey = document.getElementById("journey");
  const counter = document.getElementById("counter");
  const progress = document.getElementById("progress");
  const plane = document.getElementById("plane");
  const stationsContainer = document.getElementById("stations");

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

  function rand(min,max){{ return Math.random()*(max-min)+min; }}

  function celebrate(layer) {{
    layer.innerHTML = "";
    // Balloons
    for(let i=0;i<8;i++) {{
      const b = document.createElement("div");
      b.className = "balloon";
      b.style.left = rand(8,92) + "%";
      b.style.setProperty("--dx", rand(-50,50) + "px");
      b.style.animationDelay = rand(0,0.3) + "s";
      layer.appendChild(b);
    }}
    // Confetti
    for(let i=0;i<14;i++) {{
      const c = document.createElement("div");
      c.className = "conf";
      c.style.left = rand(30,70) + "%";
      c.style.top = rand(30,55) + "%";
      c.style.setProperty("--dx", rand(-160,160) + "px");
      c.style.setProperty("--dy", rand(-140,140) + "px");
      c.style.animationDelay = rand(0,0.2) + "s";
      layer.appendChild(c);
    }}
    setTimeout(()=> layer.innerHTML="", 1800);
  }}

  // Modal
  const modalBack = document.getElementById("modalBack");
  const closeBtn = document.getElementById("close");
  const mTitle = document.getElementById("mTitle");
  const mImg = document.getElementById("mImg");
  const mDate = document.getElementById("mDate");
  const mHead = document.getElementById("mHead");
  const mDesc = document.getElementById("mDesc");

  function openModal(s) {{
    mTitle.textContent = "💝 Unlocked Memory";
    mImg.src = s.img || "";
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
      div.innerHTML = `
        <div class="dot"></div>
        <div class="label">${i+1}</div>
      `;
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
        <div class="badge">Stage ${idx+1} / ${STAGES.length}</div>
        <h2>${s.title}</h2>
        <p>${s.desc}</p>
      </div>
      <div class="badge">${s.date}</div>
    `;

    const giftArea = document.createElement("div");
    giftArea.className = "giftArea";

    const giftBtn = document.createElement("button");
    giftBtn.className = "giftBtn";

    const isOpen = opened.has(s.id);

    giftBtn.innerHTML = `
      <div class="gift ${{isOpen ? "opened" : "falling"}}">
        <div class="boxLid"></div>
        <div class="boxBase"></div>
        <div class="ribbonV"></div>
        <div class="ribbonH"></div>
        <div class="bow"><span></span><span></span></div>
        <div class="gift-wish">❤️ Best<br>Wishes ❤️</div>
      </div>
    `;

    // Remove falling animation after it plays
    setTimeout(() => {{
      const giftDiv = giftBtn.querySelector(".gift");
      if(giftDiv) giftDiv.classList.remove("falling");
    }}, 900);

    const burst = document.createElement("div");
    burst.className = "burstLayer";

    giftBtn.addEventListener("click", ()=> {{
      const giftDiv = giftBtn.querySelector(".gift");
      
      // If not opened, open it with celebration
      if(!opened.has(s.id)) {{
        opened.add(s.id);
        giftDiv.classList.add("opened");
        celebrate(burst);
        save();
        
        // Plane fly effect
        plane.classList.add("plane-fly");
        setTimeout(() => plane.classList.remove("plane-fly"), 400);
      }}
      
      // Show modal
      openModal(s);

      // Auto scroll to next
      setTimeout(()=> {{
        const rect = card.getBoundingClientRect();
        const containerRect = journey.getBoundingClientRect();
        if(rect.right > containerRect.right - 50) {{
          journey.scrollBy({{left: 340, behavior:"smooth"}});
        }}
      }}, 400);
    }});

    giftArea.appendChild(giftBtn);
    giftArea.appendChild(burst);

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
  document.getElementById("left").addEventListener("click", ()=> journey.scrollBy({{left:-360, behavior:"smooth"}}));
  document.getElementById("right").addEventListener("click", ()=> {{
    journey.scrollBy({{left:360, behavior:"smooth"}});
    plane.classList.add("plane-fly");
    setTimeout(() => plane.classList.remove("plane-fly"), 400);
  }});
  document.getElementById("reset").addEventListener("click", ()=> {{
    localStorage.removeItem(KEY);
    opened = new Set();
    build();
  }});

  // Background slideshow
  const bgA = document.getElementById("bgA");
  const bgB = document.getElementById("bgB");
  let bgIndex = 0;
  let showingA = true;

  function nextBg() {{
    if(!BG || BG.length===0) return;
    const src = BG[bgIndex % BG.length];
    bgIndex++;

    const showEl = showingA ? bgA : bgB;
    const hideEl = showingA ? bgB : bgA;

    showEl.src = src;
    showEl.style.opacity = "1";
    hideEl.style.opacity = "0";
    showingA = !showingA;
  }}

  // Initialize
  build();
  nextBg();
  setInterval(nextBg, 6500);
</script>
</body>
</html>
"""

st.components.v1.html(html, height=760, scrolling=False)

st.info(
    "✅ Tip: Replace only filenames in `background_files` and `stages` list. "
    "No date is written on photos — date is shown only in the modal + stage badge."
)
