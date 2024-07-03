
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.DataFrame({
    "Destination": ["Paris", "Tokyo", "New York", "Rome", "Sydney", 
                    "London", "Bangkok", "Dubai", "Rio de Janeiro", "Istanbul", 
                    "Cape Town", "Barcelona", "Moscow", "Cairo", "Beijing"],
    "TravelGuide": ["Rick Steves", "Paul Theroux", "Anthony Bourdain", "Fodors", "Bill Bryson", 
                    "Travel Channel", "Lonely Planet", "National Geographic", "Rough Guides", "Frommer's", 
                    "Insight Guides", "DK Eyewitness", "Bradt Travel Guides", "Footprint", "Time Out"],
    "Visitors": [1000, 850, 900, 750, 650, 800, 700, 600, 500, 550, 480, 620, 530, 400, 460],
    "Cost": [1200, 1500, 1300, 1100, 1400, 1250, 1000, 2000, 900, 1100, 900, 1150, 1200, 800, 900],
    "Rating": [4.9, 4.8, 4.7, 4.8, 4.6, 4.7, 4.5, 4.8, 4.7, 4.6, 4.8, 4.7, 4.5, 4.6, 4.5]
})

plt.figure(figsize=(18, 14))
bubble_chart = sns.scatterplot(data=data, x="Cost", y="Rating", size="Visitors",
                               sizes=(100, 1000), alpha=0.7, palette=["#1f78b4", "#ff7f0e", "#33a02c", 
                               "#e31a1c", "#6a3d9a", "#b15928", "#a6cee3", "#fb9a99",
                               "#fdbf6f", "#cab2d6", "#ffff99", "#b2df8a", "#b15928",
                               "#ff7f0e", "#1f78b4"])

bubble_chart.set_xlabel("Average Travel Cost ($)", fontsize=14)
bubble_chart.set_ylabel("Average Rating (out of 5)", fontsize=14)
bubble_chart.set_title("Top Travel Destinations: Visitor Numbers, Cost, and Rating", fontsize=18, pad=20, loc='left')

h, lbls = bubble_chart.get_legend_handles_labels()
bubble_chart.legend(h[1:], lbls[1:], title="Visitors (Thousands)", borderpad=1, loc='upper left', labelspacing=1.5)

plt.show()