
import streamlit as st

st.set_page_config(page_title="Smart Agro Advisor", layout="centered")

st.title("🌾 Smart Agro Advisor")
st.markdown("**Empowering Farmers with Smart Agricultural Decisions**")

st.subheader("📝 Enter Your Farm Details")

region = st.selectbox("🌍 Region", ["Southwest", "Northwest", "Southeast", "Northeast"])
soil_type = st.selectbox("🧪 Soil Type", ["Loamy", "Sandy", "Clay", "Silty"])
season = st.selectbox("⛅ Current Season", ["Rainy", "Dry"])

if st.button("🚜 Get Advisory"):
    st.success("✅ Advisory Generated Successfully!")

    # Recommendation Logic
    if soil_type == "Loamy" and season == "Rainy":
        crops = ["Maize", "Rice", "Tomatoes"]
        tip = "Loamy soil is fertile and ideal for a wide range of crops. Rainy season boosts yield."
        fertilizer = "Apply NPK 15:15:15 during early growth stages."
        pest_control = "Monitor for stem borers and use neem-based bio-pesticides weekly."
        calendar = "🌱 Planting: May–June | 🌾 Harvesting: September–October"
    elif soil_type == "Sandy":
        crops = ["Cassava", "Groundnut", "Watermelon"]
        tip = "Sandy soils need mulching and regular watering. Perfect for root crops."
        fertilizer = "Use organic compost and potassium-rich supplements."
        pest_control = "Watch for aphids and grasshoppers; apply neem oil."
        calendar = "🌱 Planting: March–April | 🌾 Harvesting: August–September"
    elif soil_type == "Clay":
        crops = ["Sugarcane", "Rice", "Soybeans"]
        tip = "Clay soil retains water; manage drainage to avoid root rot."
        fertilizer = "Incorporate urea and phosphate pre-planting."
        pest_control = "Apply fungicides if rainfall is high."
        calendar = "🌱 Planting: April–May | 🌾 Harvesting: October–November"
    else:
        crops = ["Yam", "Sorghum", "Millet"]
        tip = "Silty soil is rich and easy to cultivate. Maintain good aeration."
        fertilizer = "Mix compost with lime before planting."
        pest_control = "Use insect traps and rotate crops seasonally."
        calendar = "🌱 Planting: May | 🌾 Harvesting: September"

    # Output sections
    st.subheader("🌿 Recommended Crops")
    st.write(", ".join(crops))

    st.subheader("💡 Farming Tip")
    st.info(tip)

    st.subheader("🧪 Fertilizer Recommendation")
    st.write(fertilizer)

    st.subheader("🛡️ Pest Control Advice")
    st.write(pest_control)

    st.subheader("📅 Planting Calendar")
    st.write(calendar)

    st.markdown("---")
    st.caption("🚀 Built by Adefuye Abiodun | 3MTT Nigeria – Smart Agro Project 2025")

    st.success("📢 Smart Agro Insight: 'The future of farming is data-driven. Stay informed, stay ahead!'")
