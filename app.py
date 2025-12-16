import streamlit as st
import os
import sys
import time

# Add modules to path
sys.path.append(os.path.join(os.path.dirname(__file__), 'modules'))

from modules import neon_brain, tyche_engine, lead_scraper

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="EON MATRIX | Melivive Central", page_icon="🧬", layout="wide")

# --- STYLING ---
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: #00ff41; }
    .stButton>button { background-color: #00ff41; color: black; border: none; font-weight: bold; width: 100%; }
    .stTextInput>div>div>input { background-color: #1c1c1c; color: #00ff41; border: 1px solid #00ff41; }
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
    
    st.divider()
    
    st.markdown("### 🎙️ VOICE COMMAND")
    voice_cmd = st.text_input("Type command (Simulating Voice):", placeholder="e.g., 'Check Revenue'")
    if voice_cmd:
        st.info(f"🗣️ PROCESSING AUDIO: '{voice_cmd}'")
        time.sleep(1)
        st.success("✅ COMMAND RECOGNIZED")

    st.divider()
    st.markdown("**User Workload:** -∞ + 1")
    st.markdown("**Revenue Potential:** +∞")

# --- MAIN DASHBOARD ---
st.title("🧬 THE EON MATRIX: Central Command")
tab1, tab2, tab3 = st.tabs(["💰 AGENCY (Revenue)", "🧠 LAB (Brain)", "🎨 MEDIA (Brand)"])

# --- TAB 1: REVENUE ENGINE ---
with tab1:
    col1, col2 = st.columns(2)
    
    with col1:
        st.header("1. Lead Generation")
        if st.button("RUN APOLLO SIMULATION"):
            with st.status("🚀 Scrapping Ecosystem...", expanded=True):
                time.sleep(1)
                st.write("🔍 Identifying High-Ticket Targets...")
                leads = lead_scraper.run_apollo_simulation("Tech")
                time.sleep(1)
                st.write("✅ 10 Leads Verified.")
            
            for lead in leads:
                st.write(f"🏢 **{lead['company']}** | 📊 Score: {lead['score']}/100")

    with col2:
        st.header("2. Deal Optimizer")
        deal_val = st.number_input("Enter Deal Value ($)", value=10000, step=500)
        if st.button("OPTIMIZE DEAL STRUCTURE"):
            data = tyche_engine.optimize_deal(deal_val)
            st.metric(label="PROJECTED PROFIT", value=f"${data['profit']:,.2f}", delta=f"{data['margin_percent']}% Margin")
            st.success(f"STRATEGY: {data['strategy']}")

# --- TAB 2: NEON BRAIN ---
with tab2:
    st.header("Branch B: Self-Evolving Lab")
    prompt_input = st.text_area("Input Command for NEON OLYMPUS:", height=150, placeholder="Ask me to draft a contract, analyze a market, or solve a problem...")
    
    col_a, col_b = st.columns([1, 4])
    with col_a:
        if st.button("EXECUTE TASK"):
            if not os.environ.get("GROQ_API_KEY"):
                st.error("⚠️ KEY MISSING")
            else:
                with st.spinner("🧠 NEON OLYMPUS IS THINKING..."):
                    response = neon_brain.get_neon_response(prompt_input)
                    st.markdown("### 📝 NEON RESPONSE:")
                    st.markdown(response)

# --- TAB 3: MEDIA & BRAND ---
with tab3:
    st.header("Branch C: Content Factory")
    topic = st.text_input("Enter Content Topic:", value="AI Automation Benefits")
    platform = st.selectbox("Select Platform:", ["LinkedIn", "Twitter/X", "Instagram Script"])
    
    if st.button("GENERATE VIRAL CONTENT"):
        if not os.environ.get("GROQ_API_KEY"):
            st.error("⚠️ KEY MISSING")
        else:
            with st.spinner("🎨 CREATING ASSETS..."):
                prompt = f"Write a viral {platform} post about {topic}. Use a punchy, professional tone. Include hashtags."
                content = neon_brain.get_neon_response(prompt)
                st.text_area("Generated Content:", value=content, height=300)
