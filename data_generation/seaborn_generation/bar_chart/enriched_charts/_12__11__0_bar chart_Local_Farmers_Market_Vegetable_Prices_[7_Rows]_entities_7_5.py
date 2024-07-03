
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {
    'city': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia',
             'San Antonio', 'San Diego', 'Dallas', 'San Jose', 'Austin', 'Jacksonville',
             'Fort Worth', 'Columbus', 'Charlotte'],
    'satisfaction_rate': [85, 75, 70, 65, 68, 72, 60, 78, 66, 80, 74, 58, 62, 69, 71]
}

df = pd.DataFrame(data)

# Plotting
plt.figure(figsize=(14, 8))
barplot = sns.barplot(
    y='city',
    x='satisfaction_rate',
    data=df,
    palette=['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#FFBD33', '#33FFF3',
             '#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#FFBD33', '#33FFF3',
             '#FF5733', '#33FF57', '#3357FF'],
    orient='h'
)

# Customize bars width
for bar in barplot.patches:
    bar.set_height(0.7)

plt.title('Customer Satisfaction Rates in Major Cities', pad=20)
plt.xlabel('Satisfaction Rate (%)')
plt.ylabel('City')
plt.tight_layout()

plt.show()