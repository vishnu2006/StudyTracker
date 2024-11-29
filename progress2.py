import streamlit as st

# Define subjects and units
subjects = ['MSF', 'DS', 'JP', 'DLCA', 'OS', 'DBMS']
units = ['Unit 1', 'Unit 2', 'Unit 3', 'Unit 4', 'Unit 5']  # Updated units

# Initialize session state for all toggles if not already done
if 'toggles' not in st.session_state:
    st.session_state.toggles = {f"{subject}_{unit}": False for subject in subjects for unit in units}

# Function to toggle the state
def toggle_state(key):
    st.session_state.toggles[key] = not st.session_state.toggles[key]

st.title('Exam Study Tracker')

# Create a layout similar to an Excel sheet with subjects at the top
cols = st.columns([2, 2, 2, 2, 2, 2])  # Equal width columns for subjects

# Show subject names at the top
for i, subject in enumerate(subjects):
    cols[i].markdown(f"### {subject}")

# Now display the units below each subject (toggle buttons)
for unit in units:
    cols = st.columns([2, 2, 2, 2, 2, 2])
    for i, subject in enumerate(subjects):
        key = f"{subject}_{unit}"
        
        # Ensure the key exists in session_state before checking
        if key not in st.session_state.toggles:
            st.session_state.toggles[key] = False  # Initialize key if it doesn't exist

        if st.session_state.toggles[key]:
            # Green button if toggled
            if cols[i].button(f"✅ {unit}", key=key):
                toggle_state(key)
        else:
            # Red button if not toggled
            if cols[i].button(f"🔴 {unit}", key=key):
                toggle_state(key)
