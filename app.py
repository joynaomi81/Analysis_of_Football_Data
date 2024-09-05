import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title for the Streamlit app
st.title("Analysis of Football Data")

# Load the data
@st.cache  # Cache the data loading for better performance
def load_data():
    # Replace this with the path to your dataset
    df = pd.read_csv("/content/drive/MyDrive/Colab Notebooks/players_fifa22.csv")  
    return df

# Load data
data = load_data()

# Sidebar for user input
st.sidebar.header("User Input Features")
team_selected = st.sidebar.selectbox('Select a team:', data['Team'].unique())
position_selected = st.sidebar.selectbox('Select a position:', data['Position'].unique())

# Filter data based on user selection
filtered_data = data[(data['Team'] == team_selected) & (data['Position'] == position_selected)]

# Display the filtered data
st.write(f"Showing players from {team_selected} playing as {position_selected}")
st.dataframe(filtered_data)

# Example visualization (e.g., Age vs. Overall Rating)
st.write(f"Player Age vs. Overall Rating for {team_selected}")
fig, ax = plt.subplots()
ax.scatter(filtered_data['Age'], filtered_data['Overall'])
plt.xlabel('Age')
plt.ylabel('Overall Rating')
st.pyplot(fig)

# Add more sections and analysis based on your notebook code...
