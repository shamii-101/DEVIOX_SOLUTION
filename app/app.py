import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Netflix Data Analysis",
    page_icon="🎬",
    layout="wide"
)

# --------------------------------------------------
# Load Dataset
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "dataset" / "netflix_titles.csv"

df = pd.read_csv(DATA_PATH)

# --------------------------------------------------
# Title
# --------------------------------------------------

st.title("🎬 Netflix Data Analysis Dashboard")
st.write("Devixo Solutions AI/ML Internship – Task 01")

st.divider()

# --------------------------------------------------
# Main KPI Cards
# --------------------------------------------------

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Titles", len(df))

with col2:
    st.metric("Movies", (df["type"] == "Movie").sum())

with col3:
    st.metric("TV Shows", (df["type"] == "TV Show").sum())

# --------------------------------------------------
# Additional KPI Cards
# --------------------------------------------------

col1, col2, col3 = st.columns(3)

with col1:
    countries_count = (
        df["country"]
        .dropna()
        .str.split(", ")
        .explode()
        .nunique()
    )

    st.metric("Countries Represented", countries_count)

with col2:
    st.metric("Release Years", df["release_year"].nunique())

with col3:
    st.metric("Most Common Rating", df["rating"].mode()[0])

st.divider()

# --------------------------------------------------
# Sidebar Filters
# --------------------------------------------------

st.sidebar.header("🔎 Dashboard Filters")

# Content Type Filter
content_types = st.sidebar.multiselect(
    "Select Content Type",
    options=df["type"].unique(),
    default=df["type"].unique()
)

filtered_df = df[df["type"].isin(content_types)]

# Rating Filter
rating_options = sorted(
    filtered_df["rating"].dropna().unique()
)

selected_ratings = st.sidebar.multiselect(
    "Select Rating",
    options=rating_options,
    default=rating_options
)

filtered_df = filtered_df[
    filtered_df["rating"].isin(selected_ratings)
]

# --------------------------------------------------
# Filtered Dataset Count
# --------------------------------------------------

st.subheader("📊 Filtered Dataset")

st.write(
    f"Showing **{len(filtered_df):,} titles** based on selected filters."
)

# --------------------------------------------------
# Movies vs TV Shows
# --------------------------------------------------

st.subheader("🎥 Movies vs TV Shows")

type_counts = filtered_df["type"].value_counts()

fig, ax = plt.subplots(figsize=(8, 5))

type_counts.plot(
    kind="bar",
    ax=ax
)

ax.set_title("Movies vs TV Shows")
ax.set_xlabel("Content Type")
ax.set_ylabel("Number of Titles")
ax.tick_params(axis="x", rotation=0)

st.pyplot(fig)

plt.close(fig)

# --------------------------------------------------
# Rating Distribution
# --------------------------------------------------

st.subheader("⭐ Content Rating Distribution")

rating_counts = (
    filtered_df["rating"]
    .value_counts()
    .head(10)
)

fig, ax = plt.subplots(figsize=(10, 5))

rating_counts.plot(
    kind="bar",
    ax=ax
)

ax.set_title("Top 10 Content Ratings")
ax.set_xlabel("Rating")
ax.set_ylabel("Number of Titles")
ax.tick_params(axis="x", rotation=45)

st.pyplot(fig)

plt.close(fig)

# --------------------------------------------------
# Release Year Trend
# --------------------------------------------------

st.subheader("📅 Titles by Release Year")

year_counts = (
    filtered_df["release_year"]
    .value_counts()
    .sort_index()
)

fig, ax = plt.subplots(figsize=(10, 5))

ax.plot(
    year_counts.index,
    year_counts.values
)

ax.set_title("Netflix Titles by Release Year")
ax.set_xlabel("Release Year")
ax.set_ylabel("Number of Titles")

st.pyplot(fig)

plt.close(fig)

# --------------------------------------------------
# Top 10 Countries
# --------------------------------------------------

st.subheader("🌍 Top 10 Countries")

country_counts = (
    filtered_df["country"]
    .dropna()
    .loc[lambda x: x != "Unknown"]
    .str.split(", ")
    .explode()
    .value_counts()
    .head(10)
)

fig, ax = plt.subplots(figsize=(10, 5))

country_counts.sort_values().plot(
    kind="barh",
    ax=ax
)

ax.set_title("Top 10 Countries by Number of Titles")
ax.set_xlabel("Number of Titles")
ax.set_ylabel("Country")

st.pyplot(fig)

plt.close(fig)

# --------------------------------------------------
# Dataset Preview
# --------------------------------------------------

st.subheader("📋 Dataset Preview")

st.dataframe(
    filtered_df.head(10),
    use_container_width=True
)

# --------------------------------------------------
# Footer
# --------------------------------------------------

st.divider()

st.caption(
    "Devixo Solutions AI/ML Internship Program – Task 01 | "
    "Python Programming, Data Analysis & Visualization"
)