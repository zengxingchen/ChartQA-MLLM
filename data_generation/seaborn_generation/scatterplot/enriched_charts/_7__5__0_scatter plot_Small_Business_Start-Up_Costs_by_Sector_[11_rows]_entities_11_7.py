
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt 

# Data points
data = {
    'University': ['Harvard', 'Stanford', 'MIT', 'Caltech', 'Princeton', 'Yale', 'Columbia', 'UChicago', 'UPenn', 'Brown', 
                   'Cornell', 'Duke', 'Northwestern', 'Johns_Hopkins', 'Dartmouth', 'Vanderbilt', 'Rice', 'Notre_Dame', 
                   'WashU', 'Georgetown', 'UC_Berkeley', 'UCLA', 'Michigan', 'UVA', 'UNC', 'Boston_College', 'Emory', 
                   'USC', 'NYU', 'Carnegie_Mellon'],
    'Monthly_Expense': [2000, 2100, 1900, 1800, 2200, 2050, 1950, 2000, 2100, 1850, 1950, 2000, 2050, 1900, 1800, 1950, 
                        2050, 1850, 2000, 2100, 1750, 1800, 1900, 1850, 1950, 2000, 2100, 2200, 2250, 1950],
    'Student_Satisfaction': [4.7, 4.6, 4.8, 4.5, 4.7, 4.6, 4.7, 4.5, 4.7, 4.4, 4.6, 4.5, 4.6, 4.5, 4.4, 4.6, 4.5, 4.4, 
                             4.6, 4.5, 4.3, 4.4, 4.5, 4.4, 4.5, 4.4, 4.5, 4.6, 4.5, 4.6]
}

# Create DataFrame
df = pd.DataFrame(data)

# Set up the matplotlib figure
plt.figure(figsize=(16, 12))

# Draw a seaborn scatter plot
sb.scatterplot(data=df, x="Monthly_Expense", y="Student_Satisfaction", palette=['#1f77b4', '#ff7f0e'], s=100)

# Additional customizations
plt.title('Monthly Expense and Student Satisfaction in U.S. Universities', fontsize=18, y=1.03)
plt.xlabel('Monthly Expense (USD)', fontsize=14)
plt.ylabel('Student Satisfaction (Out of 5)', fontsize=14)
plt.grid(True)

# Show the plot
plt.show()