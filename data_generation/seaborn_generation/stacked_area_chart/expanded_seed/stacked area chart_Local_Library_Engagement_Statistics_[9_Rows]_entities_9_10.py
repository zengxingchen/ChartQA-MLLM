
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Your data in dictionary form
data = [
    {'Month': 'January', 'Visitors': 2300, 'Books Loaned': 5700, 'eBook Downloads': 3100, 'Event Attendees': 450},
    {'Month': 'February', 'Visitors': 2100, 'Books Loaned': 5300, 'eBook Downloads': 2900, 'Event Attendees': 400},
    {'Month': 'March', 'Visitors': 2500, 'Books Loaned': 5900, 'eBook Downloads': 3300, 'Event Attendees': 480},
    {'Month': 'April', 'Visitors': 2400, 'Books Loaned': 6000, 'eBook Downloads': 3400, 'Event Attendees': 500},
    {'Month': 'May', 'Visitors': 2600, 'Books Loaned': 6100, 'eBook Downloads': 3200, 'Event Attendees': 520},
    {'Month': 'June', 'Visitors': 2700, 'Books Loaned': 6200, 'eBook Downloads': 3500, 'Event Attendees': 540},
    {'Month': 'July', 'Visitors': 2800, 'Books Loaned': 6300, 'eBook Downloads': 3600, 'Event Attendees': 550},
    {'Month': 'August', 'Visitors': 2900, 'Books Loaned': 6400, 'eBook Downloads': 3700, 'Event Attendees': 560},
    {'Month': 'September', 'Visitors': 2700, 'Books Loaned': 6200, 'eBook Downloads': 3500, 'Event Attendees': 540}
]

# Convert dictionary to pandas DataFrame
df = pd.DataFrame(data)

# Setting Seaborn style
sns.set_style('whitegrid')

# Figuring out the proper order of months since Matplotlib's stackplot doesn't automatically sort categories
df['Month'] = pd.Categorical(df['Month'], categories=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September'], ordered=True)
df.sort_values('Month', inplace=True)

# Preparing data for the stackplot
x = df['Month']
y = [df['Visitors'], df['Books Loaned'], df['eBook Downloads'], df['Event Attendees']]

# Plotting the stacked area chart
plt.figure(figsize=(10, 7))
plt.stackplot(x, y, labels=['Visitors', 'Books Loaned', 'eBook Downloads', 'Event Attendees'], alpha=0.8)

# Adding the legend, title, and labels
plt.legend(loc='upper left')
plt.title('Monthly Usage Statistics')
plt.xlabel('Month')
plt.ylabel('Count')

# Display the plot
plt.tight_layout()
plt.show()