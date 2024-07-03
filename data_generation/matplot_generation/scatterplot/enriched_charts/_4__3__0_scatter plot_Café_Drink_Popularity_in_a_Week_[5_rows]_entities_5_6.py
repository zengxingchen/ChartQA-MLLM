
import matplotlib.pyplot as plt

# Data
day = [
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
    11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
    21, 22, 23, 24, 25, 26, 27, 28, 29, 30
]
engagement_time = [
    25, 30, 35, 40, 28, 50, 45, 30, 20, 35,
    38, 32, 48, 27, 33, 29, 40, 25, 36, 34,
    50, 45, 35, 28, 40, 42, 30, 35, 50, 38
]
page_views = [
    150, 170, 180, 190, 160, 210, 200, 170, 140, 185,
    190, 175, 205, 155, 180, 165, 195, 150, 185, 180,
    210, 200, 185, 160, 195, 200, 175, 180, 210, 190
]
visitor_source = [
    '#FF5733', '#33FF57', '#3357FF', '#FF33A8', '#57FF33',
    '#FF8333', '#8333FF', '#33FF83', '#FF3385', '#3385FF',
    '#FF5733', '#33FF57', '#3357FF', '#FF33A8', '#57FF33',
    '#FF8333', '#8333FF', '#33FF83', '#FF3385', '#3385FF',
    '#FF5733', '#33FF57', '#3357FF', '#FF33A8', '#57FF33',
    '#FF8333', '#8333FF', '#33FF83', '#FF3385', '#3385FF'
]

# Scatter plot
fig, ax = plt.subplots(figsize=(14, 8))
sc = ax.scatter(day, engagement_time, s=[s + 10 for s in page_views], c=visitor_source, alpha=0.75)

# Customizing the axes and title
ax.set_xlabel('Day of the Month')
ax.set_ylabel('Engagement Time (mins)')
ax.set_title('Daily Engagement Time and Page Views from Different Visitor Sources')
ax.grid(True)

# Show plot
plt.show()