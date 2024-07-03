
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Country': ['United States', 'China', 'Germany', 'United Kingdom', 'France', 'Japan', 
                'Canada', 'Australia', 'India', 'Brazil', 'Russia', 'South Korea', 'Italy', 'Spain', 'Netherlands'],
    'Research Funding (Billion $)': [1600, 1300, 750, 650, 600, 850, 450, 350, 550, 400, 250, 500, 300, 280, 200],
    'Number of Universities': [4500, 3000, 1500, 1300, 1000, 1200, 900, 500, 800, 600, 500, 700, 600, 700, 400],
    'Average Graduation Rate (%)': [85, 80, 78, 83, 81, 79, 84, 82, 75, 77, 76, 80, 79, 80, 85]
}

df = pd.DataFrame(data)

plt.figure(figsize=(16, 10))
bubble_chart = sns.scatterplot(data=df, 
                               x='Research Funding (Billion $)', 
                               y='Number of Universities', 
                               size='Average Graduation Rate (%)', 
                               hue='Country', 
                               palette=["#ff9999", "#66b3ff", "#99ff99", "#ffcc99", 
                                        "#c2c2f0", "#ffb3e6", "#c4e17f", "#ff6666",
                                        "#c2f0c2", "#6666ff", "#99ffcc", "#ffccff", 
                                        "#ffb366", "#ff66b2", "#99ffb3"],
                               sizes=(100, 2000))

plt.title('Country-wise Research Funding vs Number of Universities and Average Graduation Rate', pad=20)
plt.xlabel('Research Funding (Billion $)')
plt.ylabel('Number of Universities')

bubble_chart.legend(loc='upper left', bbox_to_anchor=(1, 1), title='Country')

plt.show()