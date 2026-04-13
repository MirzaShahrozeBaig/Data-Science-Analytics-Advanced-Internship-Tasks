
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ==============================
# PAGE CONFIG
# ==============================
st.set_page_config(
    page_title="Business Dashboard",
    layout="wide"
)

st.title("📊 Sales & Profit Dashboard")
st.markdown("Analyze sales, profit, and customer performance")

# ==============================
# LOAD DATA
# ==============================
@st.cache_data
def load_data():
    # Load dataset from the local file
    df_loaded = pd.read_csv('superstore.csv', sep=',')
    df_loaded['Order.Date'] = pd.to_datetime(df_loaded['Order.Date'])

    # Select relevant columns and correct column names
    df_processed = df_loaded[[
        'Order.Date',
        'Region',
        'Category',
        'Sub.Category', # Corrected from 'Sub-Category'
        'Customer.Name', # Corrected from 'Customer Name'
        'Sales',
        'Profit'
    ]]
    return df_processed

df = load_data()

# ==============================
# SIDEBAR FILTERS
# ==============================
st.sidebar.header("🔍 Filters")

region = st.sidebar.multiselect(
    "Select Region",
    df['Region'].unique(),
    default=df['Region'].unique()
)

category = st.sidebar.multiselect(
    "Select Category",
    df['Category'].unique(),
    default=df['Category'].unique()
)

sub_category = st.sidebar.multiselect(
    "Select Sub-Category",
    df['Sub.Category'].unique(), # Corrected from 'Sub-Category'
    default=df['Sub.Category'].unique()
)

# ==============================
# APPLY FILTERS
# ==============================
filtered_df = df[
    (df['Region'].isin(region)) &
    (df['Category'].isin(category)) &
    (df['Sub.Category'].isin(sub_category)) # Corrected from 'Sub-Category'
]

# ==============================
# KPIs
# ==============================
total_sales = filtered_df['Sales'].sum()
total_profit = filtered_df['Profit'].sum()

col1, col2 = st.columns(2)

with col1:
    st.metric("💰 Total Sales", f"${total_sales:,.2f}")

with col2:
    st.metric("📈 Total Profit", f"${total_profit:,.2f}")

# ==============================
# TOP CUSTOMERS
# ==============================
st.subheader("🏆 Top 5 Customers by Sales")

top_customers = (
    filtered_df.groupby('Customer.Name')['Sales'] # Corrected from 'Customer Name'
    .sum()
    .sort_values(ascending=False)
    .head(5)
)

st.dataframe(top_customers)

# ==============================
# CHARTS
# ==============================

# Sales by Category
sales_by_category = filtered_df.groupby('Category')['Sales'].sum()
fig1, ax1 = plt.subplots()
sales_by_category.plot(kind='bar', ax=ax1)
ax1.set_title("Sales by Category")
st.pyplot(fig1)

# Profit by Region
profit_by_region = filtered_df.groupby('Region')['Profit'].sum()
fig2, ax2 = plt.subplots()
profit_by_region.plot(kind='bar', ax=ax2)
ax2.set_title("Profit by Region")
st.pyplot(fig2)

# Sales over time
sales_over_time = filtered_df.groupby('Order.Date')['Sales'].sum() # Corrected from 'Order Date'
fig3, ax3 = plt.subplots()
sales_over_time.plot(ax=ax3)
ax3.set_title("Sales Over Time")
st.pyplot(fig3)

# ==============================
# FOOTER
# ==============================
st.markdown("---")
st.markdown("### 📌 Dashboard Insights")
st.write("This dashboard helps analyze sales trends, profit performance, and customer contributions.")
