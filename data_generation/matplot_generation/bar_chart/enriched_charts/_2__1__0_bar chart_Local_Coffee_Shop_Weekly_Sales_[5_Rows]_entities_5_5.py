
import matplotlib.pyplot as plt

countries = [
    "China", "United States", "India", "Russia", "Japan", "Germany", 
    "South Korea", "Canada", "Brazil", "Indonesia", "Mexico", "Iran", 
    "Saudi Arabia", "Australia", "South Africa", "Turkey", "United Kingdom", 
    "Italy", "France", "Thailand"
]
emissions = [
    11565, 5875, 2710, 1570, 1210, 760, 700, 680, 640, 620, 480, 470, 
    450, 420, 400, 380, 360, 340, 320, 300
]

plt.figure(figsize=(14, 8))
plt.barh(countries, emissions, color=[
    '#FF6347', '#FFA07A', '#20B2AA', '#87CEEB', '#778899', '#B0C4DE', 
    '#4682B4', '#708090', '#00FA9A', '#ADFF2F', '#32CD32', '#FFD700', 
    '#DAA520', '#FF8C00', '#FF4500', '#8B0000', '#A52A2A', '#800080', 
    '#BA55D3', '#9400D3'], height=0.5)

plt.xlabel('Greenhouse Gas Emissions (MtCO2e)', fontsize=14)
plt.title('Top 20 Countries by Greenhouse Gas Emissions', fontsize=16)
plt.xlim(0, 12000)
plt.tight_layout()
plt.show()