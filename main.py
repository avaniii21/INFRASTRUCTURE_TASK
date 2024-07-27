import pandas as pd

def load_data(filepath):
    """Load data from a CSV file."""
    return pd.read_csv(filepath)

def calculate_total_revenue(data):
    """Calculate total revenue per order."""
    data['total_revenue'] = data['product_price'] * data['quantity']
    return data

def compute_monthly_revenue(data):
    """Compute total revenue by month."""
    data['order_date'] = pd.to_datetime(data['order_date'])
    data['month'] = data['order_date'].dt.to_period('M')
    monthly_revenue = data.groupby('month')['total_revenue'].sum()
    return monthly_revenue

def compute_product_revenue(data):
    """Compute total revenue by product."""
    product_revenue = data.groupby('product_name')['total_revenue'].sum()
    return product_revenue

def compute_customer_revenue(data):
    """Compute total revenue by customer."""
    customer_revenue = data.groupby('customer_id')['total_revenue'].sum()
    return customer_revenue

def top_10_customers(data):
    """Identify the top 10 customers by revenue."""
    customer_revenue = compute_customer_revenue(data)
    return customer_revenue.sort_values(ascending=False).head(10)

# Example usage
if __name__ == '__main__':
    file_path = 'orders_1500.csv'  # Adjust path as needed
    data = load_data(file_path)
    data = calculate_total_revenue(data)
    print("Monthly Revenue:\n", compute_monthly_revenue(data))
    print("\nProduct Revenue:\n", compute_product_revenue(data))
    print("\nCustomer Revenue:\n", compute_customer_revenue(data))
    print("\nTop 10 Customers:\n", top_10_customers(data))


