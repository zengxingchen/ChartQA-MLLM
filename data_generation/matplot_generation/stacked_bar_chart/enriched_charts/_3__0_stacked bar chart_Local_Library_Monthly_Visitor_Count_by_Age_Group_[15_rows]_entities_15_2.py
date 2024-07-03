
import matplotlib.pyplot as plt

# Data
months = ['January', 'February', 'March', 'April', 'May', 'June']
website_a = [200, 180, 190, 210, 220, 230]
website_b = [150, 160, 170, 180, 190, 200]
website_c = [120, 140, 160, 170, 180, 190]

# Color codes for each website
colors = ['#FF6347', '#4682B4', '#32CD32']

# Plot stacked vertical bar chart
plt.figure(figsize=(12, 6))  # Width and height of the chart in inches
bar_width = 0.6  # Width of the bars

plt.bar(months, website_a, color=colors[0], edgecolor='white', width=bar_width, label='Website A')
plt.bar(months, website_b, bottom=website_a, color=colors[1], edgecolor='white', width=bar_width, label='Website B')
plt.bar(months, website_c, bottom=[i + j for i, j in zip(website_a, website_b)], color=colors[2], edgecolor='white', width=bar_width, label='Website C')

# Add labels, title, and legend
plt.ylabel('Unique Visitors')
plt.xlabel('Month')
plt.title('Monthly Unique Visitors for Websites A, B, and C')
plt.legend()

# Add numerical labels
for i, month in enumerate(months):
    plt.text(i, website_a[i] / 2, str(website_a[i]), ha='center', va='center', color='white', fontweight='bold')
    plt.text(i, website_a[i] + website_b[i] / 2, str(website_b[i]), ha='center', va='center', color='white', fontweight='bold')
    plt.text(i, website_a[i] + website_b[i] + website_c[i] / 2, str(website_c[i]), ha='center', va='center', color='white', fontweight='bold')

# Display the final result
plt.show()