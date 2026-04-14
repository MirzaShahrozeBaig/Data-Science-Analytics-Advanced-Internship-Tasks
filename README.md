# Data-Science-Analytics-Advanced-Internship-Tasks( 1, 2, 3 & 5)

## 🔍 Overview

This repository contains multiple data science projects completed as part of a Data Science & Analytics Internship. The tasks focus on solving real-world problems using machine learning, time series forecasting, clustering, and business intelligence techniques.

Each project demonstrates practical implementation of data analysis, model building, and data-driven decision-making.

---

# 🟢 Task 1: Term Deposit Subscription Prediction

## 🎯 Objective

Predict whether a bank customer will subscribe to a term deposit based on marketing campaign data.

## 📊 Dataset

Bank Marketing Dataset (UCI Repository)

## ⚙️ Approach

* Data cleaning and preprocessing
* Encoding categorical variables
* Exploratory Data Analysis (EDA)
* Model training:

  * Logistic Regression
  * Random Forest
* Model evaluation using:

  * Confusion Matrix
  * F1 Score
  * ROC Curve
* Model interpretability using SHAP (Explainable AI)

## 📈 Results

* Built classification models to predict customer subscription
* Evaluated performance using multiple metrics
* Applied SHAP to explain model predictions

## 💡 Insights

* Identified key features influencing customer decisions
* Model helps improve targeting in marketing campaigns

## 🛠 Tools & Libraries

Python, Pandas, NumPy, Scikit-learn, XGBoost, SHAP, Matplotlib, Seaborn

---

# 🟢 Task 2: Customer Segmentation using K-Means

## 🎯 Objective

Segment customers based on income and spending behavior to support targeted marketing strategies.

## 📊 Dataset

Mall Customers Dataset:

* Gender
* Age
* Annual Income (k$)
* Spending Score (1–100)

## ⚙️ Approach

* Data cleaning and preprocessing
* Exploratory Data Analysis (EDA)
* Feature selection
* K-Means clustering
* Elbow Method to find optimal clusters (K=5)
* PCA for visualization

## 📈 Results

* Identified 5 distinct customer segments
* Clear separation based on income and spending behavior

## 💡 Insights

* High income + high spending → Premium customers
* Low income + high spending → Discount-driven customers
* High income + low spending → Potential growth segment

## 🛠 Tools & Libraries

Python, Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn

---

# 🟢 Task 3: Energy Consumption Forecasting

## 🎯 Objective

Forecast short-term household energy usage using historical time series data.

## 📊 Dataset

Household Power Consumption Dataset with datetime and energy usage features.

## ⚙️ Approach

* Data cleaning and handling missing values
* Datetime parsing and indexing
* Time series resampling (hourly)
* Feature engineering:

  * Hour
  * Day
  * Month
  * Day of week
* Model implementation:

  * ARIMA
  * Prophet
  * XGBoost
* Evaluation using:

  * MAE
  * RMSE

## 📈 Results

* XGBoost achieved best performance
* Prophet captured seasonality effectively
* ARIMA provided baseline comparison

## 💡 Insights

* Energy usage shows strong time-based patterns
* Feature engineering improves model performance
* Useful for demand forecasting

## 🛠 Tools & Libraries

Python, Pandas, NumPy, Scikit-learn, Statsmodels, Prophet, XGBoost, Matplotlib, Seaborn

---

# 🟢 Task 3: Loan Default Risk Prediction

## 🎯 Objective

Predict whether a customer will default on a loan and optimize decisions based on business cost.

## ⚙️ Approach

* Data cleaning and preprocessing
* Encoding categorical variables
* Logistic Regression model for classification
* Model evaluation using Confusion Matrix and F1 Score
* Applied threshold tuning to reduce business cost

## 📊 Key Idea

* False Negative → High financial loss
* False Positive → Lost opportunity
* Optimized threshold to minimize total cost

## 📈 Result

* Built a model to predict loan default risk
* Improved decision-making using cost-based optimization

## 🛠 Tools

Python, Pandas, NumPy, Scikit-learn

## 🧾 Conclusion

This project shows how machine learning can help reduce financial risk by combining prediction with business cost optimization.


# 🟢 Task 5: Interactive Business Dashboard (Streamlit)

## 🎯 Objective

Build an interactive dashboard to analyze sales and profit performance.

## 📊 Dataset

Global Superstore Dataset:

* Sales
* Profit
* Customer Name
* Region
* Category
* Sub-Category

## ⚙️ Approach

* Data cleaning using Pandas
* Exploratory Data Analysis
* Visualization using Matplotlib
* Dashboard development using Streamlit
* Added filters:

  * Region
  * Category
  * Sub-Category

## 📈 Results

* Identified top-performing regions
* Found top 5 customers by sales
* Built dynamic KPIs:

  * Total Sales
  * Total Profit
* Created fully interactive dashboard

## 💡 Insights

* Clear understanding of regional performance
* Customer contribution analysis
* Helps in business decision-making

## 🛠 Tools & Libraries

Python, Pandas, Matplotlib, Streamlit

---

# 🚀 Key Skills Demonstrated

* Machine Learning (Classification & Clustering)
* Time Series Forecasting
* Feature Engineering
* Data Visualization
* Explainable AI (SHAP)
* Business Intelligence & Dashboarding

---

# 🧾 Conclusion

These projects demonstrate the practical application of data science techniques to real-world business problems. The work highlights the ability to:

* Build predictive models
* Extract actionable insights
* Develop interactive dashboards
* Support data-driven decisions

---

# 👤 Author

Completed as part of a **Data Science & Analytics Internship (Phase 2)**.
