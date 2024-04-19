import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv(r'C:\Users\HOME\Desktop\새싹_교육\GitHub_CHOI\project_5_flow-of-time-visualization\자료실\Master daily sales.csv')

# Set up the Streamlit interface
st.title('Sales Data Analysis and Visualization')
st.write('This is a web dashboard for displaying sales data.')

# Display the data
st.subheader('Sales Data')
st.dataframe(data)

# Plot sales trends over years
st.subheader('Yearly Sales Trends')
plt.figure(figsize=(10, 6))
for column in data.columns[1:]:
    sns.lineplot(data=data, x='TIME', y=column, label=column)
plt.xticks(rotation=45)
plt.ylabel('Sales')
plt.legend(title='Year')
st.pyplot(plt)

# Create a heatmap
st.subheader('Sales Heatmap')
plt.figure(figsize=(10, 8))
heatmap_data = data.set_index('TIME')
sns.heatmap(heatmap_data, annot=True, cmap='viridis', linewidths=.5)
st.pyplot(plt)
