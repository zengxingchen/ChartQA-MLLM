
import matplotlib.pyplot as plt

# Data to plot
labels = 'Online Advertising', 'Content Marketing', 'SEO', 'Social Media', 'Email Marketing'
sizes = [35.0, 25.0, 15.0, 15.0, 10.0]
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0']

# Create pie chart
plt.figure(figsize=(10, 8))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)

plt.title('Digital Marketing Spend Distribution in 2023', pad=20)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()