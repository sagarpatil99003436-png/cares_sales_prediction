
import joblib
import numpy as np
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Car Sales Predictor Pro | TABULO DUO",
    page_icon="🏎️",
    layout="wide",
)

st.markdown("""
<style>

.stApp{
    background:
    linear-gradient(rgba(5,8,15,0.92),rgba(5,8,15,0.92)),
    url("https://images.unsplash.com/photo-1503376780353-7e6692767b70?q=80&w=2070&auto=format&fit=crop");
    background-size:cover;
    background-position:center;
    background-attachment:fixed;
    color:white;
    font-family:'Segoe UI',sans-serif;
}

#MainMenu{visibility:hidden;}
footer{visibility:hidden;}
header{visibility:hidden;}

.hero-title{
    text-align:center;
    font-size:4.5rem;
    font-weight:900;
    background:linear-gradient(90deg,#22c55e,#4ade80,#ffffff);
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
    margin-bottom:0px;
}

.hero-subtitle{
    text-align:center;
    color:#d1fae5;
    font-size:1.2rem;
    margin-bottom:35px;
}

.glass-card{
    background:rgba(0,0,0,0.65);
    border-radius:25px;
    padding:25px;
    border:1px solid rgba(255,255,255,0.08);
    backdrop-filter:blur(12px);
    box-shadow:0px 10px 30px rgba(0,0,0,0.5);
}

.section-title{
    color:#4ade80;
    font-size:1.4rem;
    font-weight:700;
    margin-bottom:20px;
}

div[data-baseweb="select"] > div{
    background-color:#000000 !important;
    color:white !important;
    border-radius:14px !important;
    border:1px solid #22c55e !important;
}

.stNumberInput input{
    background-color:#000000 !important;
    color:white !important;
    border-radius:12px !important;
    border:1px solid #22c55e !important;
}

.stRadio > div{
    background-color:#000000 !important;
    padding:10px;
    border-radius:12px;
    border:1px solid #22c55e;
}

.stSlider > div{
    color:#22c55e !important;
}

.stButton > button{
    width:100%;
    background:linear-gradient(90deg,#16a34a,#22c55e);
    color:white;
    border:none;
    border-radius:18px;
    padding:16px;
    font-size:22px;
    font-weight:800;
    box-shadow:0px 8px 25px rgba(34,197,94,0.4);
}

.stButton > button:hover{
    transform:translateY(-4px);
    box-shadow:0px 12px 35px rgba(34,197,94,0.6);
}

.car-card{
    background:rgba(0,0,0,0.75);
    border-radius:22px;
    padding:15px;
    border:1px solid rgba(255,255,255,0.08);
    text-align:center;
}

.car-price{
    color:#22c55e;
    font-size:1.5rem;
    font-weight:800;
}

.feature-box{
    background:rgba(0,0,0,0.75);
    border:1px solid rgba(34,197,94,0.25);
    border-radius:18px;
    padding:18px;
    text-align:center;
    margin-top:15px;
}

.feature-title{
    color:#86efac;
    font-size:1rem;
    font-weight:700;
}

.feature-value{
    color:white;
    font-size:1.2rem;
    font-weight:800;
    margin-top:8px;
}

</style>
""", unsafe_allow_html=True)

@st.cache_resource
def load_model():
    model = joblib.load("xgboost_model.pkl")

    fuels = ["Diesel", "LPG", "CNG", "Petrol"]

    owners = [
        "First Owner",
        "Second Owner",
        "Third Owner",
        "Fourth & Above Owner",
        "Test Drive Car",
    ]

    return model, fuels, owners

try:
    model, fuels, owners = load_model()

except Exception as e:
    st.error(f"Error loading model: {e}")
    st.stop()

st.markdown("""
<div style='padding-top:20px;padding-bottom:10px;'>
    <h1 class='hero-title'> CAR SALES PRICE PRIDICTOR BY "TABULO DUO"</h1>
    <p class='hero-subtitle'>
        Premium resale prediction powered by Advanced Machine Learning
    </p>
</div>
""", unsafe_allow_html=True)

img1, img2, img3 = st.columns(3)

with img1:
    st.markdown("<div class='car-card'>", unsafe_allow_html=True)
    st.image("https://images.unsplash.com/photo-1492144534655-ae79c964c9d7?q=80&w=1200&auto=format&fit=crop")
    st.markdown("<h3 style='color:white;'>BMW M4 Competition</h3>", unsafe_allow_html=True)
    st.markdown("<div class='car-price'>₹ 52,00,000</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

with img2:
    st.markdown("<div class='car-card'>", unsafe_allow_html=True)
    st.image("https://images.unsplash.com/photo-1502877338535-766e1452684a?q=80&w=1200&auto=format&fit=crop")
    st.markdown("<h3 style='color:white;'>Mercedes AMG GT</h3>", unsafe_allow_html=True)
    st.markdown("<div class='car-price'>₹ 78,50,000</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

with img3:
    st.markdown("<div class='car-card'>", unsafe_allow_html=True)
    st.image("https://images.unsplash.com/photo-1553440569-bcc63803a83d?q=80&w=1200&auto=format&fit=crop")
    st.markdown("<h3 style='color:white;'>Audi RS7 Sportback</h3>", unsafe_allow_html=True)
    st.markdown("<div class='car-price'>₹ 1,12,00,000</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("<div class='glass-card'>", unsafe_allow_html=True)

st.markdown(
    "<div class='section-title'>📋 Vehicle Information</div>",
    unsafe_allow_html=True,
)

col1, col2, col3 = st.columns(3)

with col1:

    year = st.number_input(
        "Year of Manufacture",
        min_value=1990,
        max_value=2026,
        value=2018,
        step=1,
    )

    name_encoded = st.number_input(
        "Car Model Label Code",
        min_value=0.0,
        max_value=2000.0,
        value=100.0,
    )

    seats = st.slider(
        "Seats Capacity",
        min_value=2,
        max_value=10,
        value=5,
    )

with col2:

    mileage = st.number_input(
        "Mileage (kmpl)",
        min_value=0.0,
        max_value=50.0,
        value=20.0,
        step=0.1,
    )

    engine = st.number_input(
        "Engine Capacity (CC)",
        min_value=600,
        max_value=5000,
        value=1248,
        step=1,
    )

    max_power = st.number_input(
        "Max Power (bhp)",
        min_value=30.0,
        max_value=500.0,
        value=85.0,
        step=0.1,
    )

with col3:

    fuel = st.selectbox(
        "Fuel Type",
        options=fuels,
    )

    owner = st.selectbox(
        "Owner History",
        options=owners,
    )

    transmission = st.radio(
        "Transmission",
        options=["Manual", "Automatic"],
        horizontal=True,
    )

    seller_type = st.selectbox(
        "Seller Category",
        options=["Individual", "Dealer", "Trustmark Dealer"],
    )

st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

left, center, right = st.columns([1,2,1])

with center:
    predict_btn = st.button("🚀 Predict Resale Price")

if predict_btn:

    fuel_encoded = fuels.index(fuel)
    owner_encoded = owners.index(owner)

    transmission_Automatic = 1 if transmission == "Automatic" else 0
    transmission_Manual = 1 if transmission == "Manual" else 0

    seller_type_Dealer = 1 if seller_type == "Dealer" else 0
    seller_type_Individual = 1 if seller_type == "Individual" else 0
    seller_type_Trustmark_Dealer = 1 if seller_type == "Trustmark Dealer" else 0

    raw_features = np.array(
        [
            name_encoded,
            year,
            fuel_encoded,
            owner_encoded,
            mileage,
            engine,
            max_power,
            seats,
            transmission_Automatic,
            transmission_Manual,
            seller_type_Dealer,
            seller_type_Individual,
            seller_type_Trustmark_Dealer,
        ]
    ).reshape(1, -1)

    feature_names = [
        "name",
        "year",
        "fuel",
        "owner",
        "mileage",
        "engine",
        "max_power",
        "seats",
        "transmission_Automatic",
        "transmission_Manual",
        "seller_type_Dealer",
        "seller_type_Individual",
        "seller_type_Trustmark Dealer",
    ]

    input_df = pd.DataFrame(raw_features, columns=feature_names)

    try:

        predicted_scaled_price = model.predict(input_df)[0]

        st.markdown(
            f"""
            <h1 style='
                text-align:center;
                font-size:7rem;
                font-weight:1000;
                color:#22c55e;
                margin-top:40px;
                text-shadow:0px 0px 40px rgba(34,197,94,0.9);
            '>
                ₹ {predicted_scaled_price:,.2f}
            </h1>
            """,
            unsafe_allow_html=True,
        )

        st.markdown("<br>", unsafe_allow_html=True)

        f1, f2, f3 = st.columns(3)

        with f1:
            st.markdown(f"""
            <div class='feature-box'>
                <div class='feature-title'>Fuel Type</div>
                <div class='feature-value'>{fuel}</div>
            </div>
            """, unsafe_allow_html=True)

            st.markdown(f"""
            <div class='feature-box'>
                <div class='feature-title'>Transmission</div>
                <div class='feature-value'>{transmission}</div>
            </div>
            """, unsafe_allow_html=True)

            st.markdown(f"""
            <div class='feature-box'>
                <div class='feature-title'>Seller Type</div>
                <div class='feature-value'>{seller_type}</div>
            </div>
            """, unsafe_allow_html=True)

        with f2:
            st.markdown(f"""
            <div class='feature-box'>
                <div class='feature-title'>Manufacturing Year</div>
                <div class='feature-value'>{year}</div>
            </div>
            """, unsafe_allow_html=True)

            st.markdown(f"""
            <div class='feature-box'>
                <div class='feature-title'>Mileage</div>
                <div class='feature-value'>{mileage} kmpl</div>
            </div>
            """, unsafe_allow_html=True)

            st.markdown(f"""
            <div class='feature-box'>
                <div class='feature-title'>Seats</div>
                <div class='feature-value'>{seats}</div>
            </div>
            """, unsafe_allow_html=True)

        with f3:
            st.markdown(f"""
            <div class='feature-box'>
                <div class='feature-title'>Engine</div>
                <div class='feature-value'>{engine} CC</div>
            </div>
            """, unsafe_allow_html=True)

            st.markdown(f"""
            <div class='feature-box'>
                <div class='feature-title'>Max Power</div>
                <div class='feature-value'>{max_power} bhp</div>
            </div>
            """, unsafe_allow_html=True)

            st.markdown(f"""
            <div class='feature-box'>
                <div class='feature-title'>Owner History</div>
                <div class='feature-value'>{owner}</div>
            </div>
            """, unsafe_allow_html=True)

    except Exception as e:
        st.error(f"Prediction Pipeline Error: {e}")

