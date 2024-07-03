
import matplotlib.pyplot as plt

# Data
instrument = ["Piano", "Violin", "Guitar", "Flute", "Drums", 
              "Trumpet", "Harp", "Saxophone", "Cello", "Clarinet", 
              "Tuba", "Oboe", "Bassoon", "Accordion", "Mandolin", 
              "Tambourine", "Synthesizer", "Ukulele", "Banjo", "Marimba", 
              "Bagpipes", "Lute"]
popularity = [80, 90, 85, 70, 60, 75, 50, 55, 95, 65, 40, 45, 85, 50, 60, 25, 70, 80, 55, 65, 40, 45]
complexity = [60, 85, 40, 30, 75, 60, 95, 45, 90, 20, 50, 70, 25, 75, 10, 55, 15, 35, 65, 55, 85, 20]

# Create figure and axis objects
fig, ax = plt.subplots(figsize=(14, 10))

# Scatter plot
ax.scatter(popularity, complexity, color=["#4B0082", "#FFD700", "#FF69B4", "#4682B4", "#8A2BE2", 
                                          "#5F9EA0", "#D2691E", "#6495ED", "#DC143C", "#8FBC8F", 
                                          "#FF6347", "#FF4500", "#DA70D6", "#ADFF2F", "#FF7F50", 
                                          "#008B8B", "#8B0000", "#20B2AA", "#4169E1", "#F08080", 
                                          "#7FFF00", "#FF1493"])

# Title and labels
plt.title('Popularity vs. Complexity of Various Musical Instruments')
plt.xlabel('Popularity')
plt.ylabel('Complexity')

# Show plot
plt.show()