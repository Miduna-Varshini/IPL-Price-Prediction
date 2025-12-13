import streamlit as st

# Set page config
st.set_page_config(page_title="IPL Player Type Selector", layout="centered")

# Custom background and styling
page_bg = """
<style>
body {
    background: linear-gradient(to right, #dbeafe, #f0fdf4);
    font-family: 'Segoe UI', sans-serif;
}
.stApp {
    background-color: #f9fafb;
}
h1 {
    color: #1e3a8a;
}
.stSelectbox label {
    font-weight: bold;
    color: #1e40af;
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# Title and instructions
st.title("🏏 IPL Player Type Selector")
st.markdown("Choose a player type from the dropdown below to begin your analysis or prediction.")

# Unique player types extracted from your list
player_types = sorted(set([
    "All-Rounder", "Bowler", "Batter", "Wicket-Keeper"
]))

# Dropdown for Type
selected_type = st.selectbox("Type", player_types)

# Display selection
st.success(f"You selected: **{selected_type}**")

# Footer
st.markdown("---")
st.caption("Designed by Miduna 🌟 | Streamlit Frontend")

