
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import squarify

data = {
    'Type': ['Yoga Studios', 'Gyms and Fitness Centers', 'Sports Arenas', 'Outdoor Adventure Parks',
             'Swimming Pools', 'Cycling Paths', 'Hiking Trails', 'Climbing Gyms',
             'Martial Arts Dojos', 'Dance Studios', 'Tennis Courts', 'Golf Courses',
             'Basketball Courts', 'Running Tracks', 'Ski Resorts', 'Surfing Spots',
             'Baseball Fields', 'Soccer Fields', 'Cricket Grounds', 'Rugby Pitches',
             'Boxing Gyms', 'Skate Parks', 'Bowling Alleys', 'Archery Ranges',
             'Badminton Courts', 'Horseback Riding Trails', 'Parkour Parks', 'Gymnastics Centers',
             'Trampoline Parks', 'Diving Centers', 'Ice Skating Rinks'],
    'Emissions': [210, 250, 300, 220, 270, 230, 190, 240, 260, 280, 210, 220, 230, 240,
                  250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380,
                  390, 400, 410]
}

df = pd.DataFrame(data)

plt.figure(figsize=(18, 12))
colors = ["#4e79a7", "#f28e2b", "#e15759", "#76b7b2", "#59a14f", "#edc949", 
          "#af7aa1", "#ff9da7", "#9c755f", "#bab0ac", "#e377c2", "#f7b6d2",
          "#c5b0d5", "#ffbb78", "#8c564b", "#c49c94", "#1f77b4", "#aec7e8",
          "#98df8a", "#ff9896", "#9467bd", "#c7c7c7", "#dbdb8d", "#ffbb78",
          "#17becf", "#bcbd22", "#9edae5", "#d62728", "#2ca02c", "#ff9896",
          "#8c564b"]
squarify.plot(sizes=df['Emissions'], label=df['Type'], alpha=0.8, color=colors)
plt.title('Distribution of Sports & Fitness Facilities by Emissions in 2024', fontsize=16, fontweight='bold', pad=20)
plt.axis('off')
plt.show()