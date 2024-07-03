
import matplotlib.pyplot as plt
import squarify

# Data points
companies = [
    'Apple', 'Samsung', 'Amazon', 'Google', 'Microsoft', 'Huawei', 'Sony', 'Intel',
    'Facebook', 'Tesla', 'Alibaba', 'Netflix', 'NVIDIA', 'IBM', 'Oracle', 'Cisco',
    'Xiaomi', 'Adobe', 'Salesforce', 'PayPal', 'Spotify', 'Shopify', 'Uber', 'Twitter',
    'Snap', 'Zillow', 'Slack', 'Square', 'Airbnb', 'Zoom'
]
revenues = [
    274500, 200700, 386100, 181690, 143015, 129000, 84940, 77870,
    85965, 31536, 109480, 24996, 10819, 73500, 39210, 49150,
    37640, 12682, 21082, 21454, 7443, 2929, 11439, 3680,
    2570, 3340, 902, 9700, 3375, 6223
]
colors = [
    '#FF5733', '#33FF57', '#3357FF', '#FF33A5', '#33FFA5', '#FF33F6', '#A533FF', '#F6FF33',
    '#33FFD1', '#FF8F33', '#8FFF33', '#FF3333', '#33D1FF', '#FF33C8', '#D1FF33', '#33FFC8',
    '#FFC833', '#C8FF33', '#33FFB4', '#FF5733', '#5733FF', '#33FF57', '#33B4FF', '#FF333F',
    '#33FFD8', '#D833FF', '#FF33B4', '#33FF5B', '#FF5733', '#33FF57'
]

# Plot Dimensions
plt.figure(figsize=(16, 12))

# Create a treemap
squarify.plot(sizes=revenues, label=companies, color=colors, alpha=0.8)

# Title
plt.title('Annual Revenue of Major Tech Companies (in Millions USD)', fontsize=18, y=1.05)

# Remove axes
plt.axis('off')

# Show plot
plt.show()