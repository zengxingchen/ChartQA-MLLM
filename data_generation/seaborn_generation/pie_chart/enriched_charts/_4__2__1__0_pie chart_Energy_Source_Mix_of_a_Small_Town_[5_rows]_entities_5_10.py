
import matplotlib.pyplot as plt

labels = ['Stocks', 'Bonds', 'Real Estate', 'Mutual Funds', 'Commodities', 'Cryptocurrency']
sizes = [350, 200, 150, 100, 75, 125]
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']

plt.figure(figsize=(14,10))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)

plt.title('Investment Portfolio Distribution', pad=20)
plt.axis('equal')  
plt.show()