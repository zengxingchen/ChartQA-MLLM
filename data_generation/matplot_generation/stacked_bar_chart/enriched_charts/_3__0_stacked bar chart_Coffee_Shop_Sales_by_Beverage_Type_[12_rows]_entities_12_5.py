
import matplotlib.pyplot as plt

# Data
years = ['2015', '2016', '2017', '2018', '2019', '2020', '2021']
sci_fi = [22000, 25000, 28000, 31000, 35000, 38000, 42000]
fantasy = [32000, 34000, 37000, 40000, 42000, 45000, 48000]
mystery = [18000, 20000, 22000, 24000, 27000, 30000, 33000]
romance = [27000, 30000, 33000, 36000, 39000, 42000, 45000]

# Plot
fig, ax = plt.subplots(figsize=(12, 6))  # Change width and height of the chart

ax.bar(years, sci_fi, color='#4e79a7', edgecolor='white', width=0.6)
ax.bar(years, fantasy, bottom=sci_fi, color='#f28e2b', edgecolor='white', width=0.6)
ax.bar(years, mystery, bottom=[i+j for i,j in zip(sci_fi, fantasy)], color='#e15759', edgecolor='white', width=0.6)
ax.bar(years, romance, bottom=[i+j+k for i,j,k in zip(sci_fi, fantasy, mystery)], color='#76b7b2', edgecolor='white', width=0.6)

ax.set_ylabel('Number of Books Sold')
ax.set_title('Book Sales by Genre from 2015 to 2021', pad=20)
ax.set_xticks(years)
ax.set_ylim(0, 200000)  # Adjust to accommodate the sum of the data points

for i in range(len(years)):
    ax.text(i, sci_fi[i] / 2, sci_fi[i], ha='center', va='center', color='white', fontweight='bold')
    ax.text(i, sci_fi[i] + fantasy[i] / 2, fantasy[i], ha='center', va='center', color='white', fontweight='bold')
    ax.text(i, sci_fi[i] + fantasy[i] + mystery[i] / 2, mystery[i], ha='center', va='center', color='white', fontweight='bold')
    ax.text(i, sci_fi[i] + fantasy[i] + mystery[i] + romance[i] / 2, romance[i], ha='center', va='center', color='white', fontweight='bold')

plt.show()