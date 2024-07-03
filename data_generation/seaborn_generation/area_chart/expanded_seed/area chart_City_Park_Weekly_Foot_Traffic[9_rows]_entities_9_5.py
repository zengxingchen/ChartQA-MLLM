
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Given data
data = [
    {'Week': '2023-02-01 to 2023-02-07', 'Foot Traffic': 1050},
    {'Week': '2023-02-08 to 2023-02-14', 'Foot Traffic': 1250},
    {'Week': '2023-02-15 to 2023-02-21', 'Foot Traffic': 950},
    {'Week': '2023-02-22 to 2023-02-28', 'Foot Traffic': 875},
    {'Week': '2023-03-01 to 2023-03-07', 'Foot Traffic': 1375},
    {'Week': '2023-03-08 to 2023-03-14', 'Foot Traffic': 1425},
    {'Week': '2023-03-15 to 2023-03-21', 'Foot Traffic': 1330},
    {'Week': '2023-03-22 to 2023-03-28', 'Foot Traffic': 1290},
    {'Week': '2023-03-29 to 2023-04-04', 'Foot Traffic': 1450}
]

# Convert to DataFrame
df = pd.DataFrame(data)

# Parse week dates to use as x-axis
df['Week'] = df['Week'].apply(lambda x: pd.to_datetime(x.split(' to ')[0]))

# Set up the Seaborn theme
sns.set_theme(style="whitegrid")

# Create an area chart
plt.figure(figsize=(12, 6))
plt.fill_between(x=df['Week'], y1=df['Foot Traffic'], color="skyblue", alpha=0.4)

# Beautify the x-axis
plt.xticks(df['Week'], rotation=45, ha='right')

# Add titles and labels
plt.title('Foot Traffic by Week', size=16)
plt.xlabel('Week Starting', size=12)
plt.ylabel('Foot Traffic', size=12)

# Show the plot with a legend
plt.legend(['Foot Traffic'], loc='upper left')

# Show the plot
plt.tight_layout()
plt.show()