import streamlit as st
import os
import sys

# Add modules to path to ensure imports work
sys.path.append(os.path.join(os.path.dirname(__file__), 'modules'))

from modules import neon_brain, tyche_engine, lead_scraper

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="EON MATRIX | Melivive Central", page_icon="🧬", layout="wide")

# --- STYLING ---
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: #00ff41; }
    .stButton>button { background-color: #00ff41; color: black; border: none; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.title("🔋 SYSTEM STATUS")
    api_key = st.text_input("Enter Groq API Key", type="password")
    
    if api_key:
        os.environ["GROQ_API_KEY"] = api_key
        st.success("NEON OLYMPUS: ONLINE")
    else:
        st.warning("NEON OLYMPUS: OFFLINE")
    
    st.markdown("---")
    st.markdown("**User Workload:** -∞ + 1")

# --- MAIN DASHBOARD ---
st.title("🧬 THE EON MATRIX: Central Command")
tab1, tab2, tab3 = st.tabs(["AGENCY (Revenue)", "LAB (Brain)", "MEDIA (Brand)"])

# --- TAB 1: REVENUE ---
with tab1:
    st.header("Branch A: Revenue Engine")
    if st.button("INITIATE SALES SEQUENCE"):
        leads = lead_scraper.run_apollo_simulation("Tech")
        st.write(f"✅ Scraped {len(leads)} Leads (Free Mode)")
        for lead in leads:
            audit = tyche_engine.audit_task_cost("Call Lead", 0.00)
            st.write(f"📞 Calling {lead['company']}... {audit['reason']}")

# --- TAB 2: BRAIN ---
with tab2:
    st.header("Branch B: Self-Evolving Lab")
    prompt_input = st.text_area("Input Command for NEON OLYMPUS:", height=100)
    if st.button("EXECUTE TASK"):
        response = neon_brain.get_neon_response(prompt_input)
        st.markdown("### NEON OLYMPUS RESPONSE:")
        st.write(response)

# --- TAB 3: MEDIA ---
with tab3:
    st.header("Branch C: Media & Branding")
    st.write("Visual Dominance Protocols Active.")
