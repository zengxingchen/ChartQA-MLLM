
import matplotlib.pyplot as plt

# Data
years = range(2010, 2021)
beauty_salon_visits = [2000, 2200, 2600, 3000, 3500, 4000, 4800, 5800, 7000, 8500, 10000]

# Plot
fig, ax = plt.subplots(figsize=(14, 10))  # changing width and height

# Plotting the area chart
ax.fill_between(years, beauty_salon_visits, color="#8A2BE2", alpha=0.7, label='Beauty Salon Visits')

# Titles and labels
ax.set_title('Annual Beauty Salon Visits from 2010 to 2020', fontsize=18, pad=20)
ax.set_xlabel('Year', fontsize=15)
ax.set_ylabel('Number of Visits', fontsize=15)

# Customizing the y-axis to get a better understanding of scales
ax.set_yscale('linear')

# Annotation
for i, txt in enumerate(beauty_salon_visits):
    ax.annotate(txt, (years[i], beauty_salon_visits[i]), textcoords="offset points", xytext=(0,5), ha='center')

# Legend
ax.legend(loc='upper right')

plt.show()