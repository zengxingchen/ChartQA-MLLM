
import matplotlib.pyplot as plt

# Data
years = ['2015', '2016', '2017', '2018', '2019', '2020', '2021']
math = [11000, 13000, 14000, 15000, 16000, 17000, 18000]
science = [15000, 16000, 18000, 19000, 20000, 22000, 23000]
english = [10000, 11000, 12000, 13000, 14000, 15000, 16000]
history = [5000, 7000, 9000, 11000, 13000, 15000, 17000]

# Plot
fig, ax = plt.subplots(figsize=(14, 8))  # Change width and height of the chart

# Horizontal bar chart
ax.barh(years, math, color='#1e90ff', edgecolor='white', height=0.6)
ax.barh(years, science, left=math, color='#ff6347', edgecolor='white', height=0.6)
ax.barh(years, english, left=[i+j for i,j in zip(math, science)], color='#32cd32', edgecolor='white', height=0.6)
ax.barh(years, history, left=[i+j+k for i,j,k in zip(math, science, english)], color='#ff69b4', edgecolor='white', height=0.6)

# Adding numerical labels
for i in range(len(years)):
    ax.text(math[i]/2, i, str(math[i]), va='center', ha='center', color='white', fontweight='bold')
    ax.text(math[i] + science[i]/2, i, str(science[i]), va='center', ha='center', color='white', fontweight='bold')
    ax.text(math[i] + science[i] + english[i]/2, i, str(english[i]), va='center', ha='center', color='white', fontweight='bold')
    ax.text(math[i] + science[i] + english[i] + history[i]/2, i, str(history[i]), va='center', ha='center', color='white', fontweight='bold')

ax.set_xlabel('Number of Students')
ax.set_title('Subject Enrollment from 2015 to 2021')
ax.set_yticks(years)
ax.set_xlim(0, 80000)  # Adjust to accommodate the sum of the data points

plt.show()