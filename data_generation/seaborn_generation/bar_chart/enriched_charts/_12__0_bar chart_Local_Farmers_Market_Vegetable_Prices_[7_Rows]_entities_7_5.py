
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {
    'city': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia',
             'San Antonio', 'San Diego', 'Dallas', 'San Jose', 'Austin', 'Jacksonville',
             'Fort Worth', 'Columbus', 'Charlotte'],
    'exercise_hours': [6, 7, 5.5, 6.5, 7.5, 5.7, 6.2, 8, 6.8, 7.3, 7, 6, 5.5, 6.3, 6.7]
}

df = pd.DataFrame(data)

# Plotting
plt.figure(figsize=(10, 12))
barplot = sns.barplot(
    x='city',
    y='exercise_hours',
    data=df,
    palette=['#4E79A7', '#A0CBE8', '#F28E2C', '#FFBE7D', '#59A14F', '#8CD17D', 
             '#B6992D', '#F1CE63', '#499894', '#86BCB6', '#E15759', '#FF9D9A', 
             '#79706E', '#BAB0AC', '#D37295'],
    orient='v'
)

# Customize bars width
for bar in barplot.patches:
    bar.set_width(0.5)

plt.title('Average Weekly Exercise Hours in Various Cities', fontsize=16, pad=20)
plt.xlabel('City', fontsize=14)
plt.ylabel('Exercise Hours', fontsize=14)

plt.xticks(rotation=45, ha='right')

plt.tight_layout()
plt.show()