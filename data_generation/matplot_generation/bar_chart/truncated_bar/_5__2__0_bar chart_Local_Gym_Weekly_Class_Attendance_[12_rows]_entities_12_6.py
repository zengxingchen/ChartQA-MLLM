
import matplotlib.pyplot as plt

# Data
country = ['China', 'India', 'United States', 'Indonesia', 'Brazil',
           'Nigeria', 'Japan', 'Russia', 'Bangladesh', 'Mexico',
           'Philippines', 'Vietnam', 'Germany', 'Turkey', 'United Kingdom',
           'France', 'Thailand', 'South Africa', 'Italy', 'Egypt']
internet_users = [1042, 624, 312, 171, 160, 154, 118, 118, 100, 95,
                  85, 72, 67, 66, 65, 58, 52, 48, 46, 45]

# Create horizontal bar chart
plt.figure(figsize=(14, 10))
colors = ['#4daf4a', '#377eb8', '#ff7f00', '#984ea3', '#e41a1c',
          '#ffff33', '#a65628', '#f781bf', '#999999', '#66c2a5',
          '#fc8d62', '#8da0cb', '#e78ac3', '#a6d854', '#ffd92f',
          '#e5c494', '#b3b3b3', '#fb8072', '#80b1d3', '#fdb462']

plt.barh(country, internet_users, color=colors, height=0.6)

# Customizing the plot
plt.xlabel('Internet Users in Millions')
plt.title('Internet Users by Country (2023)')
plt.xlim(40, 1100)  # Truncated y-axis

plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()