import streamlit as st
import pandas as pd

if "reservations" not in st.session_state:
    st.session_state["reservations"] = []

# App title
st.title("Priority Pass Lounge Reservations by HyperJets")

# Sidebar application form
st.sidebar.header("Make a Reservation")
with st.sidebar.form("reservation_form"):
    id_number = st.text_input("Identification Number")
    name = st.text_input("Name")
    reservation_date = st.date_input("Reservation Date")
    reservation_time = st.time_input("Reservation Time")
    membership_type = st.selectbox(
        "Membership Type", 
        ["Bronze", "Silver", "Gold", "Platinum", "HyperJets Executive"]
    )
    suite_number = st.number_input("Suite Number", min_value=1, step=1)
    suite_type = st.selectbox(
        "Suite Type", 
        ["Commons", "Basic Suite", "Executive Suite", "Presidential Suite"]
    )
    status = st.selectbox(
        "Reservation Status", 
        ["Scheduled", "Arrived", "Departed"]
    )
    submitted = st.form_submit_button("Submit Reservation")
    
    if submitted:
        new_reservation = {
            "ID": id_number,
            "Name": name,
            "Reservation Date": reservation_date,
            "Reservation Time": reservation_time,
            "Membership Type": membership_type,
            "Suite Number": suite_number,
            "Suite Type": suite_type,
            "Status": status
        }
        st.session_state["reservations"].append(new_reservation)
        st.success("Reservation added successfully!")

# Display current reservations
st.header("Current Reservations")
if st.session_state["reservations"]:
    reservations_df = pd.DataFrame(st.session_state["reservations"])
    st.dataframe(reservations_df)

    # Add a delete option
    st.subheader("Manage Reservations")
    selected_id = st.selectbox(
        "Select a Reservation to Delete by ID",
        options=[res["ID"] for res in st.session_state["reservations"]]
    )
    delete_button = st.button("Delete Reservation")
    if delete_button:
        st.session_state["reservations"] = [
            res for res in st.session_state["reservations"] if res["ID"] != selected_id
        ]
        st.success(f"Reservation with ID {selected_id} deleted.")
else:
    st.info("No reservations yet. Use the form on the sidebar to add a new reservation.")