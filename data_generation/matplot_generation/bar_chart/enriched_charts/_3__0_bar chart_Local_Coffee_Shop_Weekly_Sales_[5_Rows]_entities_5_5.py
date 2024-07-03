
import matplotlib.pyplot as plt

# Generate data points
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
steps = [12000, 15000, 13000, 17000, 16000, 20000, 18000]

plt.figure(figsize=(10, 12))  # Change the width and height of the chart

# Create a vertical bar chart with specified bar width and colors
plt.bar(days, steps, color=[
    '#FF5733', '#33B8FF', '#8E33FF', '#FFC300', '#57C785', '#D733FF', '#FF8D33'], width=0.5)

plt.ylabel('Number of Steps', fontsize=14)
plt.title('Weekly Step Count', fontsize=16)
plt.ylim(0, 22000)  # Adjusted to give some space for readability

plt.tight_layout()
plt.show()