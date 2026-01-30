import pandas as pd
import matplotlib.pyplot as plt

def load_data(filepath):
    """
    Loads the e-commerce sales dataset from a CSV file.
    Args:
        filepath (str): Path to the CSV file.
    Returns:
        pd.DataFrame: Loaded dataset as a pandas DataFrame.
    """
    df = pd.read_csv(filepath, encoding="ISO-8859-1")
    return df

def inspect_data(df):
    """
    Prints the first few rows and info about the DataFrame.
    Args:
        df (pd.DataFrame): The dataset to inspect.
    """
    print("\n--- Data Preview ---")
    print(df.head())
    print("\n--- Data Info ---")
    print(df.info())

def prepare_data(df):
    """
    Cleans and prepares the dataset for analysis.
    Ensures InvoiceDate is datetime and Revenue column exists.
    Args:
        df (pd.DataFrame): The dataset to prepare.
    Returns:
        pd.DataFrame: Prepared dataset.
    """
    if not pd.api.types.is_datetime64_any_dtype(df["InvoiceDate"]):
        df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])
    if "Revenue" not in df.columns:
        df["Revenue"] = df["Quantity"] * df["UnitPrice"]
    return df

def revenue_by_product(df):
    """
    Calculates total revenue by product (Description).
    Args:
        df (pd.DataFrame): The dataset.
    Returns:
        pd.Series: Revenue summed by product, sorted descending.
    """
    revenue = (
        df.groupby("Description")["Revenue"]
        .sum()
        .sort_values(ascending=False)
    )
    return revenue

def average_order_value_per_month(df):
    """
    Calculates the average order value per month.
    Args:
        df (pd.DataFrame): The dataset.
    Returns:
        pd.Series: Average order value per month.
    """
    df["Month"] = df["InvoiceDate"].dt.to_period("M")
    avg_value = (
        df.groupby("Month")["Revenue"]
        .mean()
    )
    return avg_value

def orders_per_month(df):
    """
    Calculates the number of unique orders per month.
    Args:
        df (pd.DataFrame): The dataset.
    Returns:
        pd.Series: Number of orders per month.
        str: Month with the highest number of orders.
    """
    orders = df.groupby("Month")["InvoiceNo"].nunique()
    highest_month = orders.idxmax()
    return orders, highest_month

def plot_top_products(revenue_series, top_n=10):
    """
    Plots a bar chart of the top N products by total revenue.
    Args:
        revenue_series (pd.Series): Revenue by product.
        top_n (int): Number of top products to plot.
    """
    revenue_series.head(top_n).plot(kind="bar")
    plt.title(f"Top {top_n} Products by Total Revenue")
    plt.xlabel("Product (Description)")
    plt.ylabel("Revenue")
    plt.tight_layout()
    plt.show()

def main():
    """
    Main function to run the e-commerce data analysis workflow.
    Loads, inspects, prepares data, performs analysis, and visualizes results.
    """
    # Load data
    df = load_data("data/ecommerce_sales.csv")

    # Inspect data
    inspect_data(df)

    # Prepare data
    df = prepare_data(df)

    # Question 1: Revenue by product
    revenue = revenue_by_product(df)
    print("\nTotal Revenue by Product (Description):")
    print(revenue)

    # Question 2: Average order value per month
    avg_order_value = average_order_value_per_month(df)
    print("\nAverage Order Value per Month:")
    print(avg_order_value)

    # Question 3: Orders per month
    orders, highest_month = orders_per_month(df)
    print("\nOrders per Month:")
    print(orders)
    print(f"\nMonth with highest number of orders: {highest_month}")

    # Visualization
    plot_top_products(revenue, top_n=10)

# Entry point for script execution
if __name__ == "__main__":
    main()

# Extra: Example of additional analysis functions for more lines and learning
def revenue_by_country(df):
    """
    Calculates total revenue by country.
    Args:
        df (pd.DataFrame): The dataset.
    Returns:
        pd.Series: Revenue summed by country, sorted descending.
    """
    revenue = (
        df.groupby("Country")["Revenue"]
        .sum()
        .sort_values(ascending=False)
    )
    return revenue

def plot_revenue_by_country(df):
    """
    Plots a bar chart of total revenue by country (top 10).
    Args:
        df (pd.DataFrame): The dataset.
    """
    revenue = revenue_by_country(df)
    revenue.head(10).plot(kind="bar")
    plt.title("Top 10 Countries by Total Revenue")
    plt.xlabel("Country")
    plt.ylabel("Revenue")
    plt.tight_layout()
    plt.show()
