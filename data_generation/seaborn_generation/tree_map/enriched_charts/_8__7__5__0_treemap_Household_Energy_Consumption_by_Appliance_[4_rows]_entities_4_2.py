
import matplotlib.pyplot as plt
import pandas as pd
import squarify

data = {
    "Category": ["Mental Health Services", "Mental Health Services", "Mental Health Services",
                 "Nutrition Counseling", "Nutrition Counseling", "Nutrition Counseling",
                 "Physical Therapy", "Physical Therapy", "Physical Therapy",
                 "Wellness Coaching", "Wellness Coaching", "Wellness Coaching",
                 "Fitness Programs", "Fitness Programs", "Fitness Programs",
                 "Alternative Medicine", "Alternative Medicine", "Alternative Medicine",
                 "Sleep Science", "Sleep Science", "Sleep Science"],
    "Subcategory": ["Teletherapy", "In-person Counseling", "Mindfulness Workshops",
                    "Weight Management", "Diet Planning", "Sports Nutrition",
                    "Rehabilitation", "Occupational Therapy", "Chiropractic Services",
                    "Life Coaching", "Stress Management", "Habit Formation",
                    "Gym Memberships", "Online Fitness Classes", "Personal Training",
                    "Acupuncture", "Herbal Medicine", "Homeopathy",
                    "Insomnia Treatments", "Sleep Apnea Solutions", "Sleep Studies"],
    "Value": [200000, 300000, 150000,
              180000, 240000, 220000,
              400000, 300000, 250000,
              270000, 200000, 230000,
              500000, 320000, 420000,
              180000, 160000, 140000,
              190000, 210000, 170000]
}

df = pd.DataFrame(data)

color_mapper = {
    'Mental Health Services': '#FF6F61',
    'Nutrition Counseling': '#6B5B95',
    'Physical Therapy': '#88B04B',
    'Wellness Coaching': '#F7CAC9',
    'Fitness Programs': '#92A8D1',
    'Alternative Medicine': '#955251',
    'Sleep Science': '#B565A7'
}

colors = [color_mapper[category] for category in df['Category']]

fig, ax = plt.subplots(1, figsize=(18, 14))

squarify.plot(sizes=df['Value'], label=df['Subcategory'], color=colors, alpha=0.8, text_kwargs={'fontsize':10})

plt.title('Market Valuation of Health & Psychology Subcategories', fontsize=20, pad=20)
plt.axis('off')
plt.show()