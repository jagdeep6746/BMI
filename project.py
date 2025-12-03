import streamlit as st

st.set_page_config(
    page_title="BMI Calculator",
    page_icon="💪",
    layout="centered"
)

# ============================================================
# 🌿 Pastel Mint + Soft Charcoal Theme (Calm & Modern)
# ============================================================
st.markdown("""
    <style>
        /* FULL PAGE BACKGROUND */
        html, body, .stApp {
            background-color: #EAF8F5 !important;  /* Pastel Mint */
        }

        /* Main layout */
        .main, .block-container {
            background-color: #EAF8F5 !important;
        }

        /* Sidebar background */
        section[data-testid="stSidebar"] {
            background-color: #E3F5F1 !important;  /* Very soft mint */
        }

        /* Typography */
        h1, h2, h3, label, p, .stMarkdown {
            color: #2E2E2E !important;  /* Soft Charcoal */
        }

        /* BMI Box */
        .bmi-box {
            border-radius: 14px;
            padding: 22px;
            text-align: center;
            background: #CDEFEA; /* Soft mint card */
            box-shadow: 0px 4px 12px rgba(0,0,0,0.05);
            color: #2E2E2E;
        }
    </style>
""", unsafe_allow_html=True)


# -----------------------------------

# Initialize session state
if "weight" not in st.session_state:
    st.session_state.weight = 60.0

if "height" not in st.session_state:
    st.session_state.height = 170.0

st.title("🌿 BMI Calculator (Pastel Mint Theme)")
st.write("Use slider or manual input — both stay in sync!")

# --- Sync Functions ---
def update_weight_from_slider():
    st.session_state.weight = st.session_state.weight_slider
    st.session_state.weight_input = st.session_state.weight_slider

def update_weight_from_input():
    st.session_state.weight = st.session_state.weight_input
    st.session_state.weight_slider = st.session_state.weight_input

def update_height_from_slider():
    st.session_state.height = st.session_state.height_slider
    st.session_state.height_input = st.session_state.height_slider

def update_height_from_input():
    st.session_state.height = st.session_state.height_input
    st.session_state.height_slider = st.session_state.height_input

# --- Two columns ---
col1, col2 = st.columns(2)

with col1:
    st.subheader("🔽 Slider Input")
    st.slider(
        "Weight (kg)",
        30.0, 150.0,
        key="weight_slider",
        value=st.session_state.weight,
        step=0.1,
        on_change=update_weight_from_slider
    )
    st.slider(
        "Height (cm)",
        100.0, 220.0,
        key="height_slider",
        value=st.session_state.height,
        step=0.1,
        on_change=update_height_from_slider
    )

with col2:
    st.subheader("⌨ Manual Input")
    st.number_input(
        "Enter Weight (kg)",
        30.0, 150.0,
        key="weight_input",
        value=st.session_state.weight,
        step=0.1,
        on_change=update_weight_from_input
    )
    st.number_input(
        "Enter Height (cm)",
        100.0, 220.0,
        key="height_input",
        value=st.session_state.height,
        step=0.1,
        on_change=update_height_from_input
    )

# --- Final synced values ---
weight = st.session_state.weight
height_cm = st.session_state.height

# --- Calculate BMI ---
bmi = weight / ((height_cm / 100) ** 2)

# --- Category Logic (with mint variations) ---
# --- Category Logic ---
if bmi < 18.5:
    category = "Underweight"
    color = "#D7F5F1"   # Soft aqua
    progress = 25
    tip = "Try adding nutritious foods to gain weight."

elif 18.5 <= bmi < 24.9:
    category = "Normal Weight"
    color = "#CDEFEA"   # Mint pastel
    progress = 50
    tip = "Great! Maintain your healthy habits."

elif 25 <= bmi < 29.9:
    category = "Overweight"
    color = "#FFE7CD"   # Soft peach
    progress = 75
    tip = "Balanced diet + regular activity helps manage weight."

else:
    category = "Obese"
    color = "#FAD4D4"   # Soft rose
    progress = 95
    tip = "Consider getting professional health advice."


bmi_text = f"{bmi:.2f}"

# --- Display BMI Box --- #
st.markdown(
    f"""
    <div class='bmi-box' style='background:{color};'>
        <h2>Your BMI: {bmi_text}</h2>
        <h3>{category}</h3>
    </div>
    """,
    unsafe_allow_html=True
)

# --- Progress Bar --- #
st.write("### BMI Category Indicator:")
st.progress(progress / 100)

# --- Helpful Tip --- #
st.info(f"💡 **Tip:** {tip}")

# --- Footer --- #
st.write("---")
st.caption("Developed by Jagdeep 💻")
