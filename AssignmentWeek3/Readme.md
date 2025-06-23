# 📊 AI Job Market Data Visualization Project

This project provides a comprehensive visual analysis of the global AI job market using a dataset of 15,000 job listings. It explores trends in salaries, remote work, required skills, and company demographics through compelling data visualizations using Python libraries like Pandas, Matplotlib, and Seaborn.

---

## 📁 Dataset Overview

- **Source**: `ai_job_dataset.csv`
- **Records**: 15,000 job postings
- **Features**:
  - `job_id`, `job_title`, `company_name`
  - `salary_usd`, `salary_currency`
  - `experience_level`, `employment_type`
  - `remote_ratio`, `education_required`
  - `required_skills`, `years_experience`, `industry`
  - `company_location`, `employee_residence`, `company_size`
  - `job_description_length`, `benefits_score`
  - `posting_date`, `application_deadline`

---

## 🧠 Objectives

- Understand key trends in AI job postings globally
- Visualize distributions and relationships among job attributes
- Gain insights into salary, experience, remote opportunities, and skills demand
- Explore how education, company size, and region impact job offerings

---

## 🛠️ Tech Stack

- **Language**: Python
- **Notebook**: Jupyter Notebook
- **Libraries**:
  - `pandas` for data manipulation
  - `matplotlib` and `seaborn` for data visualization
  - `numpy` for numerical operations

---

## 📊 Key Visualizations

### 🔹 Univariate Analysis
- Top 10 most common **Job Titles**
- Distribution of **Salaries (USD)**
- Count plot of **Experience Levels** (`EN`, `MI`, `SE`, `EX`)
- Distribution of **Remote Ratio** (0%, 50%, 100%)
- Count of **Education Requirements**
- **Company Sizes** distribution (`S`, `M`, `L`)

### 🔸 Bivariate & Multivariate Analysis
- **Salary vs Experience Level**
- **Remote Ratio vs Salary**
- **Years of Experience vs Salary**
- **Top Countries by Job Count**
- **Industry vs Salary**
- **Required Skills Word Cloud**
- Correlation heatmap of numerical features

---


---

## 🧹 Data Preprocessing

- Converted date fields (`posting_date`, `application_deadline`) to datetime format
- Verified numeric types for salary, experience, and benefits
- No missing data — dataset is already clean
- Skills and descriptions tokenized for analysis

---

## 📈 Insights Summary

- 🔝 Most AI jobs require at least a **Bachelor’s or Master’s degree**
- 💸 **Senior-level (SE)** and **Executive-level (EX)** roles offer the highest salaries
- 🌍 **100% remote** roles are most common in **US, India, and Europe**
- 🧑‍💻 Popular skills include: **Python, Deep Learning, NLP, Docker, AWS**
- 🏢 **Large companies** offer higher salaries but mid-size firms dominate in number

---

