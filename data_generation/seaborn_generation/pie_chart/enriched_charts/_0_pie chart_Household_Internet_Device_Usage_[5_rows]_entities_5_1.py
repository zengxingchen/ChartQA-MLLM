
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Data
data = {
    'Brand': ['Toyota', 'Volkswagen', 'Ford', 'BMW', 'Honda', 'Mercedes', 'Hyundai', 'Audi', 'Subaru', 'Volvo'],
    'Market Share': [25, 20, 15, 10, 9, 8, 7, 3, 2, 1]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Define colors
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', 
          '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']

# Plot
plt.figure(figsize=(10, 6))
plt.pie(df['Market Share'], labels=df['Brand'], colors=colors, autopct='%1.1f%%', startangle=140)
plt.title('Car Brand Market Share in 2023')
plt.axis('equal')  # Equal aspect ratio to ensure the pie is drawn as a circle.

plt.show()