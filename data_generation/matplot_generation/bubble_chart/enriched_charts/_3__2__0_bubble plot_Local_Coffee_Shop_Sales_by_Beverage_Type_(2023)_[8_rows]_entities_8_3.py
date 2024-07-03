
import matplotlib.pyplot as plt

# Data
countries = ['United States', 'China', 'Japan', 'Germany', 'South Korea', 'India', 'France', 'United Kingdom', 
             'Italy', 'Canada', 'Russia', 'Brazil', 'Australia', 'Spain', 'Mexico', 'Netherlands', 'Sweden', 
             'Switzerland', 'Belgium', 'Norway', 'Finland', 'Denmark', 'Ireland', 'Israel', 'Singapore']
research_expenditure = [600, 500, 350, 300, 270, 250, 230, 220, 210, 200, 190, 180, 170, 160, 150, 140, 130, 120, 
                        110, 100, 90, 80, 70, 60, 50]  # in billion USD
patents_granted = [120, 110, 90, 85, 80, 75, 70, 65, 60, 55, 50, 45, 40, 35, 30, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10]  # number in thousands
researchers = [16, 14, 13, 12, 11.5, 11, 10.5, 10, 9.5, 9, 8.5, 8, 7.5, 7, 6.5, 6, 5.8, 5.6, 5.4, 5.2, 5, 4.8, 4.6, 4.4, 4.2]  # number in millions

# Normalize the researchers data to use as bubble sizes
max_researchers = max(researchers)
bubble_sizes = [(r / max_researchers) * 1000 for r in researchers]

# Plot
plt.figure(figsize=(18, 10))  # Adjusted width and height of the chart
plt.scatter(research_expenditure, patents_granted, s=bubble_sizes,
            color=['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#A133FF', '#FFD133', '#33FFD7', '#D733FF', 
                   '#FF5733', '#57FF33', '#3357FF', '#FF33A1', '#A133FF', '#FFD133', '#33FFD7', '#D733FF', 
                   '#5733FF', '#A1FF33', '#FF3357', '#33FFA1', '#A157FF', '#FFD733', '#33D7FF', '#FF5733', '#57FF33'],
            alpha=0.7)

# Additional Customization
plt.title('Research Expenditure vs. Patents Granted by Country', pad=20)
plt.xlabel('Research Expenditure (billion USD)')
plt.ylabel('Patents Granted (thousands)')
plt.xticks(rotation=45)
plt.grid(True)

# Annotating the country names
for i, country in enumerate(countries):
    plt.text(research_expenditure[i], patents_granted[i], country, ha='center', va='center')

# Show the plot
plt.tight_layout()
plt.show()