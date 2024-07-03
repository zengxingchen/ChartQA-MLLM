
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Creating the DataFrame from the provided list of dictionaries
data = [
    {'Month': '2023-01', 'New Members': 25, 'Classes Attended': 150, 'Personal Training Sessions': 40},
    {'Month': '2023-02', 'New Members': 20, 'Classes Attended': 130, 'Personal Training Sessions': 35},
    {'Month': '2023-03', 'New Members': 30, 'Classes Attended': 180, 'Personal Training Sessions': 50},
    {'Month': '2023-04', 'New Members': 35, 'Classes Attended': 200, 'Personal Training Sessions': 60},
    {'Month': '2023-05', 'New Members': 40, 'Classes Attended': 220, 'Personal Training Sessions': 65},
    {'Month': '2023-06', 'New Members': 45, 'Classes Attended': 240, 'Personal Training Sessions': 70},
    {'Month': '2023-07', 'New Members': 50, 'Classes Attended': 260, 'Personal Training Sessions': 75},
    {'Month': '2023-08', 'New Members': 40, 'Classes Attended': 230, 'Personal Training Sessions': 65},
    {'Month': '2023-09', 'New Members': 45, 'Classes Attended': 240, 'Personal Training Sessions': 68},
    {'Month': '2023-10', 'New Members': 50, 'Classes Attended': 250, 'Personal Training Sessions': 72},
    {'Month': '2023-11', 'New Members': 55, 'Classes Attended': 270, 'Personal Training Sessions': 80},
    {'Month': '2023-12', 'New Members': 60, 'Classes Attended': 300, 'Personal Training Sessions': 90}
]
df = pd.DataFrame(data)
df['Month'] = pd.to_datetime(df['Month'])

# Setting the plotting style
sns.set(style="whitegrid")

# Creating the lineplot
plt.figure(figsize=(14, 8))

# Plotting each metric with a unique style
sns.lineplot(x='Month', y='New Members', data=df, marker='o', label='New Members', color='blue')
sns.lineplot(x='Month', y='Classes Attended', data=df, marker='s', label='Classes Attended', color='green', dashes=True)
sns.lineplot(x='Month', y='Personal Training Sessions', data=df, marker='^', label='Personal Training Sessions', color='red', dashes=[(5, 2)])

# Customizing the ticks on x-axis to show them as YYYY-MM
plt.xticks(df['Month'], df['Month'].dt.strftime('%Y-%m'))
plt.xticks(rotation=45)  # rotate the x-axis labels for better readability

# Adding title and labels
plt.title('Gym Usage Statistics Over 2023')
plt.xlabel('Month')
plt.ylabel('Count')

# Positioning the legend
plt.legend(title='Key')

# Showing the plot
plt.tight_layout()
plt.show()