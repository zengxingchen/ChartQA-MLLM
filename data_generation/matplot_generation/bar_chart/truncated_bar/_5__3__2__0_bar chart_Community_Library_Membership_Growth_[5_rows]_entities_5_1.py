
import matplotlib.pyplot as plt

# Data from the table above
countries = [
    'United States', 'Germany', 'United Kingdom', 'France', 'Italy', 
    'Spain', 'Greece', 'Brazil', 'India', 'China', 'Japan', 
    'South Korea', 'Australia', 'Canada', 'Russia', 'Turkey',
    'Mexico', 'Argentina', 'South Africa', 'Egypt'
]

average_rainfall = [
    715, 700, 1120, 850, 850, 636, 540, 1761, 1190, 645, 
    1670, 1300, 534, 537, 460, 600, 758, 619, 469, 51
]

colors = [
    '#4B8BBE', '#306998', '#FFE873', '#FFD43B', '#646464',
    '#3C9D9B', '#F05A28', '#264653', '#2A9D8F', '#E9C46A',
    '#F4A261', '#E76F51', '#A8DADC', '#457B9D', '#1D3557',
    '#D90429', '#EF233C', '#8D99AE', '#2B2D42', '#FB8500'
]

plt.figure(figsize=(16, 10))
plt.bar(countries, average_rainfall, color=colors, width=0.6)
plt.ylim(400, 1800)
plt.xticks(rotation=45, ha='right')
plt.ylabel('Average Rainfall (mm)')
plt.title('Average Annual Rainfall by Country')
plt.tight_layout()
plt.show()