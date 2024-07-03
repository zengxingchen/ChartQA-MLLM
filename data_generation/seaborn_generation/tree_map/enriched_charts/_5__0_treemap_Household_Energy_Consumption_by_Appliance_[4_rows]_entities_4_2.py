
import matplotlib.pyplot as plt
import pandas as pd
import squarify

# Data for the chart
data = {
    "Category": ["Sports & Fitness", "Sports & Fitness", "Sports & Fitness",
                 "Business & Entrepreneurship", "Business & Entrepreneurship", "Business & Entrepreneurship",
                 "Future Technologies & Society", "Future Technologies & Society", "Future Technologies & Society",
                 "Education & Learning", "Education & Learning", "Education & Learning",
                 "Astronomy & Space Exploration", "Astronomy & Space Exploration", "Astronomy & Space Exploration"],
    "Subcategory": ["Running Shoes", "Yoga Mats", "Fitness Trackers",
                    "Startups", "Corporate", "Investments",
                    "AI Research", "Robotics", "Blockchain",
                    "Online Courses", "E-Books", "Tutoring Services",
                    "Space Missions", "Telescope Sales", "Astro Photography"],
    "Value": [150000, 85000, 120000, 
              300000, 450000, 320000, 
              600000, 400000, 200000, 
              250000, 180000, 140000, 
              500000, 170000, 110000]
}

df = pd.DataFrame(data)

# Create a color palette, mapped to Category
color_mapper = {
    'Sports & Fitness': '#1f77b4',
    'Business & Entrepreneurship': '#ff7f0e',
    'Future Technologies & Society': '#2ca02c',
    'Education & Learning': '#d62728',
    'Astronomy & Space Exploration': '#9467bd'
}

colors = [color_mapper[category] for category in df['Category']]

# Create the figure
fig, ax = plt.subplots(1, figsize=(14, 10))

# Create the treemap
squarify.plot(sizes=df['Value'], label=df['Subcategory'], color=colors, alpha=0.8, text_kwargs={'fontsize':9})

plt.title('Market Valuation of Categories by Subcategories in Various Fields', fontsize=16)
plt.axis('off')
plt.show()