
import matplotlib.pyplot as plt

years = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025]
reading_scores = [68.0, 67.5, 67.8, 67.2, 66.9, 66.5, 66.2, 65.8, 65.5, 65.1, 64.7, 64.4, 64.1, 63.7, 63.4, 63.0]

fig, ax = plt.subplots(figsize=(14, 8))

ax.plot(years, reading_scores, color='#ff5733', marker='o', linewidth=2)

ax.set_title('Average Reading Scores Over Time', fontsize=18)
ax.set_xlabel('Year', fontsize=16)
ax.set_ylabel('Reading Score', fontsize=16)

for year, score in zip(years, reading_scores):
    ax.annotate(f'{score}', xy=(year, score), textcoords="offset points", xytext=(0,10), ha='center')

plt.grid(True)
plt.show()