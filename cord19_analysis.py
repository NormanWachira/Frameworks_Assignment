# Import the necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import streamlit as st

# Part 1: Load and explore the dataset
try:
    # Load only useful columns + limit rows to avoid memory issues
    use_columns = ["title", "publish_time", "journal", "abstract", "source_x"]
    df = pd.read_csv("metadata.csv", usecols=use_columns, nrows=50000, low_memory=False)
    print("Dataset loaded successfully! (using 50,000 rows for performance)")
except FileNotFoundError:
    print("Error: metadata.csv file not found. Place it in the same folder as this script.")
    exit()
except Exception as e:
    print("Error loading dataset:", e)
    exit()

# Show a preview
print("\nFirst 5 rows:")
print(df.head())
print("\nShape (rows, columns):", df.shape)
print("\nInfo:")
print(df.info())
print("\nMissing values (all columns):")
print(df.isnull().sum())

# Part 2: Data cleaning and preparations

# Drop rows where publish_time or journal is missing
df = df.dropna(subset=["publish_time", "journal"])

# Convert publish_time to datetime
df["publish_time"] = pd.to_datetime(df["publish_time"], errors="coerce")

# Extract year from publish_time
df["year"] = df["publish_time"].dt.year

# Add abstract word count column
df["abstract_word_count"] = df["abstract"].fillna("").apply(lambda x: len(x.split()))

print("\n Data cleaned! New shape:", df.shape)

# Part 3: Data analysis and visualizations

# 1. Publications by year
year_counts = df["year"].value_counts().sort_index()

plt.figure(figsize=(8,5))
year_counts.plot(kind="bar", color="skyblue")
plt.title("Publications by Year (Sampled Data)")
plt.xlabel("Year")
plt.ylabel("Number of Publications")
plt.tight_layout()
plt.savefig("publications_by_year.png")
plt.close()

# 2. Top 10 journals
top_journals = df["journal"].value_counts().head(10)

plt.figure(figsize=(8,5))
sns.barplot(x=top_journals.values, y=top_journals.index, palette="viridis")
plt.title("Top 10 Journals Publishing COVID-19 Research (Sampled Data)")
plt.xlabel("Number of Publications")
plt.ylabel("Journal")
plt.tight_layout()
plt.savefig("top_journals.png")
plt.close()

# 3. Word cloud of titles
titles = " ".join(df["title"].dropna().astype(str))
wordcloud = WordCloud(width=800, height=400, background_color="white").generate(titles)
wordcloud.to_file("wordcloud_titles.png")

# 4. Distribution of sources
if "source_x" in df.columns:
    source_counts = df["source_x"].value_counts().head(10)

    plt.figure(figsize=(8,5))
    sns.barplot(x=source_counts.values, y=source_counts.index, palette="magma")
    plt.title("Top Sources of Papers (Sampled Data)")
    plt.xlabel("Number of Papers")
    plt.ylabel("Source")
    plt.tight_layout()
    plt.savefig("source_distribution.png")
    plt.close()

print("\n Analysis complete. Plots saved in the same folder.")

# Part 4: Streamlit app
def run_streamlit_app():
    st.title("CORD-19 Data Explorer")
    st.write("Explore COVID-19 research publications interactively (metadata.csv).")

    # Sidebar filter for years
    min_year = int(df["year"].min())
    max_year = int(df["year"].max())
    year_range = st.slider("Select Year Range", min_year, max_year, (2020, 2021))
    df_filtered = df[(df["year"] >= year_range[0]) & (df["year"] <= year_range[1])]

    # Show publications by year
    st.write("### Publications by Year")
    st.bar_chart(df_filtered["year"].value_counts().sort_index())

    # Show top journals
    st.write("### Top Journals")
    st.bar_chart(df_filtered["journal"].value_counts().head(10))

    # Show sample data
    st.write("### Sample Data")
    st.dataframe(df_filtered.head())

# Only run Streamlit if started with `streamlit run`
if __name__ == "__main__":
    import sys
    if any("streamlit" in arg for arg in sys.argv):
        run_streamlit_app()
