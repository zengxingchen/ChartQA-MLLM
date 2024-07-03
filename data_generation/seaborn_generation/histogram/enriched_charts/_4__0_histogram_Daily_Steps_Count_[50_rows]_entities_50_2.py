
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Given table data as a DataFrame
data = pd.DataFrame({
    'Stock Price': [
        101, 98, 103, 105, 102, 99, 100, 107, 110, 108,
        111, 114, 113, 115, 118, 117, 116, 119, 122, 121,
        120, 123, 124, 125, 126, 129, 130, 128, 127, 131,
        132, 133, 135, 134, 136, 138, 137, 139, 140, 141,
        142, 145, 143, 146, 144, 147, 148, 149, 150
    ]
})

# Setting the style
sns.set(style='whitegrid')

# Changing the size of the plot
plt.figure(figsize=(12, 8))

# Creating the histogram
# Changing color scheme using hexadecimal color codes
# Changing the orientation to vertical
# Adjusting the width of the bins
sns.histplot(data['Stock Price'], color='#e74c3c', binwidth=2, binrange=(95,155), orientation='vertical')

# Changing the chart title
plt.title('Distribution of Daily Stock Prices')

# Adjusting the labels
plt.xlabel('Stock Price ($)')
plt.ylabel('Frequency')

# Display the plot
plt.show()