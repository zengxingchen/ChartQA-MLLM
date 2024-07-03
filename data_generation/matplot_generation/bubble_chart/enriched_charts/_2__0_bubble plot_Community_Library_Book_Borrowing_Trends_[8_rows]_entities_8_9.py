
import matplotlib.pyplot as plt

data = {
    'Category': ["Yoga", "Pilates", "Running", "Cycling", "Swimming", "Weightlifting", "Hiking", "Dancing",
                 "Boxing", "CrossFit", "Tennis", "Basketball", "Football", "Martial Arts", "Rock Climbing",
                 "Golf", "Table Tennis", "Volleyball", "Horseback Riding", "Skating"],
    'Number of Participants': [150, 100, 200, 180, 120, 80, 140, 110, 60, 90, 50, 130, 160, 70, 40, 30, 20, 45, 35, 55],
    'Average Score': [85, 88, 75, 82, 90, 70, 83, 87, 65, 77, 80, 73, 79, 84, 92, 66, 78, 74, 81, 69],
    'Duration of Participation (months)': [24, 18, 36, 30, 20, 15, 22, 25, 12, 19, 14, 28, 33, 16, 13, 9, 8, 10, 17, 11]
}

size = [value * 2 for value in data['Number of Participants']]

plt.figure(figsize=(16, 10))

scatter = plt.scatter(data['Average Score'], data['Duration of Participation (months)'],
                      s=size, alpha=0.6, 
                      c=['#FF9999', '#66B2FF', '#99FF99', '#FFCC99', '#FF99CC', '#66FFB2', '#B266FF',
                         '#FF66B2', '#B2FF66', '#99B2FF', '#FFB266', '#66CCFF', '#FF66CC', '#B2CC66',
                         '#CC66FF', '#66FFCC', '#CC99FF', '#FF6666', '#66FF99', '#FF99B2'])

plt.title('Fitness Activity Participation and Performance', pad=20)
plt.xlabel('Average Score')
plt.ylabel('Duration of Participation (months)')

for index, category in enumerate(data['Category']):
    plt.text(data['Average Score'][index], data['Duration of Participation (months)'][index],
             category, fontsize=9, ha='center', va='center')

plt.grid(True)
plt.show()