
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {
    'Day': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
            16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
    'StarsSighted': [2, 3, 4, 2, 5, 6, 7, 3, 8, 9, 10, 4, 11, 12, 13,
                     5, 14, 15, 16, 6, 17, 18, 19, 7, 20, 21, 22, 8, 23, 24],
    'HoursObserved': [1.5, 2.0, 2.5, 1.0, 3.0, 3.5, 4.0, 2.2, 4.5, 5.0, 5.5, 2.8, 6.0, 6.5, 7.0,
                      3.5, 7.5, 8.0, 8.5, 4.0, 9.0, 9.5, 10.0, 4.5, 10.5, 11.0, 11.5, 5.0, 12.0, 12.5]
}

df = pd.DataFrame(data)

# Plot
plt.figure(figsize=(16, 10))
scatterplot = sns.scatterplot(x='StarsSighted', y='HoursObserved',
                              data=df, palette=['#3498DB', '#E74C3C'])

scatterplot.set_title('Relationship Between Stars Sighted and Hours Observed', fontsize=18)
scatterplot.set_xlabel('Number of Stars Sighted', fontsize=14)
scatterplot.set_ylabel('Hours Spent Observing', fontsize=14)

plt.show()