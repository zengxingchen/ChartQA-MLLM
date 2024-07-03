
import matplotlib.pyplot as plt

# Data
years = ['2015', '2016', '2017', '2018', '2019', '2020', '2021']
electric = [12000, 15000, 20000, 25000, 32000, 40000, 48000]
hybrid = [35000, 40000, 45000, 50000, 55000, 60000, 63000]
diesel = [80000, 78000, 75000, 72000, 68000, 64000, 59000]
petrol = [60000, 58000, 55000, 51000, 47000, 43000, 39000]

# Plot
fig, ax = plt.subplots(figsize=(10, 8))  # Change width and height of the chart

ax.barh(years, electric, color='#1f77b4', edgecolor='white', height=0.8)
ax.barh(years, hybrid, left=electric, color='#2ca02c', edgecolor='white', height=0.8)
ax.barh(years, diesel, left=[i+j for i,j in zip(electric, hybrid)], color='#d62728', edgecolor='white', height=0.8)
ax.barh(years, petrol, left=[i+j+k for i,j,k in zip(electric, hybrid, diesel)], color='#ff7f0e', edgecolor='white', height=0.8)

ax.set_xlabel('Number of Cars')
ax.set_title('Car Sales by Type from 2015 to 2021')
ax.set_yticks(years)
ax.set_xlim(0, 250000)  # Adjust to accommodate the sum of the data points

plt.show()