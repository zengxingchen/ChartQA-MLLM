
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = [
    {'Topic': 'Mathematics', 'Online Courses': '25%', 'Workshops': '15%', 'Books': '20%', 'Conferences': '10%', 'Webinars': '20%', 'Research Papers': '10%'},
    {'Topic': 'Physics', 'Online Courses': '20%', 'Workshops': '20%', 'Books': '15%', 'Conferences': '15%', 'Webinars': '20%', 'Research Papers': '10%'},
    {'Topic': 'Chemistry', 'Online Courses': '15%', 'Workshops': '20%', 'Books': '25%', 'Conferences': '10%', 'Webinars': '15%', 'Research Papers': '15%'},
    {'Topic': 'Biology', 'Online Courses': '30%', 'Workshops': '10%', 'Books': '20%', 'Conferences': '10%', 'Webinars': '20%', 'Research Papers': '10%'},
    {'Topic': 'Computer Science', 'Online Courses': '35%', 'Workshops': '10%', 'Books': '15%', 'Conferences': '10%', 'Webinars': '20%', 'Research Papers': '10%'},
    {'Topic': 'Engineering', 'Online Courses': '20%', 'Workshops': '15%', 'Books': '20%', 'Conferences': '15%', 'Webinars': '20%', 'Research Papers': '10%'},
    {'Topic': 'Economics', 'Online Courses': '25%', 'Workshops': '15%', 'Books': '15%', 'Conferences': '10%', 'Webinars': '20%', 'Research Papers': '15%'},
    {'Topic': 'History', 'Online Courses': '15%', 'Workshops': '20%', 'Books': '25%', 'Conferences': '15%', 'Webinars': '15%', 'Research Papers': '10%'},
    {'Topic': 'Philosophy', 'Online Courses': '10%', 'Workshops': '25%', 'Books': '25%', 'Conferences': '10%', 'Webinars': '20%', 'Research Papers': '10%'},
    {'Topic': 'Art', 'Online Courses': '20%', 'Workshops': '20%', 'Books': '20%', 'Conferences': '10%', 'Webinars': '20%', 'Research Papers': '10%'},
    {'Topic': 'Music', 'Online Courses': '30%', 'Workshops': '10%', 'Books': '20%', 'Conferences': '10%', 'Webinars': '20%', 'Research Papers': '10%'}
]

df = pd.DataFrame(data)
df = df.set_index('Topic')
df = df.applymap(lambda x: int(x.replace('%', '')))

cumulative_sum = df.cumsum(axis=1)

colors = ['#FF5733', '#33FFBD', '#FF33EC', '#3375FF', '#FF8F33', '#33FF57']

fig, ax = plt.subplots(figsize=(14, 10))

bottom = None

for column, color in zip(df.columns, colors):
    ax.bar(df.index, df[column], bottom=bottom, label=column, color=color, width=0.6)
    bottom = cumulative_sum[column]

ax.legend(title='Resources', bbox_to_anchor=(1.05, 1), loc='upper left')

ax.set_ylabel('Percentage')
ax.set_xlabel('Educational Topics')
ax.set_title('Resource Distribution Across Various Educational Topics', pad=20)

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()