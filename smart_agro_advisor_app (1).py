
import streamlit as st

st.set_page_config(page_title="Smart Agro Advisor", layout="centered")

st.title("🌾 Smart Agro Advisor")
st.markdown("**Helping Farmers Make Smart Decisions**")

st.subheader("📝 Input Your Farm Details")

region = st.selectbox("Select your region:", ["Southwest", "Northwest", "Southeast", "Northeast"])
soil_type = st.selectbox("Select your soil type:", ["Loamy", "Sandy", "Clay", "Silty"])
season = st.selectbox("Current season:", ["Rainy", "Dry"])

if st.button("Get Recommendation"):
    st.success("✅ Advice generated successfully!")

    if soil_type == "Loamy" and season == "Rainy":
        crops = ["Maize", "Rice", "Tomatoes"]
        tip = "Loamy soil retains moisture well, perfect for maize and rice. Ensure regular weeding."
    elif soil_type == "Sandy":
        crops = ["Cassava", "Groundnut", "Watermelon"]
        tip = "Sandy soil drains quickly. Mulch heavily and irrigate regularly."
    elif soil_type == "Clay":
        crops = ["Sugarcane", "Rice", "Soybeans"]
        tip = "Clay soil can be waterlogged. Create proper drainage."
    else:
        crops = ["Yam", "Sorghum", "Millet"]
        tip = "Monitor moisture levels and apply compost regularly."

    st.subheader("🌱 Recommended Crops")
    st.write(", ".join(crops))

    st.subheader("💡 Planting Tip")
    st.info(tip)

    st.markdown("---")
    st.caption("Built by Adefuye Abiodun | Smart Agro Project 2025")

