
import matplotlib.pyplot as plt

# Data
companies = ['Amazon', 'Apple', 'Google', 'Microsoft', 'Facebook', 'Alibaba', 'Tencent', 'Samsung', 'Intel', 'IBM', 'Sony', 'NVIDIA', 'Tesla', 'Oracle', 'Salesforce']
revenue = [469822, 274515, 181699, 168088, 85965, 109480, 73769, 200734, 77867, 73623, 84978, 16675, 31536, 40947, 21380]
colors = ['#1f78b4', '#ff7e0e', '#2ca03c', '#d62718', '#9466bd', '#8c563b', '#e377c1', '#7f7f6f', '#bcb923', '#17becf', '#bc55a2', '#ff6347', '#4682b4', '#daa520', '#cd5c5c']

# Figure size
plt.figure(figsize=(12, 6))

# Vertical bar chart
plt.bar(companies, revenue, color=colors, width=0.4)

# Labeling
plt.ylabel('Revenue in Millions')
plt.title('Annual Revenue of Leading Tech Companies')

# Rotate x-axis labels for better readability
plt.xticks(rotation=45, ha='right')

# Show and save plot
plt.tight_layout()
plt.show()