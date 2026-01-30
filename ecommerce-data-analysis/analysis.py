import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("data/ecommerce_sales.csv", encoding="ISO-8859-1")

# Inspect the data
print(df.head())
print(df.info())

# Data preparation
# Ensure InvoiceDate is datetime and Revenue exists
if not pd.api.types.is_datetime64_any_dtype(df["InvoiceDate"]):
    df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])
if "Revenue" not in df.columns:
    df["Revenue"] = df["Quantity"] * df["UnitPrice"]

# Question 1: Which product (Description) generated the highest total revenue?
revenue_by_product = (
    df.groupby("Description")["Revenue"]
    .sum()
    .sort_values(ascending=False)
)
print("Total Revenue by Product (Description):")
print(revenue_by_product)

# Question 2: What is the average order value per month?
df["Month"] = df["InvoiceDate"].dt.to_period("M")
average_order_value = (
    df.groupby("Month")["Revenue"]
    .mean()
)
print("\nAverage Order Value per Month:")
print(average_order_value)

# Question 3: Which month had the highest number of orders?
orders_per_month = df.groupby("Month")["InvoiceNo"].nunique()
highest_orders_month = orders_per_month.idxmax()
print("\nOrders per Month:")
print(orders_per_month)
print(f"\nMonth with highest number of orders: {highest_orders_month}")

# Draw a graph: Revenue by Product (Top 10)
revenue_by_product.head(10).plot(kind="bar")
plt.title("Top 10 Products by Total Revenue")
plt.xlabel("Product (Description)")
plt.ylabel("Revenue")
plt.tight_layout()
plt.show()
