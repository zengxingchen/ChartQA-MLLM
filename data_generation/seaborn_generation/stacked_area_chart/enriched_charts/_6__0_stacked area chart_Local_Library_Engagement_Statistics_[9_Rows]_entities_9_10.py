
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 
              'July', 'August', 'September', 'October', 'November', 'December'],
    'AI': [200, 220, 250, 270, 300, 320, 340, 360, 380, 400, 420, 440],
    'Robotics': [180, 190, 210, 220, 240, 260, 280, 300, 320, 340, 360, 380],
    'Quantum Computing': [170, 175, 180, 185, 190, 200, 210, 220, 230, 240, 250, 260],
    'Bioinformatics': [160, 165, 170, 175, 180, 190, 200, 210, 220, 230, 240, 250]
}

df = pd.DataFrame(data)
df.set_index('Month', inplace=True)

# Cumulative data for stacked area chart
cumulative = df.cumsum(axis=1)

# Plotting
plt.figure(figsize=(14, 10))
pal = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1']
plt.stackplot(cumulative.index, cumulative['AI'], cumulative['Robotics'],
              cumulative['Quantum Computing'], cumulative['Bioinformatics'], labels=cumulative.columns, colors=pal)
plt.legend(loc='upper left')
plt.title('Monthly Investment in Future Technologies', fontsize=16, pad=20)
plt.xlabel('Month')
plt.ylabel('Investment (in Million Dollars)')
plt.annotate('Peak for AI', xy=(11.2, cumulative.loc['December', 'AI']),
             xytext=(10.5, cumulative.loc['December', 'AI']+500),
             arrowprops=dict(facecolor='black', arrowstyle="->", connectionstyle="arc3"))
plt.annotate('Steady Growth in Robotics', xy=(11.2, cumulative.loc['December', 'Robotics']),
             xytext=(10.5, cumulative.loc['December', 'Robotics']+200),
             arrowprops=dict(facecolor='black', arrowstyle="->", connectionstyle="arc3"))
plt.tight_layout()
plt.show()