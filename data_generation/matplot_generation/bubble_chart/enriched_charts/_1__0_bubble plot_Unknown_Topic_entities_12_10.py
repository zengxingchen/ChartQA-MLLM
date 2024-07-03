
import matplotlib.pyplot as plt

data = {
    'Company': ['MindWellness', 'HealthCore', 'WellnessWave', 'NutriLife', 'FitForward', 
                'LifeBalance', 'HealthyMind', 'VitalityPlus', 'WellBeingInc', 
                'HealthFusion', 'EcoWellness', 'MindBodyTech', 'HarmonyHealth', 
                'HolisticCare', 'ZenLife', 'BalanceBio'],
    'R&D Investment (Millions)': [1800, 950, 420, 1350, 350, 500, 390, 600, 760, 1050, 680, 300, 480, 840, 250, 1100],
    'Revenue (Billions)': [55, 32, 23, 48, 14, 20, 24, 28, 31, 40, 21, 18, 26, 34, 12, 45],
    'Employee Satisfaction (1-10)': [9.0, 8.2, 9.4, 9.1, 7.0, 8.5, 8.3, 9.0, 8.9, 9.3, 7.6, 7.2, 8.8, 8.6, 6.4, 9.2]
}

fig, ax = plt.subplots(figsize=(14, 9))

for i in range(len(data['Company'])):
    ax.scatter(data['R&D Investment (Millions)'][i], data['Revenue (Billions)'][i], 
               s=(data['Employee Satisfaction (1-10)'][i] ** 3) * 10, 
               alpha=0.6,
               color=['#FF5733', '#33FF57', '#3357FF', '#57FF33', '#5733FF', 
                      '#FF33A1', '#33FFA1', '#A133FF', '#FFA133', '#A1FF33', 
                      '#33A1FF', '#FF5733', '#5733A1', '#33FF57', '#3357FF', 
                      '#FF33A1'][i])

ax.set_title('Health Companies: R&D Investment vs Revenue with Employee Satisfaction as Bubble Size', fontsize=16, pad=20)
ax.set_xlabel('R&D Investment (Millions)', fontsize=14)
ax.set_ylabel('Revenue (Billions)', fontsize=14)
ax.grid(True)

plt.show()