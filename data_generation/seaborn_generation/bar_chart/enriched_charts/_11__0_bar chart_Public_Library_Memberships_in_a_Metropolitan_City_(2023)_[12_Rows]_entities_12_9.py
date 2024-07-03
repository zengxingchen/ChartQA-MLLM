
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Create a DataFrame from the data points provided
data = {
    'Profession': ["Software Developer", "Data Scientist", "Graphic Designer", "Marketing Manager", 
                   "Accountant", "Mechanical Engineer", "Project Manager", "HR Specialist", 
                   "Financial Analyst", "Sales Manager", "Civil Engineer", "Operations Manager", 
                   "Business Analyst", "Product Manager", "Electrical Engineer", "Teacher", 
                   "Nurse", "Lawyer", "Doctor", "Architect"],
    'Average Income': [105000, 110000, 60000, 75000, 65000, 70000, 90000, 58000, 85000, 95000, 
                       72000, 92000, 88000, 98000, 80000, 52000, 68000, 130000, 150000, 75000]
}

df = pd.DataFrame(data)

# Set the aesthetic style of the plots
sns.set_theme(style="whitegrid")

# Create the bar plot and modify it according to the given options
plt.figure(figsize=(12, 14))  # Change width and height of chart
barplot = sns.barplot(x='Profession', y='Average Income', data=df, color="#4C72B0", ci=None)  # Vertical and specific color

# Modify the width of bars
for bar in barplot.patches:
    bar.set_width(0.5)  # Adjust the width of the bars

# Adjust the appearance of the plot
plt.title('Average Annual Income by Profession', fontsize=18, pad=20)
plt.xlabel('Profession', fontsize=14)
plt.ylabel('Average Income (USD)', fontsize=14)
plt.xticks(rotation=45, fontsize=12, ha='right')
plt.yticks(fontsize=12)

# Remove the top and right spines
sns.despine(left=True, bottom=True)

# Show the barplot
plt.show()