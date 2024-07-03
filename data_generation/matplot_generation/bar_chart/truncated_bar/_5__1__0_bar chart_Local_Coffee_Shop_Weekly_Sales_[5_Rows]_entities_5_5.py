
import matplotlib.pyplot as plt

# Generate data points
categories = [
    "Savings", "Housing", "Utilities", "Food", "Transportation",
    "Healthcare", "Entertainment", "Education", "Miscellaneous",
    "Investment", "Insurance", "Taxes"
]
percentages = [15.0, 25.0, 10.0, 20.0, 12.0, 8.0, 5.0, 3.0, 2.0, 18.0, 7.0, 22.0]

plt.figure(figsize=(14, 8))  # Change the width and height of the chart

# Create a horizontal bar chart with specified bar height and colors
plt.barh(categories, percentages, color=[
    '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
    '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf',
    '#9edae5', '#f7b6d2'], height=0.6)

plt.xlabel('Percentage of Monthly Expenses', fontsize=14)
plt.title('Distribution of Monthly Expenses in Economics & Finance', fontsize=16)
plt.xlim(5, 30)  # Adjusted to give some space for readability

plt.tight_layout()
plt.show()