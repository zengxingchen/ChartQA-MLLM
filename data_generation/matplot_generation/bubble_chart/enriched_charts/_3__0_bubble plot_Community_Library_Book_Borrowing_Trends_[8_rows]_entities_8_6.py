
import matplotlib.pyplot as plt

# Defining the data
genres = ['Action', 'Drama', 'Comedy', 'Romance', 'Sci-Fi', 'Fantasy', 
          'Horror', 'Documentary', 'Thriller', 'Mystery', 'Musical', 'Animation']
ratings = [85, 90, 70, 75, 80, 65, 55, 95, 60, 50, 45, 40]
viewership = [400, 350, 500, 450, 300, 250, 200, 100, 150, 120, 80, 60]
comments = [200, 220, 180, 150, 170, 130, 110, 90, 120, 100, 60, 50]

# Rescaling viewership for bubble size
size = [viewers * 2 for viewers in viewership]

# Create a bubble chart
fig, ax = plt.subplots(figsize=(12, 9))

for i in range(len(genres)):
    ax.scatter(ratings[i], viewership[i], s=size[i], alpha=0.6, color=f"#{i:02x}{i*2:02x}{255-i*2:02x}")

# Loop to annotate each bubble
for i, txt in enumerate(genres):
    ax.annotate(txt, (ratings[i], viewership[i]), ha='center', va='center')

# Set the chart's title and labels
ax.set_title('Popularity and Viewership of Movie Genres', fontsize=16)
ax.set_xlabel('Ratings (%)', fontsize=14)
ax.set_ylabel('Viewership (in thousands)', fontsize=14)

# Change the axes limits
ax.set_xlim(30, 100)
ax.set_ylim(50, 500)

# Tweak spacing to prevent clipping of tick-labels
plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)

plt.show()