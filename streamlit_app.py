import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

@st.cache_data
def load_data():
    df = pd.read_csv('metadata.csv', low_memory=False)
    df = df.dropna(subset=['title'])
    df['abstract'] = df['abstract'].fillna('')
    df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
    df['publish_year'] = df['publish_time'].dt.year
    df['abstract_word_count'] = df['abstract'].apply(lambda x: len(str(x).split()))
    return df

def plot_publications_by_year(df):
    yearly_counts = df['publish_year'].value_counts().sort_index()
    fig, ax = plt.subplots(figsize=(10, 5))
    yearly_counts.plot(kind='bar', ax=ax)
    ax.set_title('Number of Publications by Year')
    ax.set_xlabel('Year')
    ax.set_ylabel('Number of Papers')
    plt.xticks(rotation=45)
    st.pyplot(fig)

def plot_top_journals(df):
    top_journals = df['journal'].value_counts().head(10)
    fig, ax = plt.subplots(figsize=(10, 5))
    top_journals.plot(kind='barh', ax=ax)
    ax.set_title('Top 10 Journals Publishing COVID-19 Research')
    ax.set_xlabel('Number of Papers')
    ax.set_ylabel('Journal')
    st.pyplot(fig)

def plot_wordcloud(df):
    titles_text = ' '.join(df['title'].dropna())
    wordcloud = WordCloud(width=800, height=400, background_color='white', max_words=100).generate(titles_text)
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis('off')
    ax.set_title('Word Cloud of Paper Titles')
    st.pyplot(fig)

def plot_source_distribution(df):
    source_counts = df['source_x'].value_counts()
    fig, ax = plt.subplots(figsize=(8, 6))
    source_counts.plot(kind='pie', autopct='%1.1f%%', ax=ax)
    ax.set_ylabel('')
    ax.set_title('Distribution of Papers by Source')
    st.pyplot(fig)

def main():
    st.title("CORD-19 COVID-19 Research Papers Analysis")
    st.write("This app provides an interactive exploration of the CORD-19 metadata dataset.")

    df = load_data()

    st.sidebar.header("Filters")
    year_min = int(df['publish_year'].min())
    year_max = int(df['publish_year'].max())
    selected_years = st.sidebar.slider("Select publication year range", year_min, year_max, (year_min, year_max))

    filtered_df = df[(df['publish_year'] >= selected_years[0]) & (df['publish_year'] <= selected_years[1])]

    st.header("Publications by Year")
    plot_publications_by_year(filtered_df)

    st.header("Top Journals")
    plot_top_journals(filtered_df)

    st.header("Word Cloud of Paper Titles")
    plot_wordcloud(filtered_df)

    st.header("Distribution of Papers by Source")
    plot_source_distribution(filtered_df)

    st.header("Sample Data")
    st.dataframe(filtered_df[['title', 'publish_time', 'authors', 'journal']].head(10))

if __name__ == "__main__":
    main()
