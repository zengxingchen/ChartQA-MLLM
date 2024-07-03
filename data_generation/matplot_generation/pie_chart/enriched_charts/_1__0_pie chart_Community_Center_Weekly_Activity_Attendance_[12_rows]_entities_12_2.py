
import matplotlib.pyplot as plt

# Data setup
disorders = ['Anxiety', 'Depression', 'Bipolar', 'Schizophrenia', 'OCD', 'PTSD', 'Eating Disorders']
percentages = [30, 25, 15, 10, 8, 7, 5]
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0','#ffb3e6','#c4e17f']

# Plotting
fig, ax = plt.subplots(figsize=(12, 7))  # width and height of the chart
ax.pie(percentages, labels=disorders, autopct='%1.1f%%', colors=colors, startangle=140)
ax.set_title('Proportion of Mental Health Disorders by Type', pad=20)

# Show plot
plt.show()