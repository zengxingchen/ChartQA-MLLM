
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Create a DataFrame with the provided data
data = {
    'City': ['London', 'New York', 'Los Angeles', 'Tokyo', 'Paris', 'Berlin', 'Moscow', 'Beijing', 'Sydney', 'Rio de Janeiro', 'Cairo', 'Mumbai', 'Chicago', 'Toronto', 'Mexico City', 'Seoul', 'Madrid', 'Johannesburg', 'Dubai', 'Singapore'],
    'Startup_Investment_Billion': [3.5, 4.0, 2.5, 2.0, 1.8, 1.6, 1.2, 3.8, 2.2, 1.0, 0.8, 3.0, 2.6, 2.4, 1.4, 3.2, 1.7, 1.1, 2.9, 3.1],
    'Number_of_Startups': [4500, 5000, 3500, 3000, 2500, 2200, 1500, 4700, 3100, 1200, 800, 4000, 3700, 3400, 1800, 4200, 2300, 1300, 3900, 4100]
}

df = pd.DataFrame(data)

# Plotting the scatterplot
plt.figure(figsize=(14, 10))
scatterplot = sns.scatterplot(data=df, x='Startup_Investment_Billion', y='Number_of_Startups', palette=['#1f77b4', '#ff7f0e'])

scatterplot.set_title('Startup Investments and Number of Startups by City', fontsize=16)
scatterplot.set_xlabel('Startup Investment (Billion $)', fontsize=14)
scatterplot.set_ylabel('Number of Startups', fontsize=14)
plt.show()