
import matplotlib.pyplot as plt

# Data for plotting
genres = ["Rock", "Pop", "Hip-Hop", "Jazz", "Classical",
          "Country", "Electronic", "Reggae", "Blues", "Latin",
          "R&B", "K-Pop", "Folk", "Metal", "Gospel",
          "Disco", "Opera", "Punk", "Soul", "Funk",
          "Ambient", "New Age", "House", "Trance", "Ska", "Afrobeat"]
followers = [1200, 1500, 1100, 300, 200,
             500, 800, 400, 250, 600,
             1000, 900, 350, 450, 180,
             130, 100, 380, 420, 320,
             150, 220, 780, 640, 360, 270]  # in thousands
popularity = [90, 85, 95, 60, 40,
              70, 75, 65, 55, 80,
              88, 92, 50, 77, 35,
              45, 30, 72, 68, 62,
              38, 48, 82, 79, 66, 54]  # out of 100
influence = [8.9, 9.3, 9.5, 7.0, 6.5,
             7.8, 8.2, 7.3, 6.8, 8.0,
             8.7, 9.0, 6.7, 8.1, 6.3,
             6.4, 5.8, 7.6, 7.4, 7.2,
             6.0, 6.6, 8.4, 8.3, 7.5, 6.9]  # out of 10

# Convert Influence to a size for the plot, with an arbitrary scale factor
sizes = [i * 100 for i in influence]

# Create the Bubble Chart
plt.figure(figsize=(14, 10))
for i in range(len(genres)):
    plt.scatter(popularity[i], followers[i], s=sizes[i], alpha=0.6,
                c=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
                   '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf',
                   '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
                   '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf',
                   '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b'][i],
                edgecolors='w', linewidth=0.5)

plt.title('Genre Popularity vs Followers with Influence as Bubble Size', pad=20)
plt.xlabel('Popularity (out of 100)')
plt.ylabel('Followers (in thousands)')
plt.grid(True)

# Add genre labels to bubbles
for i, genre in enumerate(genres):
    plt.annotate(genre, (popularity[i], followers[i]), textcoords="offset points", 
                 xytext=(0, 10), ha='center', fontsize=8, color='#444444')

plt.show()