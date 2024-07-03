
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Your data
data = [
    {'Month': 'January', 'New Memberships': 48},
    {'Month': 'February', 'New Memberships': 55},
    {'Month': 'March', 'New Memberships': 60},
    {'Month': 'April', 'New Memberships': 57},
    {'Month': 'May', 'New Memberships': 63},
    {'Month': 'June', 'New Memberships': 70},
    {'Month': 'July', 'New Memberships': 75},
    {'Month': 'August', 'New Memberships': 72},
    {'Month': 'September', 'New Memberships': 68},
    {'Month': 'October', 'New Memberships': 80},
    {'Month': 'November', 'New Memberships': 83},
    {'Month': 'December', 'New Memberships': 90}
]

# Convert the list of dictionaries to a pandas DataFrame
df = pd.DataFrame(data)

# Since Seaborn does not have a direct function for area plots, we will use matplotlib
# We will use seaborn's style for consistent look and feel
sns.set_theme(style="whitegrid")

# Create an area plot
plt.fill_between(df['Month'], df['New Memberships'])
plt.plot(df['Month'], df['New Memberships'], color='Slateblue')

# Add titles and labels
plt.title('New Memberships by Month')
plt.xlabel('Month')
plt.ylabel('New Memberships')

# Add gridlines
plt.grid(True)

# Rotate x-axis labels for better visibility
plt.xticks(rotation=45)

# Optional: Remove spines / borders
sns.despine(left=True, bottom=True)

# Show the plot
plt.show()