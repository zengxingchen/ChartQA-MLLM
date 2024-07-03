
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Temperature_Celsius': [5, 6, 10, 15, 20, 25, 30, 29, 24, 18, 10, 6]
}

df = pd.DataFrame(data)
df = df.sort_values('Temperature_Celsius')

f, ax = plt.subplots(figsize=(10, 8))

sns.barplot(
    y="Month", 
    x="Temperature_Celsius", 
    data=df,
    palette=['#4c72b0', '#dd8452', '#55a868', '#c44e52', '#8172b2', '#937860', '#da8bc3', '#8c8c8c', '#ccb974', '#64b5cd', '#ff9896', '#c5b0d5'],
    edgecolor=".2",
    linewidth=1.5
)

sns.set_context("poster", font_scale=0.8)
ax.bar_label(ax.containers[0], label_type='edge')

ax.set_xlim(0, 35)
ax.set_xlabel('Average Temperature (°C)')
ax.set_ylabel('Month')
ax.set_title('Average Monthly Temperature of a City', pad=20)

plt.tight_layout()
plt.show()