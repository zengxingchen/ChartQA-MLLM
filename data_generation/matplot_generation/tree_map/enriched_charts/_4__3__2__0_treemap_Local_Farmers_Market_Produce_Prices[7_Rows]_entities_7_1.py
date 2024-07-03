
import matplotlib.pyplot as plt
import squarify

# Data points
countries = [
    'USA', 'China', 'UK', 'Germany', 'France', 'Japan', 'Italy', 'Canada',
    'Spain', 'Australia', 'South Korea', 'Brazil', 'India', 'Russia',
    'Netherlands', 'Sweden', 'Norway', 'Mexico', 'Denmark', 'Switzerland',
    'Belgium', 'Austria', 'Finland', 'Ireland', 'New Zealand', 'Greece',
    'Poland', 'Portugal', 'Turkey', 'South Africa', 'Saudi Arabia', 'Israel', 'Others'
]
research_funding = [
    950, 720, 450, 380, 310, 290, 250, 240, 230, 220, 210, 200, 190, 180, 170, 160, 
    150, 140, 130, 120, 110, 100, 90, 80, 70, 60, 50, 40, 30, 25, 20, 15, 500
]

# Color scheme
colors = [
    '#FF5733', '#33FF57', '#3357FF', '#FF33A8', '#FF5733', '#33FFF0', '#3377FF', 
    '#57FF33', '#A833FF', '#5733FF', '#33FF57', '#FF5733', '#5733FF', '#FF3357', 
    '#57FF33', '#33FF57', '#3357FF', '#FF5733', '#33FF57', '#5733FF', '#33FFF0', 
    '#3377FF', '#FF33A8', '#33FF57', '#A833FF', '#5733FF', '#FF5733', '#FF33A8', 
    '#33FF57', '#A833FF', '#FF5733', '#33FFF0', '#D3D3D3'
]

plt.figure(figsize=(18, 14))
squarify.plot(sizes=research_funding, label=countries, color=colors, alpha=0.8)

# Chart details
plt.title('Global Research Funding by Country in 2023 (millions)', fontsize=20, y=1.02)
plt.axis('off')

plt.show()