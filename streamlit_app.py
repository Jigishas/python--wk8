import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("CORD-19 Data Explorer")
st.write("Simple exploration of COVID-19 research papers")

# Add interactive elements
year_range = st.slider("Select year range", 2019, 2022, (2020, 2021))

# Add visualizations based on selection
df = pd.read_csv('metadata.csv', low_memory=False)
df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
df['publish_year'] = df['publish_time'].dt.year
filtered_df = df[(df['publish_year'] >= year_range[0]) & (df['publish_year'] <= year_range[1])]
papers_by_year = filtered_df['publish_year'].value_counts().sort_index()
plt.figure(figsize=(10, 6))
plt.plot(papers_by_year.index, papers_by_year.values)
plt.title('Number of Publications Over Time')
plt.xlabel('Year')  

# add interactive widgets (sliders, dropdowns)
plt.ylabel('Number of Publications')
st.pyplot(plt)
st.write("Data filtered by year range:", year_range)

# Display visualizations in the app
st.bar_chart(papers_by_year)

st.write("Data filtered by year range:", year_range)

# show a sample data
st.write("Sample data from the dataset:")
st.dataframe(filtered_df.head())



