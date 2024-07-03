
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create a DataFrame from the given data
data = {
    'Country': ['China', 'India', 'United States', 'Indonesia', 'Pakistan', 'Brazil', 'Nigeria', 'Bangladesh', 'Russia', 'Mexico', 'Japan', 'Ethiopia', 'Philippines', 'Egypt', 'Vietnam', 'DR Congo', 'Turkey', 'Iran', 'Germany', 'Thailand'],
    'Population': [1400, 1366, 331, 273, 220, 213, 206, 166, 145, 128, 126, 115, 109, 102, 97, 89, 84, 83, 83, 70],
    'PopularityRating': [85, 78, 95, 82, 70, 88, 65, 80, 90, 83, 96, 60, 76, 79, 75, 55, 85, 80, 92, 87],
    'RatingChange': [2, 1, 5, 3, 0, 4, -1, 2, 4, 3, 5, -2, 1, 2, 1, -3, 2, 1, 4, 3],
    'ReviewDensity': [150, 420, 36, 151, 286, 25, 226, 1265, 9, 66, 347, 115, 368, 102, 311, 40, 110, 52, 232, 137]
}
df = pd.DataFrame(data)

# Plot the bubble chart
plt.figure(figsize=(18, 12))
bubble_chart = sns.scatterplot(data=df, x='Population', y='PopularityRating', size='ReviewDensity', sizes=(20, 600), hue='Country', palette=['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#A133FF', '#FF8F33', '#33FFDA', '#FF5733', '#57FF33', '#3333FF', '#A1FF33', '#FF338F', '#5733FF', '#FF8333', '#33A1FF', '#8F33FF', '#FF33DA', '#33FF8F', '#DAFF33', '#FF5733'])

# Customizing the plot
plt.title('Population vs Popularity Rating by Country', fontsize=22, pad=20)
plt.xlabel('Population (in millions)', fontsize=16)
plt.ylabel('Popularity Rating', fontsize=16)
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0)

# Show the plot
plt.tight_layout()
plt.show()