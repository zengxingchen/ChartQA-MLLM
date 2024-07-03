
import matplotlib.pyplot as plt

# Data for the new chart
years = ['2015','2016','2017','2018','2019','2020','2021']
action = [12, 15, 17, 19, 22, 24, 27]
comedy = [18, 20, 22, 25, 28, 30, 33]
drama = [25, 30, 35, 40, 45, 50, 55]
fantasy = [8, 10, 12, 14, 16, 18, 20]

# Stacking data
comedy_bottom = [action[i] for i in range(len(action))]
drama_bottom = [comedy_bottom[i] + comedy[i] for i in range(len(comedy))]
fantasy_bottom = [drama_bottom[i] + drama[i] for i in range(len(drama))]

# Setting figure size
plt.figure(figsize=(10, 12))

# Plotting data
bar_width = 0.4
plt.bar(years, action, width=bar_width, color='#ff5733', edgecolor='white', label='Action')
plt.bar(years, comedy, bottom=action, width=bar_width, color='#33ff57', edgecolor='white', label='Comedy')
plt.bar(years, drama, bottom=comedy_bottom, width=bar_width, color='#3357ff', edgecolor='white', label='Drama')
plt.bar(years, fantasy, bottom=drama_bottom, width=bar_width, color='#ff33a8', edgecolor='white', label='Fantasy')

# Adding titles and labels
plt.ylabel('Number of Movies')
plt.xlabel('Year')
plt.title('Movie Genre Distribution over Years')
plt.legend(loc='upper left')

# Adding numerical labels
for i in range(len(years)):
    plt.text(i, action[i] / 2, str(action[i]), ha='center', va='center', color='white')
    plt.text(i, comedy_bottom[i] + comedy[i] / 2, str(comedy[i]), ha='center', va='center', color='white')
    plt.text(i, drama_bottom[i] + drama[i] / 2, str(drama[i]), ha='center', va='center', color='white')
    plt.text(i, fantasy_bottom[i] + fantasy[i] / 2, str(fantasy[i]), ha='center', va='center', color='white')

# Display the plot
plt.show()