
import matplotlib.pyplot as plt

countries = ['Finland', 'Denmark', 'Switzerland', 'Iceland', 'Netherlands',
             'Norway', 'Sweden', 'Luxembourg', 'New Zealand', 'Austria',
             'Australia', 'Israel', 'Germany', 'Canada', 'Ireland', 
             'Costa Rica', 'United Kingdom', 'Czech Republic', 'United States', 'Belgium']
caloric_intake = [3200, 3150, 3100, 3080, 3050, 3000, 2950, 2900, 2880, 2850,
                  2820, 2800, 2780, 2750, 2730, 2700, 2680, 2650, 2600, 2580]

colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', 
          '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf', 
          '#bcbddc', '#fdae61', '#fee08b', '#d73027', '#1a9850', 
          '#91cf60', '#fee08b', '#e0f3f8', '#4575b4', '#313695']

plt.figure(figsize=(14, 8))
plt.bar(countries, caloric_intake, color=colors, edgecolor='black', width=0.5)

plt.ylabel('Caloric Intake (kcal/day)', fontsize=12)
plt.xlabel('Country', fontsize=12)
plt.title('Average Daily Caloric Intake by Country in 2021', fontsize=16)
plt.ylim(2500, 3300)

plt.xticks(rotation=90)
plt.tight_layout()
plt.show()