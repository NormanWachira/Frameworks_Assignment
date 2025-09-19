# Frameworks

# Basic Data Analysis – CORD-19 Dataset

This project demonstrates the full workflow of working with a real dataset (`metadata.csv`) using **Python, pandas, matplotlib, seaborn, and Streamlit**.

---

## Tasks Completed

### Part 1: Data Loading & Exploration
- Load `metadata.csv` into pandas DataFrame
- Preview rows, dataset shape, data types, missing values

### Part 2: Data Cleaning & Preparation
- Handle missing values (drop rows where needed)
- Convert `publish_time` to datetime
- Extract year of publication
- Add `abstract_word_count` column

### Part 3: Data Analysis & Visualization
- Publications by year (bar chart)
- Top 10 journals publishing COVID-19 research
- Word cloud of paper titles
- Distribution of sources

### Part 4: Streamlit App
- Interactive filters (year range)
- Dynamic bar charts for publications and journals
- Display of sample data

### Part 5: Documentation & Reflection
- Code is **commented** for clarity
- README explains project steps and how to run
- Reflection: learned dataset cleaning, visualization, Streamlit basics

---

## Requirements

Make sure these Python libraries are installed:

- pandas  
- matplotlib  
- seaborn  
- streamlit  
- (optional) wordcloud  


---

## How to Run

### 1. Run as a Python script
```bash
python cord19_analysis.py
```

**### 2. Run as a Streamlit app**
```bash
streamlit run cord19_analysis.py
```
