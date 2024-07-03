
import seaborn as sns
import matplotlib.pyplot as plt

# Data points
data = {
    "Average_Monthly_Temperature": [2.4, 3.1, 7.2, 10.3, 15.6, 20.1, 23.8, 22.7, 17.9, 12.5, 6.2, 3.9]
}

# Create DataFrame
import pandas as pd
df = pd.DataFrame(data)

# Set style
sns.set_style('whitegrid')

# Increase the figure size and adjust histogram width (bin width)
plt.figure(figsize=(10, 6))
sns.histplot(df['Average_Monthly_Temperature'], color="#3498db", binwidth=1.5)

# Tweak the title and labels
plt.title('Distribution of Average Monthly Temperatures')
plt.xlabel('Temperature (Celsius)')
plt.ylabel('Frequency')

# Visualize the plot
plt.show()