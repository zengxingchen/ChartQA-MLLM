
import matplotlib.pyplot as plt

# Data
categories = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
documentaries = [300, 280, 270, 260, 250, 240]
movies = [250, 240, 230, 220, 210, 200]
tv_shows = [180, 190, 200, 210, 220, 230]
mini_series = [140, 150, 160, 170, 180, 190]
specials = [120, 130, 140, 150, 160, 170]

# Cumulative values for stacking
cumulative_a = documentaries
cumulative_b = [a + b for a, b in zip(cumulative_a, movies)]
cumulative_c = [b + c for b, c in zip(cumulative_b, tv_shows)]
cumulative_d = [c + d for c, d in zip(cumulative_c, mini_series)]
cumulative_e = [d + e for d, e in zip(cumulative_d, specials)]

# Figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Stacked bar chart
ax.bar(categories, documentaries, color='#4c72b0', edgecolor='white', width=0.5, label='Documentaries')
ax.bar(categories, movies, bottom=cumulative_a, color='#55a868', edgecolor='white', width=0.5, label='Movies')
ax.bar(categories, tv_shows, bottom=cumulative_b, color='#c44e52', edgecolor='white', width=0.5, label='TV Shows')
ax.bar(categories, mini_series, bottom=cumulative_c, color='#8172b2', edgecolor='white', width=0.5, label='Mini-Series')
ax.bar(categories, specials, bottom=cumulative_d, color='#ccb974', edgecolor='white', width=0.5, label='Specials')

# Adding labels and a title, and a legend
ax.set_ylabel('Number of Viewers (in thousands)')
ax.set_title('Monthly Viewership by Content Type', pad=20)
ax.legend(loc='upper left', bbox_to_anchor=(1, 1))

# Adding numerical labels
for i in range(len(categories)):
    plt.text(i, cumulative_a[i] / 2, str(documentaries[i]), ha='center', va='center', color='white')
    plt.text(i, cumulative_a[i] + (movies[i] / 2), str(movies[i]), ha='center', va='center', color='white')
    plt.text(i, cumulative_b[i] + (tv_shows[i] / 2), str(tv_shows[i]), ha='center', va='center', color='white')
    plt.text(i, cumulative_c[i] + (mini_series[i] / 2), str(mini_series[i]), ha='center', va='center', color='white')
    plt.text(i, cumulative_d[i] + (specials[i] / 2), str(specials[i]), ha='center', va='center', color='white')

# Adjusting layout for better fit and visuals
plt.tight_layout()

# Show the plot
plt.show()