
import matplotlib.pyplot as plt
import pandas as pd
import squarify

# Data for the chart
data = {
    "Category": ["Politics & Governance", "Politics & Governance", "Politics & Governance",
                 "Environment & Climate Change", "Environment & Climate Change", "Environment & Climate Change",
                 "Music & Performing Arts", "Music & Performing Arts", "Music & Performing Arts",
                 "Fashion & Beauty", "Fashion & Beauty", "Fashion & Beauty",
                 "Education & Learning", "Education & Learning", "Education & Learning",
                 "Health & Psychology", "Health & Psychology", "Health & Psychology",
                 "Economics & Finance", "Economics & Finance", "Economics & Finance"],
    "Subcategory": ["Policy Research", "Campaign Management", "Public Administration",
                    "Renewable Energy", "Climate Policy", "Conservation Projects",
                    "Live Concerts", "Theater Productions", "Music Education",
                    "Fashion Shows", "Cosmetics", "Personal Styling",
                    "Online Courses", "E-Books", "Tutoring Services",
                    "Mental Health Services", "Nutrition Counseling", "Physical Therapy",
                    "Investment Banking", "Stock Market Analysis", "Insurance"],
    "Value": [250000, 150000, 300000, 
              450000, 320000, 380000, 
              600000, 400000, 200000, 
              250000, 180000, 140000, 
              500000, 170000, 110000, 
              300000, 200000, 400000, 
              600000, 350000, 250000]
}

df = pd.DataFrame(data)

# Create a color palette, mapped to Category
color_mapper = {
    'Politics & Governance': '#FF5733',
    'Environment & Climate Change': '#33FF57',
    'Music & Performing Arts': '#3357FF',
    'Fashion & Beauty': '#FF33A8',
    'Education & Learning': '#33FFF6',
    'Health & Psychology': '#FFC300',
    'Economics & Finance': '#DAF7A6'
}

colors = [color_mapper[category] for category in df['Category']]

# Create the figure
fig, ax = plt.subplots(1, figsize=(16, 12))

# Create the treemap
squarify.plot(sizes=df['Value'], label=df['Subcategory'], color=colors, alpha=0.8, text_kwargs={'fontsize':10})

plt.title('Market Valuation of Categories by Subcategories in Various Fields', fontsize=20)
plt.axis('off')
plt.show()