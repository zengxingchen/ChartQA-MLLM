
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia', 'San Antonio', 'San Diego', 
             'Dallas', 'San Jose', 'Austin', 'Jacksonville', 'Fort Worth', 'Columbus', 'Charlotte', 'Indianapolis', 
             'San Francisco', 'Seattle', 'Denver', 'Washington'],
    'Number_of_Museums': [85, 60, 55, 40, 35, 33, 30, 28, 25, 22, 20, 18, 16, 15, 14, 13, 12, 11, 10, 9]
}

df = pd.DataFrame(data)

# Plot
plt.figure(figsize=(10, 14))  # Width and height modification
sns.barplot(y="Number_of_Museums", x="City", data=df,
            palette=['#FF5733', '#33FF57', '#3357FF', '#F333FF', '#FF8333', '#33FFF8', '#D4FF33', '#FF3342', '#FFB533',
                     '#6F33FF', '#33FFB5', '#33C4FF', '#83FF33', '#C833FF', '#FF3333', '#FFDA33', '#FF3396', '#3357FF', '#FF5733', '#33FF57'],
            dodge=False)  # Color modification using specific color codes

# Set the bars' width
for bar in plt.gca().patches:
    bar.set_width(0.4)  # Width of bars when vertical

plt.ylabel('Number of Museums')
plt.xlabel('City')
plt.title('Number of Museums in Various Cities')
plt.xticks(rotation=90)  # Rotate city names for better readability
sns.despine(left=True, bottom=True)  # Cleaning up the plot
plt.show()