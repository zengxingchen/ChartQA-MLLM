
import matplotlib.pyplot as plt
import seaborn as sns

# Data for pie chart
manufacturers = ['Samsung', 'Apple', 'Huawei', 'Xiaomi', 'OPPO', 'Vivo', 'Lenovo', 'LG', 'Others']
market_shares = [31.2, 22.7, 10.4, 9.1, 5.7, 5.3, 2.4, 1.8, 11.4]
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0','#ffb3e6', '#c4e17f', '#76d7c4', '#f7db70']

# Create a pie chart
plt.figure(figsize=(10, 8))
plt.pie(market_shares, labels=manufacturers, colors=colors, autopct='%1.1f%%', startangle=140)

# Draw a circle at the center for donut-style
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Equal aspect ratio ensures that pie is drawn as a circle.
plt.axis('equal')  

plt.title('Smartphone Market Share in 2023')

# Display the pie chart
plt.show()