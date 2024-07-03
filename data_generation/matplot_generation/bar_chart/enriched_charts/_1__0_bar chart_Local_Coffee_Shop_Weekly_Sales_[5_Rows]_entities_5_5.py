
import matplotlib.pyplot as plt

# Generate data points
categories = [
    "Savings", "Housing", "Utilities", "Food", "Transportation",
    "Healthcare", "Entertainment", "Education", "Miscellaneous"
]
percentages = [15.0, 25.0, 10.0, 20.0, 12.0, 8.0, 5.0, 3.0, 2.0]

plt.figure(figsize=(12, 10))  # Change the width and height of the chart

# Create a vertical bar chart with specified bar width and colors
plt.bar(categories, percentages, color=[
    '#4CAF50', '#FF5733', '#3375FF', '#FFC300', '#8E33FF',
    '#FF33AB', '#57C785', '#D733FF', '#ADD45C'], width=0.5)

plt.ylabel('Percentage of Monthly Expenses', fontsize=14)
plt.title('Distribution of Monthly Expenses', fontsize=16)
plt.ylim(0, 30)  # Adjusted to give some space for readability

plt.tight_layout()
plt.show()