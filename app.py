import streamlit as st
import os
import google.generativeai as genai

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="EON MATRIX | Melivive Central",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- STYLING (Dark Mode & Central Command Aesthetics) ---
st.markdown("""
    <style>
    .stApp {
        background-color: #0e1117;
        color: #00ff41;
    }
    .stButton>button {
        background-color: #00ff41;
        color: black;
        border-radius: 5px;
        border: none;
        font-weight: bold;
    }
    h1, h2, h3 {
        color: #ffffff;
        font-family: 'Courier New', Courier, monospace;
    }
    div.stMetric {
        background-color: #161b22;
        padding: 10px;
        border-radius: 5px;
        border: 1px solid #30363d;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR: SYSTEM STATUS & KEY ---
with st.sidebar:
    st.title("🔋 SYSTEM STATUS")
    api_key = st.text_input("Enter Gemini API Key", type="password")
    
    if api_key:
        os.environ["GEMINI_API_KEY"] = api_key
        genai.configure(api_key=api_key)
        st.success("NEON OLYMPUS: ONLINE")
    else:
        st.warning("NEON OLYMPUS: OFFLINE")
    
    st.markdown("---")
    st.markdown("**User Workload:** -∞ + 1")
    st.markdown("**Automation:** +∞")

# --- MAIN DASHBOARD ---
st.title("🧬 THE EON MATRIX: Central Command")

# TABS FOR THE 3 ENGINES
tab1, tab2, tab3 = st.tabs(["AGENCY (Revenue)", "LAB (Brain)", "MEDIA (Brand)"])

# --- TAB 1: MELIVIVE AGENCY (Revenue) ---
with tab1:
    st.header("Branch A: Revenue Engine")
    col1, col2, col3 = st.columns(3)
    col1.metric("Leads Scraped", "0", "Waiting...")
    col2.metric("Calls Made", "0", "Waiting...")
    col3.metric("Revenue Trend", "$0.00", "0%")
    
    if st.button("INITIATE SALES SEQUENCE"):
        st.info("Engaging Apollo & Vapi protocols...")
        # Placeholder for connection to modules
        st.write(">> Tyche Engine calculating COGS...")
        st.write(">> Sales sequence started.")

# --- TAB 2: SELF-EVOLVING LAB (Automation) ---
with tab2:
    st.header("Branch B: Self-Evolving Lab")
    prompt_input = st.text_area("Input Command for NEON OLYMPUS:", height=100)
    
    if st.button("EXECUTE TASK"):
        if api_key:
            try:
                model = genai.GenerativeModel('gemini-1.5-flash')
                response = model.generate_content(prompt_input)
                st.markdown("### NEON OLYMPUS RESPONSE:")
                st.write(response.text)
            except Exception as e:
                st.error(f"Error: {e}")
        else:
            st.error("Please enter API Key in sidebar first.")

# --- TAB 3: MEDIA & BRANDING (Visuals) ---
with tab3:
    st.header("Branch C: Media & Branding")
    st.write("Visual Dominance Protocols")
    col_a, col_b = st.columns(2)
    with col_a:
        st.subheader("Video Queue")
        st.empty()
    with col_b:
        st.subheader("Content Calendar")
        st.empty()