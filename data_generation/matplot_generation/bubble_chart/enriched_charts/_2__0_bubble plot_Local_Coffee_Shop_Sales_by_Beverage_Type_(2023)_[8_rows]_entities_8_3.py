
import matplotlib.pyplot as plt

# Data
countries = ['United States', 'China', 'Japan', 'Germany', 'South Korea', 'India', 'France', 'United Kingdom', 
             'Italy', 'Canada', 'Russia', 'Brazil', 'Australia', 'Spain', 'Mexico']
research_expenditure = [500, 450, 300, 280, 260, 240, 220, 210, 200, 190, 180, 170, 160, 150, 140]  # in billion USD
patents_granted = [100, 95, 85, 80, 75, 70, 65, 60, 55, 50, 45, 40, 35, 30, 25]  # number in thousands
researchers = [15, 13.5, 12, 11, 10.5, 10, 9.5, 9, 8.5, 8, 7.5, 7, 6.5, 6, 5.5]  # number in millions

# Normalize the researchers data to use as bubble sizes
max_researchers = max(researchers)
bubble_sizes = [(r / max_researchers) * 1000 for r in researchers]

# Plot
plt.figure(figsize=(16, 9))  # Adjusted width and height of the chart
plt.scatter(research_expenditure, patents_granted, s=bubble_sizes,
            color=['#FF4500', '#1E90FF', '#32CD32', '#FFD700', '#FF6347', '#6A5ACD', '#20B2AA', '#FF69B4', 
                   '#8B4513', '#708090', '#FFA500', '#ADFF2F', '#4682B4', '#FF1493', '#B22222'],
            alpha=0.6)

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