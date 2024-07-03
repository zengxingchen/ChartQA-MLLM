
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Your table data
data = [
    {'Month': 'January', 'Adult Memberships': 1200, 'Youth Memberships': 300, 'Senior Memberships': 450},
    {'Month': 'February', 'Adult Memberships': 1250, 'Youth Memberships': 320, 'Senior Memberships': 470},
    # ... include all other months here
    {'Month': 'December', 'Adult Memberships': 1450, 'Youth Memberships': 390, 'Senior Memberships': 520}
]

# Convert the table data into a Pandas DataFrame
df = pd.DataFrame(data)

# We melt the DataFrame to have a proper format for Seaborn
df_melted = df.melt(id_vars='Month', var_name='Membership Type', value_name='Count')

# Set the aesthetic style of the plots
sns.set_style("whitegrid")

# Initialize the matplotlib figure
f, ax = plt.subplots(figsize=(12, 6))

# Create a barplot
sns.barplot(x="Month", y="Count", hue="Membership Type", data=df_melted, ax=ax)

# Customize the plot with title, labels, and other aesthetics
ax.set_title('Monthly Memberships')
ax.set_xlabel('Month')
ax.set_ylabel('Number of Memberships')

# Rotate the x-axis labels for better readability
plt.xticks(rotation=45)

# Place the legend outside the plot
plt.legend(title='Membership Type', bbox_to_anchor=(1.05, 1), loc='upper left')

# Show the plot
plt.show()