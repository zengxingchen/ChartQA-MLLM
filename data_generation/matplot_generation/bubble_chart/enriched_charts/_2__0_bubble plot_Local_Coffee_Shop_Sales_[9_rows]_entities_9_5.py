
import matplotlib.pyplot as plt

data = {
    'Country': ['United States', 'Germany', 'India', 'China', 'United Kingdom', 'Japan', 'Brazil', 'Canada', 'Australia',
                'France', 'Russia', 'South Korea', 'Italy', 'Spain', 'Mexico', 'Indonesia', 'Turkey', 'Saudi Arabia',
                'South Africa', 'Nigeria', 'Egypt', 'Vietnam', 'Bangladesh', 'Pakistan', 'Philippines', 'Argentina',
                'Colombia', 'Iran', 'Ukraine', 'Thailand'],
    'Literacy Rate (%)': [99, 99, 74, 97, 99, 99, 93, 99, 99, 99, 99, 99, 99, 98, 95, 93, 96, 94, 87, 62, 75, 95, 74, 60, 
                          94, 98, 95, 85, 99, 93],
    'Govt Expenditure on Education (billions)': [700, 160, 150, 550, 110, 90, 35, 95, 65, 120, 50, 55, 70, 60, 50, 30, 50, 
                                                 20, 20, 10, 20, 25, 10, 10, 20, 30, 20, 40, 15, 25],
    'Number of Universities': [4316, 429, 8500, 3000, 130, 783, 2370, 223, 43, 77, 896, 430, 96, 76, 196, 300, 200, 28, 25, 
                               150, 40, 235, 150, 200, 1200, 115, 86, 61, 300, 170]
}

fig, ax = plt.subplots(figsize=(18, 10))

sizes = [u/10 for u in data['Number of Universities']]

scatter = ax.scatter(x=data['Literacy Rate (%)'], y=data['Govt Expenditure on Education (billions)'], s=sizes, 
                     c=['#FF5733' if l > 95 else '#33FF57' if 85 < l <= 95 else '#3357FF' for l in data['Literacy Rate (%)']],
                     alpha=0.6, edgecolors='w', linewidth=2)

ax.set_title('Government Expenditure on Education vs Literacy Rate and Number of Universities', fontsize=18)
ax.set_xlabel('Literacy Rate (%)', fontsize=14)
ax.set_ylabel('Govt Expenditure on Education (billions)', fontsize=14)

for i, txt in enumerate(data['Country']):
    ax.annotate(txt, (data['Literacy Rate (%)'][i], data['Govt Expenditure on Education (billions)'][i]), fontsize=8, ha='center')

plt.show()