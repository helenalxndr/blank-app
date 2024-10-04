import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# Set Streamlit page configuration
st.set_page_config(page_title="Dashboard E-commerce", layout="wide")


product_returns = pd.read_csv('/workspaces/blank-app/data/product_return.csv')  # cleaned product return data
profit = pd.read_csv('/workspaces/blank-app/data/profit.csv') # cleaned profit data
coment = pd.read_csv('/workspaces/blank-app/data/coment.csv')  # cleaned low-score comments
delivery_delay = pd.read_csv('/workspaces/blank-app/data/delivery_delay.csv') # cleaned delivery delay data
avg_review_score_per_product = pd.read_csv('/workspaces/blank-app/data/agv_review_score_per_product.csv')  # cleaned review score data

# Dashboard Title
st.title("Dashboard E-commerce")

# Section 1: Product Returns Visualization
st.subheader("Produk dengan Pengembalian Terbanyak")

# Sort by return count descending
product_returns = product_returns.sort_values('return_count', ascending=False)

# Plot: Product Returns
fig, ax = plt.subplots(figsize=(12, 6))
sns.barplot(x=product_returns['product_category_name_english'], y=product_returns['return_count'], palette='Pastel1', ax=ax)
ax.set_title('Produk dengan Pengembalian Terbanyak', fontsize=16, fontweight='bold')
ax.set_xlabel('Kategori Produk', fontsize=12)
ax.set_ylabel('Jumlah Pengembalian', fontsize=12)
ax.set_xticklabels(ax.get_xticklabels(), rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)
st.pyplot(fig)

# Section 2: Top 10 Profitable Products
st.subheader("10 Produk dengan Profit Terbesar")

# Sort by profit margin descending and take top 10
top_profit_products = profit.sort_values('profit_margin', ascending=False).head(10)

# Plot: Profit Margin
fig, ax = plt.subplots(figsize=(16, 6))
sns.barplot(data=top_profit_products, x='product_category_name_english', y='profit_margin', palette='coolwarm', ax=ax)
ax.set_title('10 Produk dengan Profit Terbesar', fontsize=16, fontweight='bold')
ax.set_xlabel('Kategori Produk', fontsize=12)
ax.set_ylabel('Keuntungan', fontsize=12)
ax.set_xticklabels(ax.get_xticklabels(), rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)
st.pyplot(fig)

# Section 3: Low-Score Review Comments
st.subheader("Komentar untuk Produk dengan Skor Rendah")

# Display low-score comments as a table
st.table(coment)

# Section 4: Delivery Delay Visualization
st.subheader("Keterlambatan Pengiriman Berdasarkan Kategori Produk")

# Plot: Delivery Delay
fig, ax = plt.subplots(figsize=(12, 6))
sns.barplot(data=delivery_delay, x='product_category_name_english', y='delivery_delay', palette='mako', ax=ax)
ax.set_title('Rata-rata Keterlambatan Pengiriman Berdasarkan Kategori Produk', fontsize=16, fontweight='bold')
ax.set_xlabel('Kategori Produk', fontsize=12)
ax.set_ylabel('Keterlambatan (dalam hari)', fontsize=12)
ax.set_xticklabels(ax.get_xticklabels(), rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)
st.pyplot(fig)

# Section 5: Average Review Scores
st.subheader("Rata-rata Skor Review Berdasarkan Kategori Produk")

# Sort by average review score
average_review = avg_review_score_per_product.sort_values(by='average_review_score', ascending=False)

# Plot: Average Review Score
fig, ax = plt.subplots(figsize=(12, 6))
sns.barplot(data=average_review, x='average_review_score', y='product_category_name_english', palette='viridis', ax=ax)
ax.set_title('Rata-rata Skor Review Berdasarkan Kategori Produk', fontsize=16, fontweight='bold')
ax.set_xlabel('Rata-rata Skor Review', fontsize=12)
ax.set_ylabel('Kategori Produk', fontsize=12)
plt.grid(axis='x', linestyle='--', alpha=0.7)
st.pyplot(fig)

# Conclusion Section
st.subheader("Kesimpulan")
st.write("""
- Produk dengan tingkat pengembalian tertinggi berada pada kategori produk 'health and beauty'.
- 'Health and beauty' juga memberikan keuntungan yang cukup besar, meskipun memiliki tingkat pengembalian tinggi.
- Kategori produk dengan keterlambatan pengiriman terbesar adalah 'perfumery'.
- Rata-rata skor review untuk produk di kategori 'fashion_bags_accessories' sangat baik.
""")
