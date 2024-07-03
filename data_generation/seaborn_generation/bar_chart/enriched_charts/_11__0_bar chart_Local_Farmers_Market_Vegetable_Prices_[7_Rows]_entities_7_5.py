
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {
    'city': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia',
             'San Antonio', 'San Diego', 'Dallas', 'San Jose', 'Austin', 'Jacksonville',
             'Fort Worth', 'Columbus', 'Charlotte'],
    'ai_adoption': [78, 70, 65, 60, 55, 68, 50, 72, 58, 80, 75, 48, 52, 62, 66],
    'blockchain_adoption': [56, 45, 50, 40, 35, 52, 30, 47, 38, 60, 55, 28, 32, 43, 48],
    'vr_adoption': [64, 59, 55, 50, 52, 58, 48, 62, 54, 66, 63, 46, 49, 53, 57]
}

df = pd.DataFrame(data)

# Plotting
plt.figure(figsize=(12, 10))
barplot = sns.barplot(
    x='city',
    y='ai_adoption',
    data=df,
    palette=['#4C72B0', '#55A868', '#C44E52', '#8172B2', '#CCB974', '#64B5CD',
             '#4C72B0', '#55A868', '#C44E52', '#8172B2', '#CCB974', '#64B5CD',
             '#4C72B0', '#55A868', '#C44E52'],
    orient='v'
)

# Customize bars width
for bar in barplot.patches:
    bar.set_width(0.5)

plt.title('Adoption Rates of Emerging Technologies in Major Cities', pad=20)
plt.xlabel('City')
plt.ylabel('AI Adoption Rate (%)')
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()