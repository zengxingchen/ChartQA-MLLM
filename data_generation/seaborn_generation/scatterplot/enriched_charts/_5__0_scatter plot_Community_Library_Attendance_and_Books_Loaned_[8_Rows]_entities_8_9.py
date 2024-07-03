
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Create a DataFrame with the provided data
data = {
    'Country': ['USA', 'Canada', 'Germany', 'France', 'UK', 'Japan', 'Australia', 'Italy', 'Spain', 'South Korea', 'China', 'India', 'Brazil', 'Russia', 'Mexico', 'Nigeria', 'South Africa'],
    'Life_Expectancy_Years': [78.5, 82.3, 81.2, 82.4, 81.0, 84.5, 82.8, 83.6, 83.4, 82.6, 76.7, 69.4, 75.7, 73.3, 75.0, 54.3, 64.1],
    'Healthcare_Expenditure_Percentage_GDP': [16.9, 10.7, 11.3, 11.2, 10.0, 10.9, 9.3, 9.0, 9.2, 8.1, 5.4, 3.6, 9.2, 5.3, 5.4, 3.9, 8.1]
}

df = pd.DataFrame(data)

# Plotting the scatterplot
plt.figure(figsize=(12, 8))
scatterplot = sns.scatterplot(data=df, x='Life_Expectancy_Years', y='Healthcare_Expenditure_Percentage_GDP', palette=['#FFA07A', '#20B2AA'])

scatterplot.set_title('Life Expectancy vs. Healthcare Expenditure by Country')
scatterplot.set_xlabel('Life Expectancy (Years)')
scatterplot.set_ylabel('Healthcare Expenditure (% of GDP)')
plt.show()