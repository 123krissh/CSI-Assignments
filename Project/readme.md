# 🧠 Customer Segmentation based on their purchasing behavior and demographics to target marketing strategies effectively

This project performs **Customer Segmentation** using the popular unsupervised machine learning algorithm **KMeans**. The goal is to group customers based on their purchasing behavior (e.g., annual income, spending score, age) to help businesses target marketing strategies effectively.

---

## 📊 Objective

- Segment customers into distinct groups using clustering
- Understand purchasing behavior using demographics like Age and Income
- Visualize the clusters for marketing insights

---

## 📁 Dataset

The dataset contains the following columns:

- `CustomerID`
- `Gender`
- `Age`
- `Annual Income (k$)`
- `Spending Score (1-100)`

Dataset Source: [Mall Customers Dataset - Kaggle](https://www.kaggle.com/datasets/vjchoudhary7/customer-segmentation-tutorial)

---

## 🔍 Methodology

1. **Data Preprocessing**
   - Handling missing values
   - Label encoding categorical data (e.g., Gender)
   - Feature scaling

2. **Elbow Method**
   - Used to determine the optimal number of clusters (K)

3. **KMeans Clustering**
   - Customers grouped based on selected features (e.g., Age, Income, Spending Score)

4. **Visualization**
   - Scatter plots to display customer clusters
   - Color-coded clusters to show patterns in Age, Income, and Spending Score

---

## 📈 Visualizations

- **Age vs Spending Score**
- **Annual Income vs Spending Score**

These plots help businesses understand what kind of customers spend more, which age/income groups are high-value, etc.

---

## 📦 Libraries Used

- `pandas`
- `numpy`
- `matplotlib`
- `seaborn`
- `scikit-learn`

---

## 🚀 How to Run

1. Clone this repository or download the notebook.
2. Install required packages (preferably in a virtual environment)
3. Open CustomerSegmentation.ipynb and run all cells.

## 📌 Results

- The Elbow Method suggested K = 5 as an optimal number of clusters.
- Each cluster represents a unique customer segment (e.g., high income & high spenders, young low spenders, etc.).
- Visual plots clearly show segmentation based on behavior and demographics.

## 📬 Future Work

- Apply DBSCAN or Hierarchical Clustering for comparison.
- Integrate customer feedback or transaction history.
- Build a dashboard using Streamlit or Plotly Dash for real-time customer insights.

## 🙋‍♂️ Author

- **Krishna Suthar**
- B.Tech AI & Data Science
- Portfolio: [Krishna-suthar](https://krishna-suthar.vercel.app/)
- GitHub: [123krissh](https://github.com/123krissh)
