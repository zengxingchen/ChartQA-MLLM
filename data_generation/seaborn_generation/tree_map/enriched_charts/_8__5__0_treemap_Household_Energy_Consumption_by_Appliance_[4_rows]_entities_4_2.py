
import matplotlib.pyplot as plt
import pandas as pd
import squarify

data = {
    "Category": ["Travel & Adventure", "Travel & Adventure", "Travel & Adventure",
                 "Travel & Adventure", "Travel & Adventure", "Travel & Adventure",
                 "Travel & Adventure", "Travel & Adventure", "Travel & Adventure",
                 "Travel & Adventure", "Travel & Adventure", "Travel & Adventure",
                 "Travel & Adventure", "Travel & Adventure", "Travel & Adventure"],
    "Subcategory": ["Hiking", "Camping", "Backpacking",
                    "Scuba Diving", "Surfing", "Sky Diving",
                    "Rock Climbing", "Safari", "Mountain Biking",
                    "Skiing", "Snowboarding", "Kayaking",
                    "White Water Rafting", "Paragliding", "Hot Air Ballooning"],
    "Value": [200000, 150000, 100000, 
              250000, 180000, 160000, 
              220000, 300000, 170000, 
              190000, 210000, 140000, 
              120000, 130000, 200000]
}

df = pd.DataFrame(data)

# Create a color palette, mapped to Category
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#33FFF0', 
          '#FF9633', '#A133FF', '#57FF33', '#33D1FF', '#FF5733', 
          '#33FF57', '#3357FF', '#FF33A1', '#33FFF0', '#FF9633']

# Create the figure
fig, ax = plt.subplots(1, figsize=(16, 12))

# Create the treemap
squarify.plot(sizes=df['Value'], label=df['Subcategory'], color=colors, alpha=0.8, text_kwargs={'fontsize':10})

plt.title('Popularity of Various Travel & Adventure Activities', fontsize=20)
plt.axis('off')
plt.show()