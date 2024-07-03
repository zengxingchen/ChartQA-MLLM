
import matplotlib.pyplot as plt

countries = [
    'Canada', 'Russia', 'Germany', 'United Kingdom', 'France', 'Spain', 
    'Italy', 'Greece', 'Turkey', 'Australia', 'Brazil', 'India', 
    'China', 'Japan', 'South Korea', 'Mexico', 'South Africa', 
    'Argentina', 'Nigeria', 'Egypt'
]

healthcare_expenditure = [
    300, 400, 450, 420, 370, 290, 310, 280, 350, 380, 330, 500, 
    550, 460, 340, 260, 230, 240, 200, 220
]

colors = [
    '#FF4500', '#FF8C00', '#FFA500', '#FFD700', '#ADFF2F', '#32CD32', 
    '#00FA9A', '#00CED1', '#1E90FF', '#4169E1', '#6A5ACD', '#8A2BE2', 
    '#FF1493', '#C71585', '#DB7093', '#FF6347', '#7FFFD4', '#4682B4', 
    '#D2691E', '#8B008B'
]

plt.figure(figsize=(14, 10))
plt.bar(countries, healthcare_expenditure, color=colors, width=0.6)
plt.ylabel('Healthcare Expenditure (billions)')
plt.title('Healthcare Expenditure by Country', pad=20)
plt.ylim(150, 600)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()