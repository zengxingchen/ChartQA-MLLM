
import matplotlib.pyplot as plt

# Data for scatterplot
countries = ["USA", "UK", "Germany", "France", "Japan", "China", 
             "India", "Brazil", "Russia", "Australia", "Canada", 
             "Italy", "Spain", "Mexico", "South Korea", "Netherlands",
             "Turkey", "Sweden", "South Africa", "New Zealand"]
screen_time = [7.0, 6.5, 5.8, 6.2, 5.0, 7.5, 6.8, 6.0, 5.5, 6.4, 
               6.7, 6.1, 5.9, 6.3, 7.2, 5.7, 6.6, 5.6, 6.0, 5.4]
stress_levels = [70, 65, 60, 63, 55, 75, 68, 64, 58, 66, 67, 62, 61, 
                 63, 72, 59, 66, 60, 62, 57]

# Create scatterplot
plt.figure(figsize=(14, 10))
plt.scatter(screen_time, stress_levels, c=[
    '#FF4500','#32CD32','#1E90FF','#FFD700','#FF69B4',
    '#8A2BE2','#00CED1','#FF6347','#4682B4','#DC143C',
    '#00FA9A','#A9A9A9','#FF1493','#7FFF00','#BA55D3',
    '#DAA520','#8B0000','#20B2AA','#ADFF2F','#FF7F50'], s=120)

# Customize plot
plt.title('Correlation between Average Daily Screen Time and Stress Levels in Different Countries', fontsize=18)
plt.xlabel('Average Daily Screen Time (hours)', fontsize=14)
plt.ylabel('Average Stress Level (index)', fontsize=14)

# Annotate data points
for i, country in enumerate(countries):
    plt.annotate(country, (screen_time[i], stress_levels[i]), 
                 textcoords="offset points", xytext=(0,10), ha='center')

# Show plot
plt.show()