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
    dict(id="jan6", date="06 Jan 2024", title="Ajay’s Cafe ☕",
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
         desc="Funny-cute moment… Meera bit Zeel’s cheek",
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
  body{{ margin:0; font-family: system-ui,-apple-system,Segoe UI,Roboto,Arial; color:var(--text); overflow:hidden; }}

  /* Background slideshow */
  .bg{{ position:fixed; inset:0; z-index:-2; background:#0b0b16; overflow:hidden; }}
  .bg::after{{
    content:""; position:absolute; inset:0; z-index:2; pointer-events:none;
    background:
      radial-gradient(1200px 800px at 20% 10%, rgba(255,105,180,.22), transparent 60%),
      radial-gradient(900px 700px at 90% 30%, rgba(100,200,255,.18), transparent 60%),
      linear-gradient(to bottom, rgba(0,0,0,.25), rgba(0,0,0,.55));
  }}
  .bg img{{
    position:absolute; inset:0; width:100%; height:100%; object-fit:cover;
    opacity:0; transform:scale(1.04);
    transition: opacity 1.6s ease, transform 7.5s ease;
    z-index:1;
  }}
  .bg img.show{{ opacity:1; transform:scale(1.12); }}

  /* HUD */
  .hud{{
    position:fixed; left:14px; right:14px; top:10px; z-index:10;
    display:flex; gap:10px; justify-content:space-between; align-items:center;
  }}
  .pill{{
    backdrop-filter: blur(10px);
    background: rgba(255,255,255,.10);
    border: 1px solid rgba(255,255,255,.20);
    border-radius:999px;
    padding:10px 14px;
    box-shadow:0 10px 30px rgba(0,0,0,.25);
    display:flex; gap:10px; align-items:center;
    min-height:42px;
    white-space:nowrap;
  }}
  .title{{ font-weight:800; letter-spacing:.2px; }}
  .tiny{{ font-size:12px; color:var(--muted); }}
  .btn{{
    cursor:pointer; user-select:none;
    border:1px solid rgba(255,255,255,.22);
    background: rgba(255,255,255,.10);
    color:var(--text);
    padding:9px 12px;
    border-radius:999px;
    font-weight:700;
  }}
  .btn:hover{{ background: rgba(255,255,255,.16); }}

  /* Progress track */
  .wrap{{ position:fixed; inset:0; padding-top:72px; padding-bottom:14px; display:flex; flex-direction:column; }}
  .track{{
    margin: 0 14px;
    height: 10px; border-radius:999px;
    background: rgba(255,255,255,.12);
    border: 1px solid rgba(255,255,255,.18);
    position: relative; overflow:hidden;
  }}
  .progress{{ height:100%; width:0%; border-radius:999px;
    background: linear-gradient(90deg, rgba(255,105,180,.85), rgba(130,220,255,.85));
    transition: width .55s ease;
  }}
  .plane{{ position:absolute; top:50%; left:0%;
    transform: translate(-10px,-50%);
    transition: left .55s ease;
    font-size:18px;
    filter: drop-shadow(0 6px 14px rgba(0,0,0,.35));
  }}

  /* Horizontal journey */
  .journey{{
    flex:1;
    margin-top:12px;
    overflow-x:auto; overflow-y:hidden;
    display:flex; gap:16px;
    padding: 10px 14px 18px;
    scroll-snap-type:x mandatory;
    -webkit-overflow-scrolling: touch;
  }}
  .journey::-webkit-scrollbar{{ height:10px; }}
  .journey::-webkit-scrollbar-thumb{{ background: rgba(255,255,255,.18); border-radius:999px; }}

  .stage{{
    scroll-snap-align:start;
    min-width: min(86vw, 420px);
    max-width:420px;
    height:100%;
    border-radius: var(--radius);
    backdrop-filter: blur(12px);
    background: linear-gradient(180deg, rgba(255,255,255,.14), rgba(255,255,255,.08));
    border: 1px solid rgba(255,255,255,.20);
    box-shadow: var(--shadow);
    position: relative; overflow:hidden;
    padding:16px;
    display:flex; flex-direction:column; gap:10px;
  }}
  .stage::before{{
    content:""; position:absolute; inset:-60px; pointer-events:none;
    background:
      radial-gradient(600px 240px at 20% 20%, rgba(255,105,180,.25), transparent 55%),
      radial-gradient(600px 240px at 80% 30%, rgba(120,210,255,.22), transparent 55%);
    transform: rotate(8deg);
  }}
  .row{{ position:relative; display:flex; justify-content:space-between; gap:10px; }}
  .badge{{
    font-size:12px; color: rgba(255,255,255,.85);
    background: rgba(0,0,0,.22);
    border: 1px solid rgba(255,255,255,.16);
    border-radius:999px;
    padding:6px 10px; width:fit-content;
  }}
  h2{{ margin:6px 0 0; font-size:20px; line-height:1.15; }}
  p{{ margin:0; color: var(--muted); font-size:13px; line-height:1.5; }}

  /* Gift */
  .giftArea{{ margin-top:6px; display:flex; justify-content:center; align-items:center; min-height:220px; position:relative; }}
  .giftBtn{{ width:168px; height:168px; border:0; background:transparent; cursor:pointer;
    filter: drop-shadow(0 18px 28px rgba(0,0,0,.35));
  }}
  .gift{{ width:100%; height:100%; position:relative; }}
  .boxBase{{ position:absolute; left:20px; right:20px; bottom:18px; height:92px; border-radius:16px;
    background: linear-gradient(180deg, rgba(255,255,255,.18), rgba(255,255,255,.10));
    border:1px solid rgba(255,255,255,.22);
  }}
  .boxLid{{ position:absolute; left:14px; right:14px; bottom:88px; height:54px; border-radius:16px;
    background: linear-gradient(180deg, rgba(255,255,255,.20), rgba(255,255,255,.12));
    border:1px solid rgba(255,255,255,.22);
    transform-origin:left bottom;
    transition: transform .6s cubic-bezier(.2,.9,.2,1);
  }}
  .ribbonV{{ position:absolute; left:50%; transform:translateX(-50%); bottom:18px; width:20px; height:124px; border-radius:999px;
    background: linear-gradient(180deg, rgba(255,105,180,.85), rgba(120,210,255,.85));
    opacity:.92;
  }}
  .ribbonH{{ position:absolute; left:20px; right:20px; bottom:58px; height:20px; border-radius:999px;
    background: linear-gradient(90deg, rgba(255,105,180,.85), rgba(120,210,255,.85));
    opacity:.92;
  }}
  .bow{{ position:absolute; left:50%; bottom:124px; transform:translateX(-50%); width:58px; height:32px; display:flex; gap:6px; align-items:center; justify-content:center; }}
  .bow span{{ width:26px; height:22px; border-radius:999px 999px 999px 6px; background: rgba(255,105,180,.85); transform: rotate(12deg); border:1px solid rgba(255,255,255,.22); }}
  .bow span:last-child{{ border-radius:999px 999px 6px 999px; background: rgba(120,210,255,.85); transform: rotate(-12deg); }}

  .opened .boxLid{{ transform: rotate(-52deg) translate(-6px,-8px); }}

  /* Burst layer */
  .burstLayer{{ position:absolute; inset:0; pointer-events:none; overflow:hidden; }}
  .balloon{{ position:absolute; bottom:-40px; width:24px; height:30px; border-radius:999px;
    background: rgba(255,105,180,.85);
    filter: drop-shadow(0 10px 18px rgba(0,0,0,.25));
    animation: floatUp 1.5s ease forwards;
    opacity:.95;
  }}
  .balloon::after{{ content:""; position:absolute; left:50%; bottom:-18px; width:1px; height:22px; background: rgba(255,255,255,.5);
    transform: translateX(-50%); opacity:.65;
  }}
  @keyframes floatUp{{ from{{ transform:translateY(0) translateX(0); opacity:.95; }}
    to{{ transform:translateY(-260px) translateX(var(--dx)); opacity:0; }} }}

  .conf{{ position:absolute; width:8px; height:12px; background: rgba(120,210,255,.9);
    top:45%; left:50%;
    transform: translate(-50%,-50%);
    animation: confetti 1.1s ease forwards;
    opacity:.95;
  }}
  @keyframes confetti{{ from{{ transform: translate(-50%,-50%) rotate(0deg); }}
    to{{ transform: translate(calc(-50% + var(--dx)), calc(-50% + var(--dy))) rotate(540deg); opacity:0; }} }}

  /* Modal */
  .modalBack{{
    position:fixed; inset:0; display:none; z-index:50;
    background: rgba(0,0,0,.55);
    backdrop-filter: blur(6px);
    align-items:center; justify-content:center;
    padding: 18px;
  }}
  .modal{{
    width: min(560px, 96vw);
    border-radius: 22px;
    border: 1px solid rgba(255,255,255,.22);
    background: rgba(20,20,30,.72);
    box-shadow: 0 30px 90px rgba(0,0,0,.55);
    overflow:hidden;
  }}
  .modalTop{{
    display:flex; align-items:center; justify-content:space-between; gap:12px;
    padding: 12px 14px;
    background: rgba(255,255,255,.08);
    border-bottom: 1px solid rgba(255,255,255,.14);
  }}
  .modalTop b{{ font-size:14px; }}
  .closeBtn{{ border:1px solid rgba(255,255,255,.22); background: rgba(255,255,255,.10);
    color: var(--text); padding: 8px 10px; border-radius: 999px; cursor:pointer; font-weight:800; }}
  .modalBody{{ padding: 14px; display:flex; gap:12px; align-items:flex-start; }}
  .modalImg{{ width: 140px; height: 140px; border-radius: 20px; object-fit:cover; border:1px solid rgba(255,255,255,.18); background: rgba(255,255,255,.08); }}
  .modalText{{ display:flex; flex-direction:column; gap:6px; min-width:0; }}
  .modalText .d{{ font-size:12px; color: var(--muted); }}
  .modalText .t{{ font-size:18px; font-weight:900; line-height:1.1; }}
  .modalText .p{{ font-size:13px; color: rgba(255,255,255,.84); line-height:1.45; }}
</style>
</head>
<body>
  <div class="bg" id="bg">
    <img id="bgA" alt="background A"/>
    <img id="bgB" alt="background B"/>
  </div>

  <div class="hud">
    <div class="pill">
      <div class="title">🎁 Open gifts to unlock stages</div>
      <div class="tiny" id="counter">0 / {len(stage_payload)} opened</div>
    </div>
    <div class="pill">
      <button class="btn" id="left">⬅️</button>
      <button class="btn" id="right">➡️</button>
      <button class="btn" id="reset">Reset</button>
    </div>
  </div>

  <div class="wrap">
    <div class="track">
      <div class="progress" id="progress"></div>
      <div class="plane" id="plane">🛫</div>
    </div>

    <div class="journey" id="journey"></div>
  </div>

  <div class="modalBack" id="modalBack">
    <div class="modal">
      <div class="modalTop">
        <b id="mTitle">Memory</b>
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

  // State in localStorage (browser)
  const KEY = "mz_streamlit_valentine_opened_v1";
  let opened = new Set(JSON.parse(localStorage.getItem(KEY) || "[]"));

  const journey = document.getElementById("journey");
  const counter = document.getElementById("counter");
  const progress = document.getElementById("progress");
  const plane = document.getElementById("plane");

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
    plane.textContent = pct >= 100 ? "🛬" : (pct >= 60 ? "✈️" : "🛫");
  }}

  function rand(min,max){{ return Math.random()*(max-min)+min; }}

  function celebrate(layer) {{
    layer.innerHTML = "";
    for(let i=0;i<10;i++) {{
      const b = document.createElement("div");
      b.className = "balloon";
      b.style.left = rand(8,92) + "%";
      b.style.setProperty("--dx", rand(-60,60) + "px");
      layer.appendChild(b);
    }}
    for(let i=0;i<18;i++) {{
      const c = document.createElement("div");
      c.className = "conf";
      c.style.left = rand(35,65) + "%";
      c.style.top = rand(35,55) + "%";
      c.style.setProperty("--dx", rand(-180,180) + "px");
      c.style.setProperty("--dy", rand(-160,160) + "px");
      layer.appendChild(c);
    }}
    setTimeout(()=> layer.innerHTML="", 1600);
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
    mTitle.textContent = "Unlocked Memory 💝";
    mImg.src = s.img || "";
    mDate.textContent = s.date;
    mHead.textContent = s.title;
    mDesc.textContent = s.desc;
    modalBack.style.display = "flex";
  }}
  function closeModal(){{ modalBack.style.display="none"; }}
  closeBtn.addEventListener("click", closeModal);
  modalBack.addEventListener("click", (e)=>{{ if(e.target === modalBack) closeModal(); }});

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
      <div class="gift ${isOpen ? "opened" : ""}">
        <div class="boxLid"></div>
        <div class="boxBase"></div>
        <div class="ribbonV"></div>
        <div class="ribbonH"></div>
        <div class="bow"><span></span><span></span></div>
      </div>
    `;

    const burst = document.createElement("div");
    burst.className = "burstLayer";

    giftBtn.addEventListener("click", ()=> {{
      // open animation + celebration
      celebrate(burst);

      if(!opened.has(s.id)) {{
        opened.add(s.id);
        giftBtn.querySelector(".gift").classList.add("opened");
        save();
      }}
      // show modal with AI image + event (NO text on image)
      openModal(s);

      // game feel: move forward
      setTimeout(()=> journey.scrollBy({{left: 320, behavior:"smooth"}}), 500);
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
    updateHUD();
  }}

  // Controls
  document.getElementById("left").addEventListener("click", ()=> journey.scrollBy({{left:-360, behavior:"smooth"}}));
  document.getElementById("right").addEventListener("click", ()=> journey.scrollBy({{left:360, behavior:"smooth"}}));
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
    showEl.classList.add("show");
    hideEl.classList.remove("show");
    showingA = !showingA;
  }}

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
