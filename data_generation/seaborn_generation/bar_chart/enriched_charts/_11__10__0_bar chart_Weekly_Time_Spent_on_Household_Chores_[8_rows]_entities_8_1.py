
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia', 'San Antonio', 'San Diego', 
             'Dallas', 'San Jose', 'Austin', 'Jacksonville', 'Fort Worth', 'Columbus', 'Charlotte', 'Indianapolis', 
             'San Francisco', 'Seattle', 'Denver', 'Washington'],
    'Number_of_Wellness_Centers': [300, 250, 180, 160, 140, 130, 120, 110, 100, 90, 85, 80, 75, 70, 65, 60, 55, 50, 45, 40]
}

df = pd.DataFrame(data)

# Plot
plt.figure(figsize=(14, 8))  # Width and height modification
sns.barplot(x="Number_of_Wellness_Centers", y="City", data=df,
            palette=['#FF5733','#33FF57','#3357FF','#F333FF', '#FF8333','#33FFF8', '#D4FF33', '#FF3342', '#FFB533',
                     '#6F33FF', '#33FFB5', '#33C4FF', '#83FF33', '#C833FF', '#FF3333', '#FFDA33', '#FF3396', '#3357FF', '#FF5733', '#33FF57'],
            dodge=False)  # Color modification using specific color codes

# Set the bars' height
for bar in plt.gca().patches:
    bar.set_height(0.5)  # Height of bars when horizontal

plt.xlabel('Number of Wellness Centers')
plt.ylabel('City')
plt.title('Number of Wellness Centers in Various Cities')
sns.despine(left=True, bottom=True)  # Cleaning up the plot
plt.show()