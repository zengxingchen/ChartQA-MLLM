
import matplotlib.pyplot as plt

# Data
instrument = ["VanGoghExhibit", "BroadwayShow", "MusicFestival", "ContemporaryArt", "ClassicalConcert", 
              "StreetArtFair", "DancePerformance", "Opera", "SculptureExhibit", "JazzNight", 
              "PhotographyShow", "FilmFestival", "CraftMarket", "ComicCon", "Circus", 
              "MuseumGala", "TheatrePlay", "SymphonyOrchestra", "MagicShow", "PuppetShow", 
              "Ballet", "IndieFilmScreening"]
year = [2021, 2019, 2020, 2022, 2021, 
        2019, 2020, 2022, 2021, 2020, 
        2019, 2021, 2022, 2021, 2020, 
        2022, 2021, 2019, 2020, 2022, 
        2021, 2019]
revenue = [500, 800, 600, 300, 400, 
           500, 350, 250, 450, 700, 
           750, 650, 150, 200, 500, 
           550, 400, 100, 300, 50, 
           100, 80]

# Create figure and axis objects
fig, ax = plt.subplots(figsize=(18, 14))

# Scatter plot
ax.scatter(year, revenue, color=["#FF6347", "#4682B4", "#8A2BE2", "#5F9EA0", "#7FFF00", 
                                "#DC143C", "#FF7F50", "#8B0000", "#6495ED", "#F08080", 
                                "#4169E1", "#FF1493", "#1E90FF", "#32CD32", "#FF4500", 
                                "#DAA520", "#4B0082", "#FF69B4", "#00CED1", "#8B0000", 
                                "#20B2AA", "#FF6347"])

# Title and labels
plt.title('Revenue vs. Year of Various Art & Design Events', fontsize=20, pad=20)
plt.xlabel('Year', fontsize=15)
plt.ylabel('Revenue (in thousands)', fontsize=15)

# Show plot
plt.show()