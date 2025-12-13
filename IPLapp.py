import streamlit as st

# Page setup
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
st.markdown("Select a **Type** and **Team** to view the Price in ₹ Cr.")

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

# Price mapping for all teams (sample values — replace with your dataset averages)
price_map = {
    "Chennai Super Kings": {
        "All-Rounder": 16.25, "Bowler": 8.0, "Batter": 6.5, "Wicket-Keeper": 4.2
    },
    "Delhi Capitals": {
        "All-Rounder": 12.0, "Bowler": 7.5, "Batter": 5.0, "Wicket-Keeper": 3.0
    },
    "Gujarat Titans": {
        "All-Rounder": 14.0, "Bowler": 9.0, "Batter": 6.2, "Wicket-Keeper": 4.5
    },
    "Lucknow Super Giants": {
        "All-Rounder": 13.5, "Bowler": 8.2, "Batter": 5.8, "Wicket-Keeper": 3.8
    },
    "Mumbai Indians": {
        "All-Rounder": 15.0, "Bowler": 9.0, "Batter": 6.0, "Wicket-Keeper": 4.0
    },
    "Punjab Kings": {
        "All-Rounder": 11.5, "Bowler": 7.0, "Batter": 5.5, "Wicket-Keeper": 3.2
    },
    "Royal Challengers Bangalore": {
        "All-Rounder": 14.5, "Bowler": 8.8, "Batter": 6.7, "Wicket-Keeper": 4.1
    },
    "Rajasthan Royals": {
        "All-Rounder": 13.0, "Bowler": 7.8, "Batter": 5.9, "Wicket-Keeper": 3.6
    },
    "Sunrisers Hyderabad": {
        "All-Rounder": 12.8, "Bowler": 7.4, "Batter": 5.6, "Wicket-Keeper": 3.4
    },
    "Unsold": {
        "All-Rounder": 0.2, "Bowler": 0.2, "Batter": 0.2, "Wicket-Keeper": 0.2
    }
}

# Show price
if selected_team in price_map and selected_type in price_map[selected_team]:
    price = price_map[selected_team][selected_type]
    st.success(f"💰 Price: ₹ {price} Cr")
else:
    st.warning("No price available for this combination yet.")

# Footer
st.markdown("---")
st.caption("Dark Mode IPL Price Lookup 🌌 | Designed by Miduna")
