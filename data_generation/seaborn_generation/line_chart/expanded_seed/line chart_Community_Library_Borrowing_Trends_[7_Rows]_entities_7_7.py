
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Given data
data = [
    {'Month': 'January', 'E-books Borrowed': 3200, 'Physical Books Borrowed': 8700, 'Magazines Borrowed': 450},
    {'Month': 'February', 'E-books Borrowed': 2800, 'Physical Books Borrowed': 9100, 'Magazines Borrowed': 390},
    {'Month': 'March', 'E-books Borrowed': 3000, 'Physical Books Borrowed': 9500, 'Magazines Borrowed': 410},
    {'Month': 'April', 'E-books Borrowed': 3500, 'Physical Books Borrowed': 9800, 'Magazines Borrowed': 370},
    {'Month': 'May', 'E-books Borrowed': 4000, 'Physical Books Borrowed': 10200, 'Magazines Borrowed': 350},
    {'Month': 'June', 'E-books Borrowed': 3700, 'Physical Books Borrowed': 9900, 'Magazines Borrowed': 400},
    {'Month': 'July', 'E-books Borrowed': 3600, 'Physical Books Borrowed': 10100, 'Magazines Borrowed': 420}
]

# Convert the data into a pandas DataFrame
df = pd.DataFrame(data)

# Reshape the DataFrame to 'melt' it for seaborn
df_melted = df.melt(id_vars='Month', var_name='Category', value_name='Borrowed')

# Create a lineplot using seaborn
plt.figure(figsize=(10, 6))
sns.lineplot(data=df_melted, x='Month', y='Borrowed', hue='Category', style='Category', markers=True, dashes=False)

# Optional: Enhance the plot with title, labels, and other aesthetics
plt.title('Library Borrowings by Month')
plt.xlabel('Month')
plt.ylabel('Number of Items Borrowed')
plt.xticks(rotation=45) # Rotate x-axis labels for better readability

# Show the legend
plt.legend(title='Category')

# Show the plot
plt.tight_layout()
plt.show()