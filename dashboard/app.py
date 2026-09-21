import streamlit as st
import pandas as pd
import joblib
from streamlit_autorefresh import st_autorefresh

# =========================================================
# PAGE CONFIGURATION
# =========================================================
st.set_page_config(
    page_title="Smart AI Health Monitoring Toilet",
    page_icon="●",
    layout="wide",
    initial_sidebar_state="expanded",
)

# =========================================================
# AUTO REFRESH
# =========================================================
st_autorefresh(interval=3000, key="sensor_refresh")

# =========================================================
# FUTURISTIC GLASS / 3D UI
# =========================================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background:
        radial-gradient(circle at 75% 8%, rgba(0,210,255,.13), transparent 28%),
        radial-gradient(circle at 20% 35%, rgba(115,70,255,.10), transparent 30%),
        linear-gradient(135deg, #050816 0%, #081020 52%, #0a1020 100%);
    color: #eef6ff;
}

.block-container {
    max-width: 1550px;
    padding: 1.2rem 2.2rem 3rem;
}

header[data-testid="stHeader"] {
    background: transparent;
}

section[data-testid="stSidebar"] {
    display: block;
    background: linear-gradient(180deg, rgba(7,13,27,.98), rgba(5,10,21,.98));
    border-right: 1px solid rgba(80,170,255,.12);
}
section[data-testid="stSidebar"] > div {
    padding-top: 1.4rem;
}
.sidebar-logo {
    width: 46px;
    height: 46px;
    border-radius: 14px;
    display:flex;
    align-items:center;
    justify-content:center;
    background: linear-gradient(135deg,#16d9ff,#765cff);
    box-shadow: 0 0 28px rgba(22,217,255,.24);
    font-size: 22px;
    font-weight: 900;
}
.sidebar-title {
    font-size: 16px;
    font-weight: 800;
    margin-top: 10px;
}
.sidebar-sub {
    color:#6e7e99;
    font-size:10px;
    letter-spacing:1.4px;
    margin-top:4px;
}
.sidebar-nav {
    margin-top: 30px;
    color:#7e8da7;
    font-size:10px;
    letter-spacing:1.7px;
    font-weight:800;
}
.sidebar-item {
    margin-top:8px;
    padding:11px 12px;
    border-radius:12px;
    color:#b7c4d8;
    background:rgba(255,255,255,.025);
    border:1px solid transparent;
}
.sidebar-item.active {
    color:#eafaff;
    border-color:rgba(31,220,255,.20);
    background:linear-gradient(90deg,rgba(24,216,255,.12),rgba(111,88,255,.08));
}
.sidebar-foot {
    margin-top:30px;
    padding:12px;
    border:1px solid rgba(120,145,190,.12);
    border-radius:14px;
    background:rgba(255,255,255,.025);
    color:#71819a;
    font-size:10px;
    line-height:1.6;
}

/* Hide default Streamlit decoration */
#MainMenu, footer {visibility: hidden;}
div[data-testid="stToolbar"] {visibility: hidden; height: 0;}
div[data-testid="stDecoration"] {visibility: hidden;}

.stApp::before {
    content:"";
    position:fixed;
    inset:-30%;
    pointer-events:none;
    background:
        radial-gradient(circle at 55% 35%, rgba(18,220,255,.055), transparent 20%),
        radial-gradient(circle at 75% 70%, rgba(119,87,255,.05), transparent 24%);
    animation:ambient 12s ease-in-out infinite alternate;
    z-index:0;
}
@keyframes ambient {
    from { transform:translate3d(-1%, -1%, 0) scale(1); }
    to { transform:translate3d(1%, 1%, 0) scale(1.04); }
}
.block-container { position:relative; z-index:1; }

/* Top banner */
.preview-banner {
    padding: 10px 16px;
    border: 1px solid rgba(0,220,255,.30);
    border-radius: 12px;
    background: rgba(6,19,35,.75);
    color: #9feaff;
    font-size: 12px;
    letter-spacing: .5px;
    margin-bottom: 18px;
}

/* Header */
.brand-row {
    display:flex;
    align-items:center;
    justify-content:space-between;
    gap:20px;
    margin-bottom: 18px;
}

.brand {
    display:flex;
    align-items:center;
    gap:14px;
}

.brand-icon {
    width:52px;
    height:52px;
    border-radius:16px;
    display:flex;
    align-items:center;
    justify-content:center;
    background:linear-gradient(135deg,#19d8ff,#7c5cff);
    box-shadow:0 0 35px rgba(35,190,255,.28);
    color:white;
    font-size:25px;
    font-weight:800;
}

.brand-title {
    font-size:22px;
    font-weight:800;
    line-height:1.05;
}

.brand-sub {
    color:#72819b;
    font-size:11px;
    letter-spacing:1.5px;
    margin-top:5px;
}

.live-pill {
    padding:9px 15px;
    border-radius:999px;
    border:1px solid rgba(0,240,180,.28);
    background:rgba(0,190,140,.08);
    color:#59f2c4;
    font-size:12px;
    font-weight:700;
}

/* Hero */
.hero {
    position:relative;
    min-height:560px;
    overflow:hidden;
    border:1px solid rgba(135,160,205,.20);
    border-radius:28px;
    background:
        radial-gradient(circle at 65% 32%, rgba(25,210,255,.12), transparent 23%),
        linear-gradient(145deg, rgba(20,29,51,.92), rgba(9,15,30,.94));
    box-shadow:
        inset 0 1px 0 rgba(255,255,255,.06),
        0 25px 70px rgba(0,0,0,.32);
    margin-bottom:22px;
}

.hero-copy {
    position:absolute;
    left:38px;
    bottom:34px;
    z-index:4;
    max-width:720px;
}

.eyebrow {
    color:#35dfff;
    font-size:12px;
    font-weight:800;
    letter-spacing:3px;
    margin-bottom:12px;
}

.hero-title {
    font-size:44px;
    line-height:1.05;
    font-weight:800;
    margin:0;
}

.hero-title span {
    background:linear-gradient(90deg,#21d8ff,#8e7bff);
    -webkit-background-clip:text;
    color:transparent;
}

.hero-desc {
    color:#8d9bb3;
    font-size:15px;
    line-height:1.7;
    margin-top:14px;
    max-width:650px;
}

/* 3D pod */
.pod-stage {
    position:absolute;
    right:8%;
    top:40px;
    width:500px;
    height:410px;
}

.orbit {
    position:absolute;
    left:50%;
    top:50%;
    width:380px;
    height:380px;
    transform:translate(-50%,-50%);
    border:1px dashed rgba(25,215,255,.22);
    border-radius:50%;
    animation:spin 18s linear infinite;
}

.orbit:before, .orbit:after {
    content:"";
    position:absolute;
    width:9px;
    height:9px;
    border-radius:50%;
    background:#28ddff;
    box-shadow:0 0 16px #28ddff;
}

.orbit:before { left:42px; top:35px; }
.orbit:after { right:20px; bottom:62px; background:#8c6cff; box-shadow:0 0 16px #8c6cff; }

.pod {
    position:absolute;
    left:50%;
    top:50%;
    width:178px;
    height:250px;
    transform:translate(-50%,-50%);
    border-radius:78px 78px 58px 58px;
    background:linear-gradient(145deg, rgba(46,61,79,.78), rgba(12,24,40,.96));
    border:1px solid rgba(190,220,255,.25);
    box-shadow:
        inset 10px 10px 22px rgba(255,255,255,.07),
        inset -12px -15px 25px rgba(0,0,0,.45),
        0 25px 55px rgba(0,0,0,.35),
        0 0 50px rgba(22,210,255,.10);
}

.pod:before {
    content:"";
    position:absolute;
    left:22px;
    right:22px;
    top:20px;
    height:118px;
    border-radius:58px 58px 35px 35px;
    border:1px solid rgba(90,220,255,.17);
    background:linear-gradient(180deg, rgba(26,49,67,.60), rgba(9,23,37,.50));
}

.pod-ring {
    position:absolute;
    left:25px;
    right:25px;
    top:116px;
    height:44px;
    border:1px solid rgba(100,225,255,.14);
    border-radius:50%;
    box-shadow:inset 0 0 18px rgba(0,220,255,.05);
}
.pod-seat {
    position:absolute;
    left:24px;
    right:24px;
    bottom:48px;
    height:42px;
    border-radius:50%;
    background:linear-gradient(180deg,rgba(12,30,45,.95),rgba(5,15,27,.98));
    border:1px solid rgba(120,210,255,.13);
    box-shadow:inset 0 5px 12px rgba(255,255,255,.025);
}
.pod-light {
    position:absolute;
    left:50%;
    bottom:36px;
    width:34px;
    height:4px;
    transform:translateX(-50%);
    border-radius:10px;
    background:#27ddff;
    box-shadow:0 0 16px rgba(39,221,255,.85);
}
.pod-screen {
    position:absolute;
    left:39px;
    top:43px;
    width:72px;
    height:42px;
    border-radius:12px;
    border:1px solid rgba(0,220,255,.25);
    background:rgba(0,20,32,.70);
    display:flex;
    align-items:center;
    justify-content:center;
    color:#38e6ff;
    font-size:10px;
    box-shadow:0 0 20px rgba(0,210,255,.12);
}

.pod-glow {
    position:absolute;
    left:35px;
    right:35px;
    bottom:28px;
    height:46px;
    border-radius:50%;
    background:rgba(0,211,255,.18);
    filter:blur(8px);
}

.pod-shadow {
    position:absolute;
    left:50%;
    bottom:2px;
    width:180px;
    height:22px;
    transform:translateX(-50%);
    border-radius:50%;
    background:rgba(0,210,255,.12);
    filter:blur(5px);
}

@keyframes spin { to { transform:translate(-50%,-50%) rotate(360deg); } }

.hero-mini-stats {
    position:absolute;
    top:26px;
    left:30px;
    display:flex;
    gap:9px;
    z-index:5;
}
.hero-mini-stats div {
    min-width:110px;
    padding:9px 11px;
    border-radius:12px;
    background:rgba(4,12,24,.52);
    border:1px solid rgba(110,180,240,.12);
    backdrop-filter:blur(12px);
}
.hero-mini-stats span {
    display:block;
    color:#687995;
    font-size:8px;
    letter-spacing:1.2px;
}
.hero-mini-stats b {
    display:block;
    color:#cfeeff;
    font-size:10px;
    margin-top:4px;
}
/* Status cards */
.status-card {
    padding:16px 18px;
    border-radius:17px;
    border:1px solid rgba(115,145,190,.18);
    background:rgba(15,24,42,.72);
    box-shadow:inset 0 1px 0 rgba(255,255,255,.04);
}

.status-dot {
    display:inline-block;
    width:8px;
    height:8px;
    border-radius:50%;
    background:#31e6ae;
    box-shadow:0 0 12px rgba(49,230,174,.85);
    margin-right:8px;
}

.status-name {
    color:#8190aa;
    font-size:11px;
    letter-spacing:1px;
}

.status-value {
    color:#ecf6ff;
    font-weight:700;
    margin-top:7px;
}

/* Section */
.section {
    display:flex;
    align-items:center;
    gap:12px;
    margin:30px 0 14px;
}

.section-line {
    width:28px;
    height:2px;
    background:linear-gradient(90deg,#1edcff,#8a6cff);
    box-shadow:0 0 12px rgba(30,220,255,.5);
}

.section-title {
    font-size:21px;
    font-weight:800;
}

/* Metric cards */
.metric-card {
    min-height:145px;
    padding:20px;
    border-radius:20px;
    border:1px solid rgba(105,145,195,.17);
    background:linear-gradient(145deg, rgba(21,32,52,.88), rgba(9,17,31,.86));
    box-shadow:inset 0 1px 0 rgba(255,255,255,.04), 0 18px 35px rgba(0,0,0,.16);
}

.metric-label { color:#7f90aa; font-size:12px; letter-spacing:.6px; }
.metric-value { font-size:31px; font-weight:800; margin-top:9px; }
.metric-accent { color:#36ddff; }

/* AI result */
.ai-card {
    padding:25px;
    border-radius:22px;
    border:1px solid rgba(128,104,255,.22);
    background:
        radial-gradient(circle at 90% 20%, rgba(123,83,255,.12), transparent 25%),
        linear-gradient(145deg, rgba(23,28,57,.92), rgba(11,17,34,.92));
    box-shadow:inset 0 1px 0 rgba(255,255,255,.05), 0 20px 50px rgba(0,0,0,.22);
}

.ai-label { color:#8c9ab2; font-size:12px; letter-spacing:1px; }
.ai-result { font-size:34px; font-weight:800; margin:9px 0; }
.ai-normal { color:#4de6b2; }
.ai-unusual { color:#ffb35c; }
.ai-copy { color:#9aa8be; line-height:1.65; font-size:14px; }

/* Streamlit widgets */
div[data-testid="stProgress"] > div > div {
    background:linear-gradient(90deg,#1bdcff,#7d67ff);
}

div[data-testid="stDataFrame"] {
    border-radius:16px;
    overflow:hidden;
}

/* Buttons */
.stButton > button {
    border-radius:13px !important;
    border:1px solid rgba(31,220,255,.28) !important;
    background:rgba(15,35,55,.8) !important;
    color:#eafaff !important;
    font-weight:700 !important;
    min-height:45px !important;
}

.stDownloadButton > button {
    border-radius:13px !important;
    background:linear-gradient(90deg,#10bfe4,#675cff) !important;
    color:white !important;
    border:0 !important;
    font-weight:700 !important;
}

/* Remove default metric styling */
div[data-testid="stMetric"] {
    background:transparent;
}

/* Mobile */
@media (max-width: 900px) {
    .hero { min-height:650px; }
    .pod-stage { right:50%; transform:translateX(50%); top:20px; }
    .hero-copy { left:24px; right:24px; bottom:28px; }
    .hero-title { font-size:32px; }
}
</style>
""", unsafe_allow_html=True)

# =========================================================
# LOAD DATA + MODEL
# =========================================================
try:
    data = pd.read_csv("data/sensor_data.csv")
    model = joblib.load("ml/health_monitoring_model.pkl")
except Exception as e:
    st.error(f"Unable to load project data/model: {e}")
    st.stop()

if data.empty:
    st.warning("Waiting for sensor data...")
    st.stop()

latest = data.iloc[-1]

# =========================================================
# SIDEBAR NAVIGATION
# =========================================================
with st.sidebar:
    st.markdown("""
    <div class="sidebar-logo">+</div>
    <div class="sidebar-title">Smart Health AI</div>
    <div class="sidebar-sub">MONITORING PLATFORM</div>

    <div class="sidebar-nav">NAVIGATION</div>
    <div class="sidebar-item active">◉  Overview</div>
    <div class="sidebar-item">◌  Live Sensors</div>
    <div class="sidebar-item">⌁  AI Analytics</div>
    <div class="sidebar-item">▦  Sensor History</div>
    <div class="sidebar-item">⌘  System Architecture</div>

    <div class="sidebar-foot">
        <b style="color:#9feaff;">SYSTEM ONLINE</b><br>
        Sensor stream is connected to the dashboard.<br><br>
        Prototype interface — not a medical diagnostic system.
    </div>
    """, unsafe_allow_html=True)

# =========================================================
# TOP BAR
# =========================================================
st.markdown("""
<div class="preview-banner">
    ● LIVE SYSTEM &nbsp;•&nbsp; AI + IoT HEALTH MONITORING &nbsp;•&nbsp;
    Data refreshes automatically every 3 seconds
</div>

<div class="brand-row">
    <div class="brand">
        <div class="brand-icon">+</div>
        <div>
            <div class="brand-title">Smart AI Health Monitoring Toilet</div>
            <div class="brand-sub">INTELLIGENT HEALTH PATTERN MONITORING</div>
        </div>
    </div>
    <div class="live-pill">● SYSTEM ONLINE</div>
</div>
""", unsafe_allow_html=True)

# =========================================================
# HERO / 3D POD
# =========================================================
st.markdown("""
<div class="hero">
    <div class="pod-stage">
        <div class="orbit"></div>
        <div class="pod">
            <div class="pod-screen">AI READY</div>
            <div class="pod-ring"></div>
            <div class="pod-seat"></div>
            <div class="pod-light"></div>
            <div class="pod-glow"></div>
        </div>
        <div class="pod-shadow"></div>
    </div>
    <div class="hero-mini-stats">
        <div><span>DATA STREAM</span><b>LIVE</b></div>
        <div><span>MODEL</span><b>RANDOM FOREST</b></div>
        <div><span>REFRESH</span><b>3 SEC</b></div>
    </div>
    <div class="hero-copy">
        <div class="eyebrow">AI + IOT HEALTH MONITORING</div>
        <div class="hero-title">
            Smart AI <span>Health Monitoring Toilet</span>
        </div>
        <div class="hero-desc">
            Intelligent, contactless health-pattern monitoring powered by
            sensor data, MQTT communication and a trained Random Forest model.
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# =========================================================
# SYSTEM STATUS
# =========================================================
status_cols = st.columns(4)

statuses = [
    ("IoT", "ONLINE"),
    ("MQTT", "ACTIVE"),
    ("AI ENGINE", "ACTIVE"),
    ("DATA LOGGING", "ACTIVE"),
]

for col, (name, value) in zip(status_cols, statuses):
    with col:
        st.markdown(f"""
        <div class="status-card">
            <div class="status-name"><span class="status-dot"></span>{name}</div>
            <div class="status-value">{value}</div>
        </div>
        """, unsafe_allow_html=True)

# =========================================================
# LIVE SENSOR INTELLIGENCE
# =========================================================
st.markdown("""
<div class="section">
    <div class="section-line"></div>
    <div class="section-title">Live Sensor Intelligence</div>
</div>
""", unsafe_allow_html=True)

metric_cols = st.columns(4)

metrics = [
    ("URINE VOLUME", f"{latest['urine_volume_ml']:.0f} ml"),
    ("URINE pH", f"{latest['ph']:.2f}"),
    ("TEMPERATURE", f"{latest['temperature_c']:.1f} °C"),
    ("FREQUENCY", f"{latest['frequency_per_day']:.0f} /day"),
]

for col, (label, value) in zip(metric_cols, metrics):
    with col:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">{label}</div>
            <div class="metric-value metric-accent">{value}</div>
            <div class="metric-label" style="margin-top:9px;">LATEST SENSOR READING</div>
        </div>
        """, unsafe_allow_html=True)

# =========================================================
# AI PREDICTION
# =========================================================
input_data = pd.DataFrame([{
    "urine_volume_ml": latest["urine_volume_ml"],
    "ph": latest["ph"],
    "temperature_c": latest["temperature_c"],
    "frequency_per_day": latest["frequency_per_day"]
}])

prediction = model.predict(input_data)[0]

try:
    probabilities = model.predict_proba(input_data)[0]
    confidence = max(probabilities) * 100
except Exception:
    confidence = None

st.markdown("""
<div class="section">
    <div class="section-line"></div>
    <div class="section-title">AI Pattern Detection</div>
</div>
""", unsafe_allow_html=True)

if prediction == "Normal":
    result_class = "ai-normal"
    result_text = "NORMAL PATTERN"
    result_copy = (
        "The current sensor pattern matches the model's learned "
        "normal pattern."
    )
else:
    result_class = "ai-unusual"
    result_text = "UNUSUAL PATTERN"
    result_copy = (
        "The model detected a pattern outside its learned training "
        "pattern. Further evaluation may be appropriate."
    )

st.markdown(f"""
<div class="ai-card">
    <div class="ai-label">AI ANALYSIS RESULT</div>
    <div class="ai-result {result_class}">{result_text}</div>
    <div class="ai-copy">{result_copy}</div>
</div>
""", unsafe_allow_html=True)

if confidence is not None:
    st.write("")
    st.progress(
        min(confidence / 100, 1.0),
        text=f"Model confidence: {confidence:.1f}%"
    )

st.caption(
    "Prototype only: this system detects simulated patterns and does not provide a medical diagnosis."
)

# =========================================================
# LIVE ACTIVITY STRIP
# =========================================================
latest_time = str(latest.get("timestamp", "Latest reading"))
st.markdown(f"""
<div style="
    display:flex;
    justify-content:space-between;
    gap:12px;
    flex-wrap:wrap;
    margin:16px 0 4px;
    padding:12px 15px;
    border:1px solid rgba(90,150,205,.13);
    border-radius:14px;
    background:rgba(10,20,36,.55);
    color:#71829d;
    font-size:11px;">
    <span>● SENSOR STREAM <b style="color:#52edc2;">ACTIVE</b></span>
    <span>LAST READING <b style="color:#d7e8f7;">{latest_time}</b></span>
    <span>PIPELINE <b style="color:#9f8cff;">ESP32 → MQTT → ML</b></span>
</div>
""", unsafe_allow_html=True)

# =========================================================
# ANALYTICS
# =========================================================
st.markdown("""
<div class="section">
    <div class="section-line"></div>
    <div class="section-title">Sensor Analytics</div>
</div>
""", unsafe_allow_html=True)

chart_data = data.tail(30).copy()
chart_data["timestamp"] = pd.to_datetime(
    chart_data["timestamp"], errors="coerce"
)
chart_data = chart_data.dropna(subset=["timestamp"]).set_index("timestamp")

c1, c2 = st.columns(2)

with c1:
    st.markdown("#### Urine Volume — last 30 readings")
    st.line_chart(chart_data["urine_volume_ml"])

with c2:
    st.markdown("#### Urine pH — last 30 readings")
    st.line_chart(chart_data["ph"])

c3, c4 = st.columns(2)

with c3:
    st.markdown("#### Temperature — last 30 readings")
    st.line_chart(chart_data["temperature_c"])

with c4:
    st.markdown("#### Frequency — last 30 readings")
    st.line_chart(chart_data["frequency_per_day"])

# =========================================================
# RECENT READINGS
# =========================================================
st.markdown("""
<div class="section">
    <div class="section-line"></div>
    <div class="section-title">Recent Sensor Readings</div>
</div>
""", unsafe_allow_html=True)

recent_data = data.tail(10).sort_values(
    by="timestamp", ascending=False
)

st.dataframe(
    recent_data,
    width="stretch",
    hide_index=True
)

csv_data = data.to_csv(index=False)
st.download_button(
    label="Download Sensor Data",
    data=csv_data,
    file_name="smart_toilet_sensor_data.csv",
    mime="text/csv"
)

# =========================================================
# ARCHITECTURE
# =========================================================
st.markdown("""
<div class="section">
    <div class="section-line"></div>
    <div class="section-title">AI + IoT Architecture</div>
</div>
""", unsafe_allow_html=True)

arch_cols = st.columns(4)

architecture = [
    ("IOT LAYER", "ESP32 + Sensors", "Sensor data generation"),
    ("COMMUNICATION", "MQTT", "Real-time transmission"),
    ("AI LAYER", "Random Forest", "Pattern classification"),
    ("DASHBOARD", "Streamlit", "Live visualization"),
]

for col, (title, main, desc) in zip(arch_cols, architecture):
    with col:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">{title}</div>
            <div class="metric-value" style="font-size:20px;">{main}</div>
            <div class="metric-label" style="margin-top:10px;">{desc}</div>
        </div>
        """, unsafe_allow_html=True)

st.write("")
st.caption(
    "Smart AI Health Monitoring Toilet • ESP32 → MQTT → Python → ML → Streamlit"
)
