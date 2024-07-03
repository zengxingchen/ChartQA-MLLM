
import matplotlib.pyplot as plt
import pandas as pd
import squarify

data = {
    "Country": ["China", "United States", "India", "Russia", "Japan",
                "Germany", "South Korea", "Iran", "Canada", "Saudi Arabia",
                "Indonesia", "Brazil", "Mexico", "South Africa", "Australia"],
    "GreenhouseGasEmissions": [10460000, 5000000, 3300000, 2100000, 1200000,
                               900000, 700000, 690000, 600000, 580000,
                               540000, 510000, 490000, 480000, 460000]
}

df = pd.DataFrame(data)

color_mapper = {
    'China': '#FF5733', 
    'United States': '#33FF57', 
    'India': '#3357FF', 
    'Russia': '#FF33A1', 
    'Japan': '#F3FF33', 
    'Germany': '#33FFF6', 
    'South Korea': '#FF8A33', 
    'Iran': '#8A33FF', 
    'Canada': '#57FF33', 
    'Saudi Arabia': '#3357FF', 
    'Indonesia': '#33FFF6', 
    'Brazil': '#FF333A', 
    'Mexico': '#8A33FF', 
    'South Africa': '#FF33A1', 
    'Australia': '#57FF33'
}

colors = [color_mapper[country] for country in df['Country']]

fig, ax = plt.subplots(1, figsize=(14, 10))

squarify.plot(sizes=df['GreenhouseGasEmissions'], label=df['Country'], color=colors, alpha=0.8, text_kwargs={'fontsize':9})

plt.title('Greenhouse Gas Emissions by Country (in thousand metric tons)', fontsize=16)
plt.axis('off')
plt.show()