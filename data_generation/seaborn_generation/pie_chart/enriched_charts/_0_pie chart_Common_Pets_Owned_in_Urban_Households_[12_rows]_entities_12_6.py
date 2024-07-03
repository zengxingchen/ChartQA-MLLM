
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Data
data = {"Brand": ["PlayStation", "Xbox", "Nintendo", "PC Gaming", "Mobile Gaming", "Others"],
        "MarketShare": [40, 30, 20, 5, 3, 2]}

# Create DataFrame
df = pd.DataFrame(data)

# Define colors
colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", "#8c564b"]

# Initialize the matplotlib figure
plt.figure(figsize=(8, 6))

# Create pie chart
plt.pie(df['MarketShare'], labels=df['Brand'], colors=colors, startangle=140, autopct='%1.1f%%')

# Set the title
plt.title('Gaming Console Market Share Distribution')

# Show the plot
plt.show()