
import matplotlib.pyplot as plt

# Given data points (Notice the structured tabular data):
data = {
    'Company': ['TechCorp', 'InnovateInc', 'PioneerTech', 'NextGen', 'AlphaTech', 
                'BetaSolutions', 'GammaTech', 'DeltaProducts', 'EpsilonEnterprises', 
                'ZetaTech', 'EtaElectronics', 'ThetaSystems', 'IotaInnovations',
                'KappaCreations', 'LambdaDevelopment'],
    'R&D Investment (Millions)': [1500, 800, 400, 1200, 300, 450, 380, 550, 710, 950, 620, 290, 470, 820, 230],
    'Revenue (Billions)': [50, 30, 20, 45, 12, 18, 22, 25, 29, 33, 19, 15, 21, 40, 10],
    'Employee Satisfaction (1-10)': [8.5, 7.2, 9.1, 8.8, 6.7, 7.9, 8.1, 8.3, 8.6, 9.2, 7.4, 6.5, 8.0, 7.8, 6.1]
}

fig, ax = plt.subplots(figsize=(12, 8))  # Adjusting the size of the chart

for i in range(len(data['Company'])):
    ax.scatter(data['R&D Investment (Millions)'][i], data['Revenue (Billions)'][i], 
               s=(data['Employee Satisfaction (1-10)'][i] ** 3) * 10,  # Bubble sizes
               alpha=0.6,
               color=f'#{hex(255 - i*10)[2:]}{hex(50 + i*10)[2:]}{hex(100 + i*10)[2:]}')  # Diversified hexadecimal colors

# Customizing the plot
ax.set_title('Tech Companies: R&D Investment vs Revenue with Employee Satisfaction as Bubble Size', fontsize=14)
ax.set_xlabel('R&D Investment (Millions)', fontsize=12)
ax.set_ylabel('Revenue (Billions)', fontsize=12)
ax.grid(True)

plt.show()