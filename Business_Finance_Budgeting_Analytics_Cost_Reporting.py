# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# Define date range and categories
dates = pd.date_range(start="2024-01-01", end="2024-12-31", freq="MS")
businesses = ["Retail", "Corporate", "Support"]
products = ["Personal Loan", "Credit Card", "Business Loan", "Home Loan"]
cost_categories = ["Direct Cost", "Indirect Cost", "Fixed Cost", "Variable Cost"]
support_functions = ["HR", "IT", "Operations"]

# Generate Cost Data
cost_data = pd.DataFrame({
    "Date": np.random.choice(dates, 200),
    "Business": np.random.choice(businesses, 200),
    "Product": np.random.choice(products, 200),
    "Cost Category": np.random.choice(cost_categories, 200),
    "Amount (USD)": np.random.randint(1000, 100000, 200),
})

# Generate Budget vs Actual Data
budget_actual_data = pd.DataFrame({
    "Date": dates,
    "Business": np.random.choice(businesses, len(dates)),
    "Budgeted Cost (USD)": np.random.randint(50000, 150000, len(dates)),
    "Actual Cost (USD)": np.random.randint(50000, 150000, len(dates)),
})

# Generate Profitability Data
profitability_data = pd.DataFrame({
    "Date": dates,
    "Product": np.random.choice(products, len(dates)),
    "Income (USD)": np.random.randint(100000, 500000, len(dates)),
    "Support Cost (USD)": np.random.randint(20000, 100000, len(dates)),
    "Profitability (USD)": np.random.randint(50000, 400000, len(dates)),
})

# Save as CSV for use in BI tools
cost_data.to_csv("cost_data.csv", index=False)
budget_actual_data.to_csv("budget_actual_data.csv", index=False)
profitability_data.to_csv("profitability_data.csv", index=False)

# Business-wise Cost Report
business_cost_report = cost_data.groupby(["Business", "Cost Category"]).sum().reset_index()
print(business_cost_report)

# Calculate MoM Variances
budget_actual_data["Variance (USD)"] = budget_actual_data["Actual Cost (USD)"] - budget_actual_data["Budgeted Cost (USD)"]
budget_actual_data["MoM Change (%)"] = budget_actual_data["Actual Cost (USD)"].pct_change() * 100
print(budget_actual_data)

# Combine Profitability with Support Cost Allocation
profitability_data["Net Profit (USD)"] = profitability_data["Income (USD)"] - profitability_data["Support Cost (USD)"]
print(profitability_data)

# Automating Support Cost Allocation by Proportion of Income
total_income = profitability_data["Income (USD)"].sum()
profitability_data["Allocated Support Cost"] = profitability_data["Income (USD)"] / total_income * 1000000  # Example pool size
print(profitability_data)



# Cost Trend Visualization
plt.figure(figsize=(10, 6))
sns.lineplot(data=budget_actual_data, x="Date", y="Actual Cost (USD)", label="Actual Cost")
sns.lineplot(data=budget_actual_data, x="Date", y="Budgeted Cost (USD)", label="Budgeted Cost")
plt.title("Monthly Cost Trends")
plt.xlabel("Date")
plt.ylabel("Cost (USD)")
plt.legend()
plt.show()
