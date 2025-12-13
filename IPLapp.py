import streamlit as st

# Set page config
st.set_page_config(page_title="IPL Player Selector", layout="centered")

# Dark theme styling
dark_bg = """
<style>
body {
    background: linear-gradient(to right, #0f172a, #1e293b);
    color: #f1f5f9;
    font-family: 'Segoe UI', sans-serif;
}
.stApp {
    background-color: #0f172a;
}
h1 {
    color: #38bdf8;
}
.stSelectbox label {
    font-weight: bold;
    color: #facc15;
}
</style>
"""
st.markdown(dark_bg, unsafe_allow_html=True)

# Title
st.title("🏏 IPL Player Selector")
st.markdown("Choose a **Type** and **Team** from the dropdowns below.")

# Dropdown for Type
player_types = sorted(set([
    "All-Rounder", "Bowler", "Batter", "Wicket-Keeper"
]))
selected_type = st.selectbox("Type", player_types)

# Dropdown for Team
teams = sorted(set([
    "Chennai Super Kings", "Delhi Capitals", "Gujarat Titans",
    "Lucknow Super Giants", "Mumbai Indians", "Punjab Kings",
    "Royal Challengers Bangalore", "Rajasthan Royals",
    "Sunrisers Hyderabad", "Unsold"
]))
selected_team = st.selectbox("Team", teams)

# Display selection
st.success(f"You selected: **{selected_type}** from **{selected_team}**")

# Footer
st.markdown("---")
st.caption("Dark Mode IPL Selector 🌌 | Designed by Miduna")
