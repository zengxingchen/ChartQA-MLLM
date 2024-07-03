
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'University': [
        'Harvard', 'Stanford', 'MIT', 'Cambridge', 'Oxford', 'Yale',
        'Columbia', 'Princeton', 'UChicago', 'UPenn', 'Caltech', 'Duke',
        'Johns Hopkins', 'Northwestern', 'UCLA', 'UC Berkeley', 'NYU',
        'Cornell', 'USC', 'Carnegie Mellon'
    ],
    'Student Enrollment': [
        21000, 16000, 11500, 23000, 24000, 13000,
        31000, 8000, 17000, 22000, 2200, 16000,
        27000, 21000, 45000, 42000, 53000, 23000,
        46000, 14000
    ],
    'Graduation Rate': [
        96, 94, 92, 95, 94, 93,
        92, 98, 93, 91, 97, 92,
        90, 91, 89, 88, 87, 93,
        90, 91
    ]
}

df = pd.DataFrame(data)

plt.figure(figsize=(18, 10))

sns.scatterplot(
    x='Student Enrollment', y='Graduation Rate',
    hue='University', palette=[
        '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
        '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf',
        '#393b79', '#637939', '#8c6d31', '#843c39', '#ad494a',
        '#d6616b', '#7b4173', '#a55194', '#ce6dbd', '#de9ed6'
    ],
    data=df,
    s=150
)

plt.xlabel('Student Enrollment')
plt.ylabel('Graduation Rate')
plt.title('Student Enrollment vs. Graduation Rates at Top Universities', pad=40)
plt.show()