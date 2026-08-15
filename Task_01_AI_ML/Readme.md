# Netflix Data Analysis & Exploratory Data Analysis

## 📌 Project Overview

This project focuses on analyzing the Netflix Titles dataset using Python and popular data analysis and visualization libraries. The objective is to clean, explore, visualize, and extract meaningful insights from Netflix movies and TV shows.

The project follows a complete Exploratory Data Analysis (EDA) workflow, including data loading, data understanding, data cleaning, statistical analysis, visualization, and insight generation.

---

## 🎯 Objectives

The main objectives of this project are:

* Understand the structure and characteristics of the Netflix dataset.
* Identify and handle missing values.
* Detect and correct inconsistent or invalid data.
* Perform statistical analysis on numerical and categorical data.
* Explore relationships and patterns within the dataset.
* Create meaningful visualizations.
* Generate actionable insights from the data.
* Practice Python-based data analysis and visualization techniques.

---

## 📊 Dataset

The dataset contains information about Netflix movies and TV shows.

### Dataset Size

* **Rows:** 8,807
* **Columns:** 12 original columns
* **Final columns:** 13 after creating the `duration_value` feature.

### Main Features

| Column           | Description                         |
| ---------------- | ----------------------------------- |
| `show_id`        | Unique identifier of the title      |
| `type`           | Movie or TV Show                    |
| `title`          | Title name                          |
| `director`       | Director of the title               |
| `cast`           | Cast members                        |
| `country`        | Country of production               |
| `date_added`     | Date the title was added to Netflix |
| `release_year`   | Original release year               |
| `rating`         | Content rating                      |
| `duration`       | Movie duration or number of seasons |
| `listed_in`      | Genres/categories                   |
| `description`    | Title description                   |
| `duration_value` | Numeric representation of duration  |

---

## 🛠️ Technologies & Libraries Used

* **Python**
* **Pandas** – Data manipulation and analysis
* **NumPy** – Numerical computations
* **Matplotlib** – Data visualization
* **Seaborn** – Statistical visualization
* **Jupyter Notebook** – Development environment

---

## 🧹 Data Cleaning & Preparation

The dataset was inspected and cleaned before performing exploratory analysis.

The following preprocessing steps were performed:

### Missing Values

Missing values were identified using Pandas and handled appropriately.

Categorical missing values such as:

* `director`
* `cast`
* `country`

were replaced with `Unknown`.

### Date Conversion

The `date_added` column was converted from string format to a datetime data type.

### Invalid Rating Values

Three invalid values were identified in the `rating` column:

* `74 min`
* `84 min`
* `66 min`

These values were actually movie durations that had been incorrectly stored in the `rating` column.

The values were moved to the `duration` column, while the invalid ratings were replaced with the mode of the rating column.

### Duration Processing

A numeric `duration_value` column was created to make duration-related analysis easier.

---

## 📈 Exploratory Data Analysis

Several visualizations were created to understand the distribution and relationships within the dataset.

### Visualizations Created

1. Histogram
2. Bar Chart
3. Pie Chart
4. Scatter Plot
5. Line Chart
6. Box Plot
7. Correlation Heatmap
8. Count Plot
9. Pair Plot
10. Violin Plot

These visualizations were used to analyze content types, ratings, release years, distributions, relationships, and other patterns in the dataset.

---

## 🔍 Key Insights

The analysis produced several important findings:

1. **Movies are the dominant content type**, with 6,131 titles representing approximately 69.62% of the dataset.

2. **TV Shows account for approximately 30.38%** of the dataset, with 2,676 titles.

3. **TV-MA is the most common content rating**, with 3,214 titles.

4. **The United States is the most represented country**, with 2,818 titles.

5. **India is the second most represented country**, with 972 titles.

6. **The median release year is 2017**, indicating that the dataset contains a strong concentration of relatively recent content.

7. **2018 is the most frequently occurring release year** in the dataset.

8. The **average release year is approximately 2014.18**.

9. The dataset covers a wide release period from **1925 to 2021**, representing approximately 96 years of content.

10. The `director` column originally contained the largest number of missing values, with **2,634 missing records**.

---

## 📊 Final Dataset Status

After preprocessing:

* **Rows:** 8,807
* **Columns:** 13
* Missing values were handled in the major categorical columns.
* `date_added` was converted to datetime format.
* Invalid rating values were corrected.
* `duration_value` was created for numerical duration analysis.

The remaining 10 missing values in `date_added` represent records where the original dataset did not provide an added date.

---

## 📁 Project Structure

```text
Netflix-Data-Analysis/
│
├── Netflix_Data_Analysis.ipynb
├── netflix_titles.csv
├── README.md
└── images/
```

---

## ▶️ How to Run the Project

### 1. Clone the repository

```bash
git clone <your-repository-url>
```

### 2. Open the project folder

```bash
cd Netflix-Data-Analysis
```

### 3. Install required libraries

```bash
pip install pandas numpy matplotlib seaborn jupyter
```

### 4. Open Jupyter Notebook

```bash
jupyter notebook
```

### 5. Open

```text
Netflix_Data_Analysis.ipynb
```

Run the notebook cells from top to bottom.

---

## 🎓 Learning Outcomes

Through this project, I gained practical experience in:

* Data Cleaning
* Data Preprocessing
* Exploratory Data Analysis
* Statistical Analysis
* Missing Value Handling
* Data Validation
* Feature Creation
* Data Visualization
* Pandas and NumPy
* Matplotlib and Seaborn
* Extracting insights from real-world datasets

---

## 🏁 Conclusion

This project provided practical experience in performing a complete data analysis workflow on a real-world Netflix dataset. The analysis involved data cleaning, preprocessing, statistical analysis, exploratory data analysis, visualization, and insight generation.

The findings showed that Netflix's catalog in the dataset is dominated by Movies, with the United States being the most represented country and TV-MA being the most common rating. The project also demonstrated how data inconsistencies and missing values can be identified and handled using Python.

Overall, this project strengthened practical skills in Python, Pandas, NumPy, Matplotlib, Seaborn, data cleaning, exploratory data analysis, and data visualization, providing a strong foundation for future data science and machine learning projects.

---

## 👨‍💻 Author

**Ehtisham Javaid**

BS Computer Science Student

---

## ⭐ Project

This project was completed as part of an **AI/ML Internship Task** focused on Data Analysis and Exploratory Data Analysis.
