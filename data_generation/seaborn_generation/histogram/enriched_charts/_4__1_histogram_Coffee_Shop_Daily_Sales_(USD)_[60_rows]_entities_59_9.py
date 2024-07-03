
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Data points
data = {
    "Hours_Studied": [1.5, 2.3, 2.7, 3.1, 3.3, 4.0, 4.2, 5.1, 5.3, 6.0, 6.8, 7.2, 7.6, 8.1, 8.5, 9.0]
}

# Create DataFrame
df = pd.DataFrame(data)

# Set style
sns.set_style('whitegrid')

# Increase the figure size and adjust histogram width (bin width)
plt.figure(figsize=(12, 8))
sns.histplot(df['Hours_Studied'], color="#e74c3c", binwidth=1.0, orientation="horizontal")

# Tweak the title and labels
plt.title('Distribution of Hours Studied by Students', pad=20)
plt.xlabel('Frequency')
plt.ylabel('Hours Studied')

# Visualize the plot
plt.show()