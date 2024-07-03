
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data in a pandas DataFrame
data = pd.DataFrame({
    'Daily_Steps': [3450, 2890, 3012, 4500, 5120, 5300, 4800, 4670, 3890, 3720, 4910, 5400, 5680, 6020, 6180, 6450, 
                    6720, 6590, 7010, 6880, 7520, 7890, 8120, 8350, 7480, 7120, 6910, 6670, 6340, 5980, 5760, 5500, 
                    5010, 4820, 4600, 4390, 4100, 3920, 3720, 3540, 3300, 3110, 2950, 2760, 2550, 2370, 2180, 1990, 
                    1850, 1680, 1520, 1350, 1200, 1050, 900, 750, 600, 480, 320]
})

# Set the size of the seaborn plot
plt.figure(figsize=(12, 8))

# Plot a vertical histogram with specified bin width and color
sns.histplot(data, y='Daily_Steps', binwidth=500, color="#FF5733", orientation='horizontal')

# Set chart title and labels
plt.title('Daily Steps Distribution in a Month')
plt.xlabel('Count')
plt.ylabel('Daily Steps')

# Show the plot
plt.show()