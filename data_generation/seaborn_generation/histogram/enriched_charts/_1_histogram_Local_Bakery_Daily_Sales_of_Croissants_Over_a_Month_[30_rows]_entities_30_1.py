
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data
age_data = {'Age': [23, 25, 34, 45, 28, 30, 30, 31, 56, 60, 61, 63, 65, 67, 70, 72, 75, 77, 
                    80, 82, 85, 87, 90, 92, 18, 20, 21, 22, 24, 26, 27, 29, 32, 33, 35, 36, 
                    37, 38, 39, 40, 41, 42, 43, 44, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 
                    57, 58, 59, 62, 64, 66, 68, 69, 71, 73, 74, 76, 78, 79, 81, 83, 84, 86, 
                    88, 89, 91, 93, 94, 95, 96, 97, 98, 99, 100]}
df = pd.DataFrame(age_data)

# Set size of the figure
plt.figure(figsize=(10, 6))

# Plotting the histogram
sns.histplot(data=df, x='Age', binwidth=5, color='#007acc', edgecolor='#0a0a0a')

# Additional customizations
plt.title('Age Distribution in a Population')
plt.xlabel('Age (years)')
plt.ylabel('Frequency')
plt.grid(True)

# Show the plot
plt.show()