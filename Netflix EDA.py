import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv(r"C:\Users\HP\Downloads\netflix_titles.csv.csv")

print(df.shape)
print(df.info())
print(df.isnull().sum())
print(df.describe(include='all'))

#CLEANING
df = df.drop_duplicates()

df['director'] = df['director'].fillna("Unknown")
df['cast'] = df['cast'].fillna("Unknown")
df['country'] = df['country'].fillna("Unknown")
df['date_added'] = df['date_added'].fillna(df['date_added'].mode()[0])
df['rating'] = df['rating'].fillna(df['rating'].mode()[0])
df['duration'] = df['duration'].fillna("Unknown")

#OBJECTIVE 1: Content Production vs Country
top_countries = df['country'].value_counts().head(10)
sns.barplot(x=top_countries.values, y=top_countries.index)
plt.title("Content Production vs Country")
plt.show()

# OBJECTIVE 2: Content Production vs Year
year_count = df['release_year'].value_counts().sort_index()
sns.lineplot(x=year_count.index, y=year_count.values)
plt.title("Content Production vs Year")
plt.show()

#OBJECTIVE 3: Proportion of Movies vs TV Shows
sns.countplot(x=df['type'])
plt.title("Movies vs TV Shows")
plt.show()

#OBJECTIVE 4: Genre Analysis
genres = df['listed_in'].str.split(', ', expand=True).stack()
top_genres = genres.value_counts().head(15)
sns.barplot(x=top_genres.values, y=top_genres.index)
plt.title("Top Genres on Netflix")
plt.show()

#OBJECTIVE 5: Rating Distribution (Audience Targeting)
rating_count = df['rating'].value_counts().head(12)
sns.barplot(x=rating_count.values, y=rating_count.index)
plt.title("Rating Distribution (Audience Targeting)")
plt.show()
