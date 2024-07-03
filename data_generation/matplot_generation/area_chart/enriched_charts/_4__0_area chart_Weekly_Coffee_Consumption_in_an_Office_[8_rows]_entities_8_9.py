
import matplotlib.pyplot as plt

# Generate data points
dates = list(range(1, 31))
page_views = [
    120, 132, 150, 165, 178, 195, 210, 230, 245, 260,
    275, 290, 310, 330, 350, 360, 370, 390, 410, 430,
    450, 470, 490, 500, 520, 540, 560, 580, 600, 620
]

# Create an area chart
plt.figure(figsize=(14, 7))
plt.fill_between(dates, page_views, color="#1E90FF")

# Customize axes and labels
plt.title("Monthly Website Traffic: Page Views", pad=20)
plt.xlabel("Date of the Month")
plt.ylabel("Page Views")
plt.xticks(range(1, 31, 2))
plt.yticks(range(100, 701, 50))

# Add annotation
plt.annotate('Highest traffic', xy=(30, 620), xytext=(20, 650),
             arrowprops=dict(facecolor='black', shrink=0.05))

# Display the plot
plt.show()