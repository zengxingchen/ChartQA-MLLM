
import matplotlib.pyplot as plt

# Data from the table provided
years = ['2015','2016','2017','2018','2019','2020','2021']
kids = [23, 25, 18, 15, 20, 10, 8]
teens = [45, 50, 55, 60, 65, 70, 75]
adults = [82, 90, 88, 95, 100, 105, 110]
seniors = [30, 35, 38, 40, 45, 50, 55]

# Stacking data
teens_bottom = [kids[i] for i in range(len(kids))]
adults_bottom = [teens_bottom[i] + teens[i] for i in range(len(teens))]
seniors_bottom = [adults_bottom[i] + adults[i] for i in range(len(adults))]

# Setting figure size
plt.figure(figsize=(14, 8))

# Plotting data
bar_width = 0.6
plt.barh(years, kids, height=bar_width, color='#3498db', edgecolor='white', label='Kids')
plt.barh(years, teens, left=kids, height=bar_width, color='#2ecc71', edgecolor='white', label='Teens')
plt.barh(years, adults, left=teens_bottom, height=bar_width, color='#e74c3c', edgecolor='white', label='Adults')
plt.barh(years, seniors, left=adults_bottom, height=bar_width, color='#f1c40f', edgecolor='white', label='Seniors')

# Adding titles and labels
plt.xlabel('Number of People')
plt.ylabel('Year')
plt.title('Population Distribution by Age Group over Years')
plt.legend()

# Display the plot
plt.show()