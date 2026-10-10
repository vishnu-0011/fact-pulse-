from __future__ import annotations

import streamlit as st

st.set_page_config(page_title="FactoryPulse Console", page_icon="🏭")
st.title("FactoryPulse Console")
st.caption("Operations overview for the factory telemetry stack")

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Active machines", 24)
with col2:
    st.metric("Open alerts", 3)
with col3:
    st.metric("Model drift", "0.8%")

st.write("System status: healthy")
st.progress(75)
