
import matplotlib.pyplot as plt

# Data
years = ['2015', '2016', '2017', '2018', '2019', '2020', '2021']
basketball = [10000, 12000, 14000, 16000, 18000, 20000, 22000]
football = [20000, 22000, 24000, 26000, 28000, 30000, 32000]
swimming = [15000, 18000, 21000, 24000, 27000, 30000, 33000]
tennis = [5000, 7000, 9000, 11000, 13000, 15000, 17000]

# Plot
fig, ax = plt.subplots(figsize=(12, 10))  # Change width and height of the chart

ax.bar(years, basketball, color='#1f77b4', edgecolor='white', width=0.6)
ax.bar(years, football, bottom=basketball, color='#2ca02c', edgecolor='white', width=0.6)
ax.bar(years, swimming, bottom=[i+j for i,j in zip(basketball, football)], color='#d62728', edgecolor='white', width=0.6)
ax.bar(years, tennis, bottom=[i+j+k for i,j,k in zip(basketball, football, swimming)], color='#ff7f0e', edgecolor='white', width=0.6)

ax.set_ylabel('Number of Participants')
ax.set_title('Sports Participation from 2015 to 2021')
ax.set_xticks(years)
ax.set_ylim(0, 100000)  # Adjust to accommodate the sum of the data points

plt.show()