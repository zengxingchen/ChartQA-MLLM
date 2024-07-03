
import matplotlib.pyplot as plt

# Data to plot
labels = ['Rock', 'Pop', 'Jazz', 'Classical', 'Hip-Hop', 'Country', 'Electronic', 'Blues', 'Reggae', 'Folk']
sizes = [22, 19, 14, 13, 11, 8, 7, 3, 2, 1]
colors = ['#1F77B4', '#FF7F0E', '#2CA02C', '#D62728', '#9467BD', '#8C564B', '#E377C2', '#7F7F7F', '#BCBD22', '#17BECF']

# Plot
fig1, ax1 = plt.subplots(figsize=(12, 8))
ax1.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)

# Draw circle for donut chart
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Equal aspect ratio ensures that pie is drawn as a circle
ax1.axis('equal')

plt.title('Popularity of Music Genres', pad=20)
plt.show()