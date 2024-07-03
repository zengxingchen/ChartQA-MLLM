
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Create DataFrame with generated data
data = {
    'Age': [24, 27, 34, 53, 21, 45, 39, 33, 56, 48, 31, 24, 58, 30, 22, 41, 37, 
            26, 42, 35, 49, 50, 32, 55, 46, 28, 36, 40, 38, 25, 23, 44, 29, 47, 
            52, 43, 60, 54, 57, 51, 59]
}

df = pd.DataFrame(data)

# Set the aesthetic style of the plots
sns.set_style('whitegrid')

# Set the size of the figure
plt.figure(figsize=(12, 6))

# Plot the histogram chart
sns.histplot(df['Age'], bins=20, kde=False, color='#34a4eb', binwidth=2)

# Adding title and labels
plt.title('Age Distribution of a Population')
plt.xlabel('Age')
plt.ylabel('Frequency')

# Show plot
plt.show()