import streamlit as st
import pandas as pd
import joblib

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Tsunami Monitoring System",
    page_icon="🌊",
    layout="wide"
)

# ---------------- LOAD MODEL ----------------
model = joblib.load("model/svm_model.pkl")
scaler = joblib.load("model/scaler.pkl")

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

.stApp {
    background: linear-gradient(180deg, #04101c, #06141f);
    color: white;
}

/* Hide Streamlit branding */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* Header */
.main-title {
    text-align: center;
    font-size: 58px;
    font-weight: bold;
    color: #00d4ff;
    margin-top: 10px;
    text-shadow: 0 0 20px rgba(0,212,255,0.35);
}

.subtitle {
    text-align: center;
    color: #94a3b8;
    font-size: 20px;
    margin-bottom: 30px;
}

/* Emergency ticker */
.ticker-box {
    background: rgba(15, 29, 43, 0.95);
    border-left: 6px solid #00d4ff;
    border-radius: 20px;
    overflow: hidden;
    padding: 14px 0;
    margin-bottom: 25px;
    box-shadow: 0 0 25px rgba(0,212,255,0.18);
}

.ticker-text {
    white-space: nowrap;
    display: inline-block;
    color: #00d4ff;
    font-size: 17px;
    font-weight: 600;
    padding-left: 100%;
    animation: tickerMove 55s linear infinite;
}

@keyframes tickerMove {
    0% {
        transform: translateX(0%);
    }

    100% {
        transform: translateX(-100%);
    }
}
            
/* Left input panel */
.dashboard-card {
    background: rgba(15,29,43,0.92);
    padding: 28px;
    border-radius: 24px;
    border-left: 5px solid #00d4ff;
    box-shadow: 0 0 25px rgba(0,212,255,0.12);
}

/* Result cards */
.alert-card {
    background: rgba(15,29,43,0.95);
    border-left: 6px solid #ff4d4d;
    padding: 30px;
    border-radius: 24px;
    box-shadow: 0 0 25px rgba(255,77,77,0.15);
}

.safe-card {
    background: rgba(15,29,43,0.95);
    border-left: 6px solid #22c55e;
    padding: 30px;
    border-radius: 24px;
    box-shadow: 0 0 25px rgba(34,197,94,0.15);
}

/* Geological alert */
.warning-box {
    background: linear-gradient(135deg,#332700,#5a4600);
    border-left: 6px solid #facc15;
    padding: 22px;
    border-radius: 22px;
    margin-top: 18px;
    box-shadow: 0 0 20px rgba(250,204,21,0.15);
}

/* Footer */
.footer-box {
    text-align: center;
    color: #94a3b8;
    margin-top: 40px;
    padding: 15px;
    font-size: 14px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown(
    '<div class="main-title">🌊 Tsunami Monitoring System</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Real-Time Earthquake Threat Assessment Dashboard</div>',
    unsafe_allow_html=True
)

# ---------------- EMERGENCY TICKER ----------------
st.markdown("""
<div class="ticker-box">
    <div class="ticker-text">
    🚨 Emergency Helpline: 112 |
    🌊 Tsunami Warning Centre |
    📻 Follow Government Alerts |
    ⛰️ Move to Higher Ground During Coastal Alerts |
    🚫 Stay Away From Shorelines After Major Earthquakes |
    🎒 Emergency Kit: Water • Torch • First Aid |
    📍 Coastal Residents: Stay Alert After Magnitude 7.5+ Earthquakes |
    ⚠️ Never Return To Coast Until Official Clearance |
    📡 Real-Time Monitoring Active |
    🚨 Your Safety Is Our Priority
    </div>
</div>
""", unsafe_allow_html=True)

# ---------------- LAYOUT ----------------
col1, col2 = st.columns([1.3, 1])

# ---------------- INPUT PANEL ----------------
with col1:


    st.subheader("🌍 Earthquake Parameters")

    magnitude = st.number_input(
        "Magnitude",
        min_value=0.0,
        max_value=10.0,
        value=7.0,
        step=0.1
    )

    depth = st.number_input(
        "Earthquake Depth (km)",
        min_value=0.0,
        value=50.0,
        step=0.1
    )

    cdi = st.number_input(
        "Community Determined Intensity",
        min_value=0,
        max_value=10,
        value=5
    )

    mmi = st.number_input(
        "Modified Mercalli Intensity",
        min_value=0,
        max_value=10,
        value=5
    )

    nst = st.number_input(
        "Number of Stations",
        min_value=0,
        value=100
    )

    dmin = st.number_input(
        "Distance to Nearest Station",
        min_value=0.0,
        value=1.0,
        step=0.1
    )

    gap = st.number_input(
        "Azimuthal Gap",
        min_value=0.0,
        value=20.0,
        step=0.1
    )

    latitude = st.number_input(
        "Latitude",
        min_value=-90.0,
        max_value=90.0,
        value=0.0,
        step=0.1
    )

    longitude = st.number_input(
        "Longitude",
        min_value=-180.0,
        max_value=180.0,
        value=0.0,
        step=0.1
    )

    predict = st.button(
        "🚨 RUN THREAT ANALYSIS",
        use_container_width=True
    )

    st.markdown('</div>', unsafe_allow_html=True)

# ---------------- RESULT PANEL ----------------
with col2:

    st.subheader("📡 Monitoring Status")

    if predict:

        input_data = pd.DataFrame([[
            magnitude,
            depth,
            cdi,
            mmi,
            nst,
            dmin,
            gap,
            latitude,
            longitude
        ]], columns=[
            'magnitude',
            'Earthquake Depth',
            'Community Determined Intensity',
            'Modified Mercalli Intensity',
            'Number of Stations',
            'Distance to Nearest Station',
            'Azimuthal Gap',
            'latitude',
            'longitude'
        ])

        scaled_data = scaler.transform(input_data)

        prediction = model.predict(scaled_data)[0]
        probability = model.predict_proba(scaled_data)[0]

        confidence = max(probability) * 100

        # Smart geological override
        extreme_warning = (
            magnitude >= 8.5 and
            depth <= 70
        )

        # Confidence section
        st.metric(
            label="Prediction Confidence",
            value=f"{confidence:.2f}%"
        )

        st.progress(int(confidence))

        # Prediction result
        if prediction == 1 or extreme_warning:

            st.markdown(f"""
            <div class="alert-card">
            <h1>⚠️ HIGH TSUNAMI THREAT</h1>
            <h2>Confidence: {confidence:.2f}%</h2>
            <p><b>Status:</b> Emergency</p>
            <p>• Evacuate coastal zones</p>
            <p>• Move to higher ground</p>
            <p>• Follow government alerts</p>
            </div>
            """, unsafe_allow_html=True)

        else:

            st.markdown(f"""
            <div class="safe-card">
            <h1>✅ LOW TSUNAMI RISK</h1>
            <h2>Confidence: {confidence:.2f}%</h2>
            <p><b>Status:</b> Stable</p>
            <p>• No immediate danger</p>
            <p>• Continue monitoring updates</p>
            <p>• Stay informed</p>
            </div>
            """, unsafe_allow_html=True)

        # Geological warning
        if extreme_warning:

            st.markdown("""
            <div class="warning-box">
            <h3 style="color:#facc15;">
            ⚠️ Geological Alert
            </h3>

            <p style="font-size:17px; color:white;">
            A very high magnitude shallow earthquake has been detected.
            </p>

            <p style="color:#d1d5db;">
            Even if the machine learning model predicts low tsunami risk,
            immediate monitoring and official emergency guidance are strongly recommended.
            </p>
            </div>
            """, unsafe_allow_html=True)

# ---------------- FOOTER ----------------
st.markdown("""
<div class="footer-box">
🌍 Stay Alert • Follow Official Disaster Warnings • Your Safety Matters
</div>
""", unsafe_allow_html=True)