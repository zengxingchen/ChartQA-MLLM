
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Topic': ['Mental Health', 'Mental Health', 'Physical Health', 'Physical Health', 'Emotional Health', 'Emotional Health', 'Financial Health', 
              'Financial Health', 'Career Health', 'Career Health', 'Environmental Health', 'Environmental Health', 'Community Health', 
              'Community Health', 'Global Health', 'Global Health', 'Technological Health', 'Technological Health'],
    'Category': ['Stress Management', 'Therapy Usage', 'Exercise Frequency', 'Nutrition Quality', 'Social Connections', 'Sleep Quality', 
                 'Savings Rate', 'Debt Levels', 'Job Satisfaction', 'Work-Life Balance', 'Pollution Levels', 'Conservation Efforts', 
                 'Volunteerism', 'Crime Rates', 'Epidemic Preparedness', 'Vaccination Rates', 'Internet Access', 'Data Privacy'],
    'Value': [7, 5, 8, 6, 9, 7, 6, 4, 8, 7, 3, 6, 5, 4, 5, 8, 9, 5],
    'Impact Score': [80, 70, 90, 75, 85, 80, 70, 65, 85, 75, 60, 70, 65, 60, 75, 85, 90, 70]
}

df = pd.DataFrame(data)

plt.figure(figsize=(14, 10))
bubble_chart = sns.scatterplot(
    data=df,
    x="Value",
    y="Impact Score",
    size="Impact Score",
    sizes=(100, 2000),
    hue="Impact Score",
    palette=["#FF5733", "#33FF57", "#3357FF", "#FF33A1", "#33FFF3", "#F3FF33", "#8D33FF", "#FF8D33", "#33FF8D", "#8D33FF", "#FF5733", "#33FF57", "#3357FF", "#FF33A1", "#33FFF3", "#F3FF33", "#8D33FF", "#FF8D33"],
    alpha=0.8,
    legend='full'
)

bubble_chart.set_title("Impact of Various Health and Well-being Factors", fontsize=18, pad=20)
bubble_chart.set_xlabel("Value", fontsize=14)
bubble_chart.set_ylabel("Impact Score", fontsize=14)
bubble_chart.legend(loc='upper left', bbox_to_anchor=(1, 1), title="Impact Score")

plt.show()