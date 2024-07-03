
import matplotlib.pyplot as plt

# Data
genres = ["Rock", "Pop", "Jazz", "Classical", "Hip-Hop", "Country", "Electronic", "Reggae", "Blues", "Folk", "Metal", 
          "R&B", "Latin", "Indie", "K-Pop", "Disco", "Soul", "Funk", "Techno", "Gospel"]
popularity = [85, 90, 75, 65, 95, 70, 80, 60, 68, 72, 78, 88, 77, 83, 92, 64, 84, 82, 79, 63]

# Create vertical bar chart
plt.figure(figsize=(14, 10))  # Width, Height of the chart
plt.bar(genres, popularity, color=['#4B0082', '#FF4500', '#1E90FF', '#32CD32', '#FFD700', '#8B0000', '#FF69B4', 
                                   '#8A2BE2', '#D2691E', '#5F9EA0', '#FF6347', '#4682B4', '#2E8B57', '#ADFF2F', 
                                   '#FF1493', '#B22222', '#DAA520', '#556B2F', '#7FFF00', '#20B2AA'], 
        width=0.6)  # Width of the bars

# Set the title and labels
plt.title('Music Genres Popularity')
plt.xlabel('Genre')
plt.ylabel('Popularity Score')

# Show the plot
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()