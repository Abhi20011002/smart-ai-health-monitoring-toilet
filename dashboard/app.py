import streamlit as st
import pandas as pd
import joblib
from streamlit_autorefresh import st_autorefresh

# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Smart AI Health Monitoring Toilet",
    page_icon="🚽",
    layout="wide"
)

# =========================================================
# AUTO REFRESH
# =========================================================

st_autorefresh(
    interval=3000,
    key="sensor_refresh"
)

# =========================================================
# CUSTOM UI
# =========================================================

st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #050816 0%, #0b1225 50%, #111827 100%);
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
    max-width: 1500px;
}

.hero {
    padding: 30px;
    border-radius: 22px;
    background: linear-gradient(135deg, #111a35, #172554);
    border: 1px solid #334155;
    margin-bottom: 25px;
    box-shadow: 0 10px 35px rgba(0,0,0,0.25);
}

.hero-title {
    font-size: 40px;
    font-weight: 800;
}

.hero-subtitle {
    color: #a5b4fc;
    font-size: 17px;
    margin-top: 5px;
}

.status {
    padding: 14px;
    border-radius: 14px;
    text-align: center;
    font-weight: 700;
    background: #0f2a24;
    border: 1px solid #1f6f5b;
    color: #5eead4;
}

.ai-box {
    padding: 30px;
    border-radius: 20px;
    background: linear-gradient(135deg, #111827, #172554);
    border: 1px solid #334155;
    margin-top: 10px;
    margin-bottom: 15px;
}

.ai-heading {
    font-size: 20px;
    color: #94a3b8;
}

.ai-result {
    font-size: 32px;
    font-weight: 800;
    margin-top: 8px;
}

.section-title {
    font-size: 25px;
    font-weight: 750;
    margin-top: 25px;
    margin-bottom: 15px;
}

.info-card {
    padding: 20px;
    border-radius: 16px;
    background: #111827;
    border: 1px solid #263449;
    min-height: 130px;
}

.small-text {
    color: #94a3b8;
    font-size: 14px;
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

# =========================================================
# LATEST READING
# =========================================================

latest = data.iloc[-1]

# =========================================================
# HEADER
# =========================================================

st.markdown("""
<div class="hero">

<div class="hero-title">
🚽 Smart AI Health Monitoring Toilet
</div>

<div class="hero-subtitle">
AI + IoT based health pattern monitoring prototype
</div>

</div>
""", unsafe_allow_html=True)

# =========================================================
# SYSTEM STATUS
# =========================================================

status1, status2, status3, status4 = st.columns(4)

with status1:
    st.markdown(
        '<div class="status">🟢 IoT ONLINE</div>',
        unsafe_allow_html=True
    )

with status2:
    st.markdown(
        '<div class="status">📡 MQTT ACTIVE</div>',
        unsafe_allow_html=True
    )

with status3:
    st.markdown(
        '<div class="status">🧠 AI ACTIVE</div>',
        unsafe_allow_html=True
    )

with status4:
    st.markdown(
        '<div class="status">💾 DATA LOGGING</div>',
        unsafe_allow_html=True
    )

# =========================================================
# LIVE SENSOR DATA
# =========================================================

st.markdown(
    '<div class="section-title">📡 Live Sensor Intelligence</div>',
    unsafe_allow_html=True
)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "💧 Urine Volume",
        f"{latest['urine_volume_ml']:.0f} ml"
    )

with col2:
    st.metric(
        "🧪 Urine pH",
        f"{latest['ph']:.2f}"
    )

with col3:
    st.metric(
        "🌡️ Temperature",
        f"{latest['temperature_c']:.1f} °C"
    )

with col4:
    st.metric(
        "🚻 Frequency",
        f"{latest['frequency_per_day']:.0f} /day"
    )

# =========================================================
# AI PREDICTION
# =========================================================

st.divider()

st.markdown(
    '<div class="section-title">🧠 AI Pattern Detection</div>',
    unsafe_allow_html=True
)

input_data = pd.DataFrame([{
    "urine_volume_ml": latest["urine_volume_ml"],
    "ph": latest["ph"],
    "temperature_c": latest["temperature_c"],
    "frequency_per_day": latest["frequency_per_day"]
}])

prediction = model.predict(input_data)[0]

# Model confidence
try:
    probabilities = model.predict_proba(input_data)[0]
    confidence = max(probabilities) * 100
except Exception:
    confidence = None

if prediction == "Normal":

    st.markdown("""
    <div class="ai-box">

    <div class="ai-heading">
    🤖 AI Analysis Result
    </div>

    <div class="ai-result">
    🟢 Normal Pattern
    </div>

    <p>
    The current simulated sensor pattern matches the
    model's learned normal pattern.
    </p>

    </div>
    """, unsafe_allow_html=True)

else:

    st.markdown("""
    <div class="ai-box">

    <div class="ai-heading">
    🤖 AI Analysis Result
    </div>

    <div class="ai-result">
    🟠 Unusual Pattern
    </div>

    <p>
    The model detected a pattern outside its simulated
    normal training pattern. Further evaluation may be appropriate.
    </p>

    </div>
    """, unsafe_allow_html=True)

if confidence is not None:

    st.progress(
        min(confidence / 100, 1.0),
        text=f"Model confidence: {confidence:.1f}%"
    )

st.caption(
    "⚠️ Prototype only: this system detects simulated patterns and "
    "does not provide a medical diagnosis."
)

# =========================================================
# DATA ANALYTICS
# =========================================================

st.divider()

st.markdown(
    '<div class="section-title">📊 Sensor Analytics</div>',
    unsafe_allow_html=True
)

chart_data = data.tail(30).copy()

chart_data["timestamp"] = pd.to_datetime(
    chart_data["timestamp"],
    errors="coerce"
)

chart_data = chart_data.dropna(
    subset=["timestamp"]
)

chart_data = chart_data.set_index("timestamp")

# Two-column charts

col1, col2 = st.columns(2)

with col1:

    st.write("### 💧 Urine Volume")

    st.line_chart(
        chart_data["urine_volume_ml"]
    )

with col2:

    st.write("### 🧪 Urine pH")

    st.line_chart(
        chart_data["ph"]
    )

col3, col4 = st.columns(2)

with col3:

    st.write("### 🌡️ Temperature")

    st.line_chart(
        chart_data["temperature_c"]
    )

with col4:

    st.write("### 🚻 Frequency")

    st.line_chart(
        chart_data["frequency_per_day"]
    )

# =========================================================
# RECENT READINGS
# =========================================================

st.divider()

st.markdown(
    '<div class="section-title">📋 Recent Sensor Readings</div>',
    unsafe_allow_html=True
)

recent_data = data.tail(10).sort_values(
    by="timestamp",
    ascending=False
)

st.dataframe(
    recent_data,
    use_container_width=True,
    hide_index=True
)

# =========================================================
# DOWNLOAD DATA
# =========================================================

csv_data = data.to_csv(index=False)

st.download_button(
    label="📥 Download Sensor Data",
    data=csv_data,
    file_name="smart_toilet_sensor_data.csv",
    mime="text/csv"
)

# =========================================================
# PROJECT ARCHITECTURE
# =========================================================

st.divider()

st.markdown(
    '<div class="section-title">🚀 AI + IoT Architecture</div>',
    unsafe_allow_html=True
)

info1, info2, info3, info4 = st.columns(4)

with info1:

    st.markdown("""
    <div class="info-card">

    <b>📡 IoT Layer</b>

    <br><br>

    ESP32 + simulated sensor

    <br><br>

    <span class="small-text">
    Sensor data generation
    </span>

    </div>
    """, unsafe_allow_html=True)

with info2:

    st.markdown("""
    <div class="info-card">

    <b>☁️ Communication</b>

    <br><br>

    MQTT Protocol

    <br><br>

    <span class="small-text">
    Real-time data transmission
    </span>

    </div>
    """, unsafe_allow_html=True)

with info3:

    st.markdown("""
    <div class="info-card">

    <b>🧠 AI Layer</b>

    <br><br>

    Random Forest

    <br><br>

    <span class="small-text">
    Pattern classification
    </span>

    </div>
    """, unsafe_allow_html=True)

with info4:

    st.markdown("""
    <div class="info-card">

    <b>📊 Dashboard</b>

    <br><br>

    Streamlit

    <br><br>

    <span class="small-text">
    Real-time visualization
    </span>

    </div>
    """, unsafe_allow_html=True)

# =========================================================
# FOOTER
# =========================================================

st.write("")

st.caption(
    "Smart AI Health Monitoring Toilet • AI + IoT Prototype • "
    "ESP32 → MQTT → Python → ML → Streamlit"
)