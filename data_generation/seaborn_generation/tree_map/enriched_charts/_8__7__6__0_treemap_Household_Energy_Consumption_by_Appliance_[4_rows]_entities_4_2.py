
import matplotlib.pyplot as plt
import pandas as pd
import squarify

data = {
    "Field": ["Fitness", "Running", "Yoga", "Weightlifting", "CrossFit", "Cardio", 
              "Pilates", "Martial Arts", "Cycling", "Swimming", "Hiking", "Dancing", 
              "Aerobics", "Bodybuilding", "Boxing", "Climbing", "Football", "Basketball", 
              "Tennis", "Golf", "Baseball", "Soccer", "Rugby", "Volleyball", "Cricket", 
              "Hockey", "Skiing", "Snowboarding", "Surfing", "Skateboarding", "Rowing", 
              "Badminton", "Table Tennis", "Squash", "Fencing", "Archery", "Diving", 
              "Horse Riding", "Ballet"],
    "Amount": [140, 125, 135, 130, 120, 115, 110, 105, 100, 95, 90, 85, 80, 75, 70, 
               65, 60, 55, 50, 45, 40, 35, 30, 25, 20, 15, 10, 5, 8, 12, 18, 22, 26, 
               30, 34, 38, 42, 46, 50]
}

df = pd.DataFrame(data)

color_mapper = {
    'Fitness': '#FF5733', 'Running': '#33FF57', 'Yoga': '#3357FF', 'Weightlifting': '#FF33A1', 
    'CrossFit': '#F3FF33', 'Cardio': '#33FFF6', 'Pilates': '#FF8A33', 'Martial Arts': '#8A33FF', 
    'Cycling': '#57FF33', 'Swimming': '#3357FF', 'Hiking': '#33FFF6', 'Dancing': '#FF333A', 
    'Aerobics': '#8A33FF', 'Bodybuilding': '#FF33A1', 'Boxing': '#57FF33', 'Climbing': '#FF5733', 
    'Football': '#33FF57', 'Basketball': '#3357FF', 'Tennis': '#FF33A1', 'Golf': '#F3FF33', 
    'Baseball': '#33FFF6', 'Soccer': '#FF8A33', 'Rugby': '#8A33FF', 'Volleyball': '#57FF33', 
    'Cricket': '#3357FF', 'Hockey': '#33FFF6', 'Skiing': '#FF333A', 'Snowboarding': '#8A33FF', 
    'Surfing': '#FF33A1', 'Skateboarding': '#57FF33', 'Rowing': '#FF5733', 'Badminton': '#33FF57', 
    'Table Tennis': '#3357FF', 'Squash': '#FF33A1', 'Fencing': '#F3FF33', 'Archery': '#33FFF6', 
    'Diving': '#FF8A33', 'Horse Riding': '#8A33FF', 'Ballet': '#57FF33'
}

colors = [color_mapper[field] for field in df['Field']]

fig, ax = plt.subplots(1, figsize=(20, 14))

squarify.plot(sizes=df['Amount'], label=df['Field'], color=colors, alpha=0.8, text_kwargs={'fontsize':9})

plt.title('Sports & Fitness Activities Distribution (Number of Participants)', fontsize=18, pad=20)
plt.axis('off')
plt.show()