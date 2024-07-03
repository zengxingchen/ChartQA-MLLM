
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import squarify

# Given table data
data = [
    {'Sector': 'Food & Beverage', 'Business Type': 'Restaurants', 'Monthly Revenue (in thousands)': 200},
    {'Sector': 'Food & Beverage', 'Business Type': 'Cafes', 'Monthly Revenue (in thousands)': 150},
    {'Sector': 'Retail', 'Business Type': 'Clothing Stores', 'Monthly Revenue (in thousands)': 120},
    {'Sector': 'Retail', 'Business Type': 'Electronics', 'Monthly Revenue (in thousands)': 90},
    {'Sector': 'Services', 'Business Type': 'Beauty Salons', 'Monthly Revenue (in thousands)': 75},
    {'Sector': 'Services', 'Business Type': 'Car Repair', 'Monthly Revenue (in thousands)': 70},
    {'Sector': 'Entertainment', 'Business Type': 'Movie Theaters', 'Monthly Revenue (in thousands)': 130},
    {'Sector': 'Entertainment', 'Business Type': 'Bowling Alleys', 'Monthly Revenue (in thousands)': 45},
    {'Sector': 'Health & Wellness', 'Business Type': 'Gyms', 'Monthly Revenue (in thousands)': 90},
    {'Sector': 'Health & Wellness', 'Business Type': 'Yoga Studios', 'Monthly Revenue (in thousands)': 60},
    {'Sector': 'Education', 'Business Type': 'Private Tutors', 'Monthly Revenue (in thousands)': 40},
    {'Sector': 'Education', 'Business Type': 'Dance Schools', 'Monthly Revenue (in thousands)': 50}
]

# Convert to DataFrame
df = pd.DataFrame(data)

# Set the aesthetic style of the plots
sns.set(style="whitegrid")

# Create a figure and a set of subplots
fig, ax = plt.subplots(1, figsize=(12, 8))

# Treemap plot
squarify.plot(sizes=df['Monthly Revenue (in thousands)'], 
              label=df['Business Type'], 
              alpha=.8,
              text_kwargs={'fontsize': 9})

# Remove the axes
plt.axis('off')

# Add a title to the plot
plt.title('Treemap of Monthly Revenue by Business Type')

# Show plot
plt.show()