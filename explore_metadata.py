import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import wordcloud as wc

df=pd.read_csv('metadata.csv', low_memory=False)
print(f"the top data : '{df.head()})'")
print(f"the shape of the data : '{df.shape}'")
# Display the first few rows of the DataFrame
print(f"the columns of the data : '{df.columns}'")
print(f"the info of the data : '{df.info()}'")

# identify data types of each column
print(f"the data types of each column : '{df.dtypes}'")

# check for missing values in important columns
print(f"the missing values in each column : '{df.isnull().sum()}'")

# statistical summary of numerical columns
print(f"the statistical summary of numerical columns : '{df.describe()}'")


# identify columns with missing values
missing_values = df.isnull().sum()

#remove missing values
df_cleaned = df.dropna(subset=['title', 'genre', 'release_year', 'rating'])

#create a cleaned version of the dataset
df=df_cleaned 

#convert date columns to datetime format
df['release_date'] = pd.to_datetime(df['release_date'], errors='coerce')
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')

#extract year from publication date for time-based analysis
df['release_year'] = df['release_date'].dt.year

#create new columns e.g abstract word count
df['title_word_count'] = df['title'].apply(lambda x: len(str(x).split()))


#perform basic analysis
#count papers by publication year
papers_by_year = df['release_year'].value_counts().sort_index()

#identify top journals pub;ication year
top_genres = df['genre'].value_counts().head(10)

#find most frequent words inntittles
from collections import Counter
all_words = ' '.join(df['title'].dropna()).split()
word_counts = Counter(all_words)
most_common_words = word_counts.most_common(10)

#plot number of publications over time
plt.figure(figsize=(10, 6))
sns.lineplot(x=papers_by_year.index, y=papers_by_year.values)
plt.title('Number of Publications Over Time')
plt.xlabel('Year')
plt.ylabel('Number of Publications')
plt.show()

#create a bar chart of top publishing journals
plt.figure(figsize=(10, 6))
sns.barplot(x=top_genres.values, y=top_genres.index)
plt.title('Top 10 Genres')

#generate a word cloud of paper titles
from wordcloud import WordCloud
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(' '.join(all_words))
plt.figure(figsize=(10, 6))

#plot distribution of paper counts by source
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off') 
plt.figure(figsize=(10, 6))
sns.histplot(df['rating'].dropna(), bins=20, kde=True)  
plt.title('Distribution of Ratings')
plt.xlabel('Rating')
plt.ylabel('Count')
plt.show()

import pandas as pd

def explore_metadata():
    # Load the metadata.csv file
    df = pd.read_csv('metadata.csv', low_memory=False)
    
    # Print the shape of the DataFrame
    print(f"DataFrame shape: {df.shape}")
    
    # Print the first 5 rows
    print("First 5 rows:")
    print(df.head())
    
    # Print data types of each column
    print("\\nData types:")
    print(df.dtypes)
    
    # Print count of missing values per column
    print("\\nMissing values per column:")
    print(df.isnull().sum())

if __name__ == "__main__":
    explore_metadata()

