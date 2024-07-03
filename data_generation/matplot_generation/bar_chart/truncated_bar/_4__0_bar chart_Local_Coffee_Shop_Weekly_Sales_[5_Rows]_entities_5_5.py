
import matplotlib.pyplot as plt

# Generate data points
months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]
tourist_arrivals = [450, 470, 550, 650, 800, 950, 1200, 1100, 900, 700, 600, 500]

plt.figure(figsize=(10, 12))  # Adjusted the width and height of the chart

# Create a vertical bar chart with specified bar width and colors
plt.bar(months, tourist_arrivals, color=[
    '#FF5733', '#FF8D33', '#FFC300', '#EDDD53', '#ADD45C',
    '#57C785', '#33B8FF', '#3375FF', '#8E33FF', '#D733FF',
    '#FF33AB', '#FF3366'], width=0.5)

plt.ylabel('Tourist Arrivals (Thousands)', fontsize=14)
plt.title('Average Monthly Tourist Arrivals in a City', fontsize=16)
plt.ylim(400, 1300)  # Adjusted to start from 400 to give some space for readability

plt.tight_layout()
plt.show()