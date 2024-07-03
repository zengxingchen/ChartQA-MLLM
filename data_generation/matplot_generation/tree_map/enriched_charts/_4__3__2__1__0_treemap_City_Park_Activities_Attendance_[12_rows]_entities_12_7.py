
import matplotlib.pyplot as plt
import squarify

companies = ['Apple', 'Microsoft', 'Amazon', 'Google', 'Facebook', 'Alibaba', 'Tencent', 'Samsung', 'Intel', 'Cisco', 'IBM', 'Sony', 
             'Oracle', 'Salesforce', 'Adobe', 'Nvidia', 'Netflix', 'PayPal', 'SAP', 'Zoom', 'Shopify', 'Uber', 'Spotify', 'Twitter', 'Airbnb']
revenue = [260, 125, 280, 160, 85, 70, 55, 200, 72, 51, 57, 77, 40, 17, 11, 11, 20, 17, 31, 1.3, 2, 11, 8, 3, 3.4]
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf', 
          '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf', 
          '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

plt.figure(figsize=(20, 16))
squarify.plot(sizes=revenue, label=companies, color=colors, alpha=0.8)
plt.title('Top Tech Companies by Revenue (in billion USD)', fontsize=24, pad=35)
plt.axis('off')
plt.show()