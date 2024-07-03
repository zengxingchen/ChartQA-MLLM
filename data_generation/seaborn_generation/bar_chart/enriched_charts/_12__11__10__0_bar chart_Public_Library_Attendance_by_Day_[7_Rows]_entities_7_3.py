
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Rainfall_mm': [78, 54, 61, 90, 110, 150, 175, 160, 130, 95, 70, 60]
}

df = pd.DataFrame(data)
df = df.sort_values('Rainfall_mm')

f, ax = plt.subplots(figsize=(12, 6))

sns.barplot(
    y="Rainfall_mm", 
    x="Month", 
    data=df,
    palette=['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0','#ffb3e6','#c4e17f','#76d7c4','#e59866','#e74c3c','#8e44ad','#3498db'],
    edgecolor=".2",
    linewidth=1.5,
    ci=None,
    width=0.8
)

sns.set_context("poster", font_scale=0.8)
ax.bar_label(ax.containers[0], label_type='edge')

ax.set_ylim(0, 200)
ax.set_ylabel('Average Rainfall (mm)')
ax.set_xlabel('Month')
ax.set_title('Average Monthly Rainfall in a City', pad=20)

plt.tight_layout()
plt.show()