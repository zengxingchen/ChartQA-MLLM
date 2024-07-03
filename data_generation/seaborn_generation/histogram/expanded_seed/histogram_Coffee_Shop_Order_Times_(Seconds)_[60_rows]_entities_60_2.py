
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Your data supplied as a list of dictionaries
data = [
    {'OrderID': 1, 'Preparation Time': 180},
    {'OrderID': 2, 'Preparation Time': 240},
    {'OrderID': 3, 'Preparation Time': 200},
    {'OrderID': 4, 'Preparation Time': 310},
    {'OrderID': 5, 'Preparation Time': 120},
    {'OrderID': 6, 'Preparation Time': 165},
    {'OrderID': 7, 'Preparation Time': 185},
    {'OrderID': 8, 'Preparation Time': 260},
    {'OrderID': 9, 'Preparation Time': 210},
    {'OrderID': 10, 'Preparation Time': 195},
    {'OrderID': 11, 'Preparation Time': 225},
    {'OrderID': 12, 'Preparation Time': 235},
    {'OrderID': 13, 'Preparation Time': 280},
    {'OrderID': 14, 'Preparation Time': 230},
    {'OrderID': 15, 'Preparation Time': 190}
]

# Convert the list of dictionaries to a pandas DataFrame
df = pd.DataFrame(data)

# Set a style
sns.set_style("whitegrid")

# Create a color palette
palette = sns.color_palette("coolwarm", n_colors=len(data))

# Create the histogram with additional aesthetics
plt.figure(figsize=(10, 6))
hist_plot = sns.histplot(data=df, x='Preparation Time', bins=5, kde=False, palette=palette, edgecolor='black')

# Additional customizations
hist_plot.set_title('Distribution of Preparation Times', fontsize=20)
hist_plot.set_xlabel('Preparation Time (seconds)', fontsize=14)
hist_plot.set_ylabel('Order Frequency', fontsize=14)

# Annotate each bar with the count
for p in hist_plot.patches:
    hist_plot.annotate(f'{int(p.get_height())}', (p.get_x() + p.get_width() / 2., p.get_height()),
                       ha='center', va='center', fontsize=10, color='black', xytext=(0, 5),
                       textcoords='offset points')

# Finalize the plot
sns.despine(trim=True)
plt.tight_layout()

# Show the plot
plt.show()