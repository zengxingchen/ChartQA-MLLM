
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Create the DataFrame from the provided data
data = [
    {'Month': 'January', 'Visits': 4500}, {'Month': 'February', 'Visits': 3700},
    {'Month': 'March', 'Visits': 4800}, {'Month': 'April', 'Visits': 5100},
    {'Month': 'May', 'Visits': 5300}, {'Month': 'June', 'Visits': 4900},
    {'Month': 'July', 'Visits': 4700}, {'Month': 'August', 'Visits': 4600},
    {'Month': 'September', 'Visits': 5200}, {'Month': 'October', 'Visits': 5500},
    {'Month': 'November', 'Visits': 5400}, {'Month': 'December', 'Visits': 5800},
    {'Month': 'January', 'Visits': 4650}, {'Month': 'February', 'Visits': 3900},
    {'Month': 'March', 'Visits': 4950}
]
df = pd.DataFrame(data)

# Set the aesthetic style of the plots
sns.set_style('whitegrid')

# Create the histogram
plt.figure(figsize=(10, 6))
hist_plot = sns.histplot(df['Visits'], bins=12, kde=True, color='skyblue')

# Add titles and labels
hist_plot.set_title('Histogram of Website Visits per Month', fontsize=16)
hist_plot.set_xlabel('Number of Visits', fontsize=14)
hist_plot.set_ylabel('Frequency', fontsize=14)

# Improve layout and display the plot
plt.tight_layout()
plt.show()