
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {
    'Age Group': ['Infants', 'Toddlers', 'Preschoolers', 'School-age', 'Teenagers', 'Young Adults', 'Adults', 'Older Adults'],
    'AverageSleepHours': [16, 13, 11, 10, 9, 7, 7, 6]
}

df = pd.DataFrame(data)

# Plot
plt.figure(figsize=(12, 6))  # Width and height modification
sns.barplot(x="Age Group", y="AverageSleepHours", data=df,
            palette=['#ff9999','#66b3ff','#99ff99','#ffcc99', '#c2c2f0','#ffb3e6', '#c4e17f', '#76d7c4'])  # Color modification using specific color codes

# Set the width of bars
for bar in plt.gca().patches:
    bar.set_width(0.6)  # Width of bars when vertical

plt.xlabel('Age Group')
plt.ylabel('Average Sleep Hours')
plt.title('Average Hours of Sleep Per Night by Age Group', pad=20)
sns.despine(left=True, bottom=True)  # Cleaning up the plot
plt.show()