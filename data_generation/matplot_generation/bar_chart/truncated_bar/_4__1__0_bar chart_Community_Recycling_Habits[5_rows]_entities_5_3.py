
import matplotlib.pyplot as plt

# Data
industries = ['Technology', 'Finance', 'Healthcare', 'Retail', 'Energy', 'Automotive', 'Construction', 'Telecommunications', 'Food & Beverages', 'Entertainment']
revenue = [850, 780, 650, 500, 460, 420, 380, 350, 330, 310]
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']

# Figure size
plt.figure(figsize=(10, 8))

# Horizontal bar chart
plt.barh(industries, revenue, color=colors, height=0.5)

# Labeling
plt.xlabel('Revenue (in billions)')
plt.title('Top 10 Industries by Revenue')

# Setting y-axis limits
plt.xlim(300, 900)

# Show and save plot
plt.tight_layout()
plt.show()