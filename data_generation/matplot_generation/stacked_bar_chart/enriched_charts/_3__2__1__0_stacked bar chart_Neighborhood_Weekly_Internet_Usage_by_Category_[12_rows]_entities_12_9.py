
import matplotlib.pyplot as plt

# Data from the table provided
years = ['2015', '2016', '2017', '2018', '2019', '2020', '2021']
action = [45, 50, 55, 60, 65, 70, 75]
comedy = [60, 65, 70, 75, 80, 85, 90]
drama = [75, 80, 85, 90, 95, 100, 105]
science_fiction = [55, 60, 65, 70, 75, 80, 85]

# Stacking data
comedy_bottom = [action[i] for i in range(len(action))]
drama_bottom = [comedy_bottom[i] + comedy[i] for i in range(len(comedy))]
science_fiction_bottom = [drama_bottom[i] + drama[i] for i in range(len(drama))]

# Setting figure size
plt.figure(figsize=(12, 8))

# Plotting data
bar_width = 0.6
plt.bar(years, action, width=bar_width, color='#FF5733', edgecolor='white', label='Action')
plt.bar(years, comedy, bottom=comedy_bottom, width=bar_width, color='#33FF57', edgecolor='white', label='Comedy')
plt.bar(years, drama, bottom=drama_bottom, width=bar_width, color='#3357FF', edgecolor='white', label='Drama')
plt.bar(years, science_fiction, bottom=science_fiction_bottom, width=bar_width, color='#FF33A1', edgecolor='white', label='Science Fiction')

# Adding titles and labels
plt.ylabel('Viewership in Millions')
plt.xlabel('Year')
plt.title('Annual Viewership by Genre (2015-2021)')
plt.legend(loc='upper left')

# Adding numerical labels
for i in range(len(years)):
    plt.text(i, action[i] / 2, str(action[i]), ha='center', va='center', color='black')
    plt.text(i, comedy_bottom[i] + comedy[i] / 2, str(comedy[i]), ha='center', va='center', color='black')
    plt.text(i, drama_bottom[i] + drama[i] / 2, str(drama[i]), ha='center', va='center', color='black')
    plt.text(i, science_fiction_bottom[i] + science_fiction[i] / 2, str(science_fiction[i]), ha='center', va='center', color='black')

# Display the plot
plt.show()