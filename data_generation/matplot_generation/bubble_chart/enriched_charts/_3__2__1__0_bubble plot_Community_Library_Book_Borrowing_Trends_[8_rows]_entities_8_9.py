
import matplotlib.pyplot as plt

data = {
    'Category': ['North America', 'South America', 'Europe', 'Africa', 'Asia', 'Australia', 'Antarctica',
                 'Arctic', 'Indian Ocean', 'Pacific Ocean', 'Atlantic Ocean', 'Caribbean', 'Mediterranean',
                 'Middle East', 'Central Asia', 'Eastern Europe', 'Western Europe', 'Northern Europe',
                 'Southern Europe', 'Eastern Asia', 'South Asia', 'Southeast Asia', 'Central America',
                 'Eastern Africa', 'Western Africa', 'Northern Africa', 'Southern Africa', 'North Pole', 'South Pole'],
    'Calories': [250, 300, 350, 200, 400, 350, 100, 150, 275, 320, 290, 240, 330, 310, 270, 260, 340, 285, 365, 390, 380, 355, 325, 240, 230, 250, 265, 105, 120],
    'Protein (g)': [20, 15, 25, 10, 30, 20, 5, 10, 18, 22, 16, 12, 26, 24, 19, 17, 27, 20, 28, 29, 27, 23, 21, 14, 12, 15, 18, 6, 8],
    'Satisfaction Score': [75, 80, 85, 70, 90, 88, 60, 65, 78, 82, 77, 74, 83, 81, 79, 76, 84, 80, 86, 89, 87, 85, 81, 72, 70, 75, 77, 62, 65]
}

size = [value * 10 for value in data['Calories']]

plt.figure(figsize=(20, 14))

scatter = plt.scatter(data['Protein (g)'], data['Satisfaction Score'], 
                      s=size, alpha=0.6, 
                      c=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', 
                         '#7f7f7f', '#bcbd22', '#17becf', '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', 
                         '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf', '#1f77b4', 
                         '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22'])

plt.title('Regional Nutritional and Satisfaction Analysis', pad=20)
plt.xlabel('Protein Intake (g)')
plt.ylabel('Satisfaction Score')

for index, category in enumerate(data['Category']):
    plt.text(data['Protein (g)'][index], data['Satisfaction Score'][index], 
             category, fontsize=9, ha='center', va='center')

plt.grid(True)
plt.show()