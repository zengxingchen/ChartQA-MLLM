
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Mock data for the frequency of reading books (times read per year)
data = {
    'Frequency': [
        30, 35, 40, 38, 33, 45, 50, 60, 55, 65, 70, 75, 80, 85, 90
    ]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Initialize the matplotlib figure
plt.figure(figsize=(12, 8))

# Create the histogram
sns.histplot(data=df, x='Frequency', bins=10, color='#ff6347', binwidth=5)

# Customizing the plot's aesthetics
plt.title('Histogram of Annual Book Reading Frequency')
plt.xlabel('Times Read Per Year')
plt.ylabel('Number of People')

# Show the plot
plt.show()