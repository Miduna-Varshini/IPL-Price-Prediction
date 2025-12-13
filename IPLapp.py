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
price_cr_values = [
    16.25, 16, 14, 12, 8, 6.75, 6, 4, 1.9, 1.5, 1.2, 1, 1, 0.7, 0.6, 0.5, 0.5,
    0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 16, 12, 8, 6.5, 6.5, 6.25, 5.5, 5.25,
    4.6, 4.2, 2.8, 2.4, 2, 2, 2, 1.1, 0.65, 0.5, 0.5, 0.5, 0.5, 0.2, 0.2, 0.2, 0.2,
    15, 15, 9, 8, 6.25, 6, 4.4, 3.2, 3, 3, 2.6, 2.4, 2.4, 2, 1.9, 1.7, 1.4, 1.2,
    0.5, 0.5, 0.3, 0.2, 0.2, 0.2, 0.2, 16, 12.25, 12
]

# Display as vertical list
st.markdown("### 💰 Price Cr Values")
for price in price_cr_values:
    st.write(price)

# Display selection
st.success(f"You selected: **{selected_type}** from **{selected_team}**")

# Footer
st.markdown("---")
st.caption("Dark Mode IPL Selector 🌌 | Designed by Miduna")

