
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Topic': ['Climate Change', 'Climate Change', 'Renewable Energy', 'Renewable Energy', 'Water Conservation', 'Water Conservation', 
              'Air Quality', 'Air Quality', 'Biodiversity', 'Biodiversity', 'Waste Management', 'Waste Management', 'Ocean Health', 
              'Ocean Health', 'Land Use', 'Land Use', 'Energy Efficiency', 'Energy Efficiency'],
    'Category': ['Greenhouse Gas Emissions', 'Deforestation Rate', 'Solar Power Adoption', 'Wind Power Adoption', 'Freshwater Availability', 'Water Pollution Levels', 
                 'Urban Air Pollution', 'Rural Air Quality', 'Species Extinction Rate', 'Protected Areas Coverage', 'Recycling Rate', 'Plastic Waste Reduction', 
                 'Coral Reef Health', 'Overfishing Levels', 'Urban Sprawl', 'Sustainable Agriculture', 'Building Energy Efficiency', 'Industrial Energy Efficiency'],
    'Value': [7, 5, 8, 6, 9, 7, 6, 4, 8, 7, 3, 6, 5, 4, 5, 8, 9, 5],
    'Impact Score': [80, 70, 90, 75, 85, 80, 70, 65, 85, 75, 60, 70, 65, 60, 75, 85, 90, 70]
}

df = pd.DataFrame(data)

plt.figure(figsize=(16, 12))
bubble_chart = sns.scatterplot(
    data=df,
    x="Value",
    y="Impact Score",
    size="Impact Score",
    sizes=(100, 2000),
    hue="Impact Score",
    palette=["#4B0082", "#8A2BE2", "#5F9EA0", "#FF6347", "#4682B4", "#7FFF00", "#D2691E", "#FF4500", "#2E8B57", "#1E90FF", "#FFD700", "#DA70D6", "#32CD32", "#BA55D3", "#FF69B4", "#8B0000", "#00FF00", "#8B4513"],
    alpha=0.8,
    legend='full'
)

bubble_chart.set_title("Impact of Various Environmental Factors", fontsize=18, pad=20)
bubble_chart.set_xlabel("Value", fontsize=14)
bubble_chart.set_ylabel("Impact Score", fontsize=14)
bubble_chart.legend(loc='upper left', bbox_to_anchor=(1, 1), title="Impact Score")

plt.show()