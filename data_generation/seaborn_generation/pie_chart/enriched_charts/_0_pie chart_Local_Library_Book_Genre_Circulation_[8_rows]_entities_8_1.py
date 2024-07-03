
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Dataframe
data = {
    'OS': ['Android', 'iOS', 'KaiOS', 'Samsung', 'Unknown', 'Others'],
    'Market Share': [74.45, 22.85, 0.91, 0.74, 0.66, 0.39]
}

df = pd.DataFrame(data)

# Prepare data for 'pie chart' like visualization
df['angle'] = df['Market Share']/df['Market Share'].sum() * 2 * np.pi
df['color'] = ['#FF6F61', '#6B5B95', '#88B04B', '#F7CAC9', '#92A8D1', '#955251']

# Barplot to mimic pie chart
plt.figure(figsize=(8, 8))
ax = plt.subplot(111, polar=True)
ax.bar(x=df['angle'].cumsum() - df['angle']/2, 
       height=df['Market Share'], 
       width=df['angle'], 
       color=df['color'], 
       linewidth=2, 
       edgecolor='white')

# Custom settings
ax.set_theta_direction(-1)
ax.set_theta_zero_location('N')
ax.set_axis_off()

# Title
plt.title('Smartphone OS Market Share in 2023', pad=20, fontsize=18)

plt.show()