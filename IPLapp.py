import streamlit as st

# Set page config
st.set_page_config(page_title="IPL Price Lookup", layout="centered")

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
st.title("🏏 IPL Price Lookup")
st.markdown("Select a **Type** and **Team** to view the fixed price in ₹ Cr.")

# Dropdowns
types = ["All-Rounder", "Bowler", "Batter", "Wicket-Keeper"]
teams = [
    "Chennai Super Kings", "Delhi Capitals", "Gujarat Titans",
    "Lucknow Super Giants", "Mumbai Indians", "Punjab Kings",
    "Royal Challengers Bangalore", "Rajasthan Royals",
    "Sunrisers Hyderabad", "Unsold"
]

selected_type = st.selectbox("Type", types)
selected_team = st.selectbox("Team", teams)

# Fixed price mapping (sample values — you can expand this)
price_map = {
    ("All-Rounder", "Chennai Super Kings"): 16.25,
    ("Bowler", "Mumbai Indians"): 8.0,
    ("Batter", "Delhi Capitals"): 6.5,
    ("Wicket-Keeper", "Punjab Kings"): 4.2,
    ("All-Rounder", "Unsold"): 0.2,
    # Add more combinations as needed
}

# Show price
key = (selected_type, selected_team)
if key in price_map:
    st.success(f"💰 Price: ₹ {price_map[key]} Cr")
else:
    st.warning("No fixed price available for this combination.")

# Footer
st.markdown("---")
st.caption("Designed by Miduna 🌌 | Streamlit Frontend")
