
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data provided
data = [
    {'Month': 'January', 'Attendance': 120, 'Books Loaned': 320},
    {'Month': 'February', 'Attendance': 135, 'Books Loaned': 350},
    {'Month': 'March', 'Attendance': 150, 'Books Loaned': 370},
    {'Month': 'April', 'Attendance': 160, 'Books Loaned': 390},
    {'Month': 'May', 'Attendance': 175, 'Books Loaned': 420},
    {'Month': 'June', 'Attendance': 180, 'Books Loaned': 450},
    {'Month': 'July', 'Attendance': 165, 'Books Loaned': 430},
    {'Month': 'August', 'Attendance': 160, 'Books Loaned': 410}
]

# Convert the data into a Pandas DataFrame
df = pd.DataFrame(data)

# Convert the 'Month' into categorical type so that it can be used for hue encoding
df['Month'] = pd.Categorical(df['Month'], categories=[
    'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August'
], ordered=True)

# Initialize the matplotlib figure
plt.figure(figsize=(10, 6))

# Create a scatterplot
sns.scatterplot(
    data=df, 
    x='Attendance', 
    y='Books Loaned', 
    hue='Month',  # Color points by 'Month'
    size='Attendance',  # Vary point size by 'Attendance'
    sizes=(50, 200),  # Range of point sizes
    style='Month',  # Vary point style by 'Month'
    palette='viridis',  # Color palette
    legend='full'
)

# Improve the layout
plt.title('Monthly Attendance vs Books Loaned')
plt.xlabel('Attendance')
plt.ylabel('Books Loaned')

# Show the plot
plt.legend(title='Month', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()

# Show the final plot
plt.show()