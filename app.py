import streamlit as st
import time
import random

st.set_page_config(page_title="Hospital Queue System")

st.title("🏥 Smart Hospital Queue Management")

# Sidebar
st.sidebar.header("Patient Details")

name = st.sidebar.text_input("Enter your name")
age = st.sidebar.number_input("Enter your age", min_value=1, max_value=100)
department = st.sidebar.selectbox(
    "Select Department",
    ["General", "Cardiology", "Orthopedics", "Dermatology"]
)

if st.sidebar.button("Book Appointment"):
    if name == "":
        st.warning("Please enter your name")
    else:
        token = random.randint(100, 999)
        wait_time = random.randint(10, 60)

        st.success(f"✅ Appointment Confirmed for {name}")
        
        st.subheader("🪪 Your Token Details")
        st.write(f"**Token Number:** {token}")
        st.write(f"**Department:** {department}")
        st.write(f"**Estimated Waiting Time:** {wait_time} minutes")

        st.info("📲 You will receive notification when your turn is near.")

        # Simulated progress
        st.subheader("⏳ Queue Status")
        progress = st.progress(0)

        for i in range(100):
            time.sleep(0.02)
            progress.progress(i + 1)

        st.success("🎉 It's your turn now!")

# Display info
st.markdown("---")
st.subheader("📊 Live Queue Info")

st.write("Total Patients Waiting:", random.randint(5, 30))
st.write("Doctors Available:", random.randint(2, 5))