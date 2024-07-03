
import matplotlib.pyplot as plt
import pandas as pd
import squarify

data = {
    'Category': ['Mental Health Services', 'Fitness Programs', 'Nutritional Counseling', 'Stress Management Workshops', 'Sleep Clinics',
                 'Rehabilitation Centers', 'Community Health Initiatives', 'Telehealth Services', 'Medical Research', 'Pharmaceutical Innovations',
                 'Yoga & Meditation', 'Preventive Screenings', 'Health Education', 'Dental Care', 
                 'Home Healthcare', 'Pediatric Care', 'Geriatric Services', 'Public Health Campaigns', 'Mobile Health Clinics', 'Health Apps',
                 'Alternative Medicine', 'Employee Wellness Programs', 'Substance Abuse Programs', 'Immunization Drives', 'First Aid Training',
                 'Healthcare Technology', 'Disease Control', 'Emergency Response', 'Fitness Tracking', 'Genetic Research'],
    'Value': [1500000, 900000, 700000, 400000, 2300000,
              800000, 650000, 500000, 300000, 750000,
              1200000, 450000, 850000, 950000, 
              600000, 200000, 100000, 700000, 300000, 400000,
              1100000, 950000, 1250000, 850000, 450000,
              2000000, 900000, 3000000, 1700000, 1400000]
}

df = pd.DataFrame(data)

plt.figure(figsize=(18,14))

colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#57FF33',
          '#5733FF', '#FF5733', '#33FF57', '#3357FF', '#FF33A1',
          '#57FF33', '#5733FF', '#FF5733', '#33FF57', '#3357FF',
          '#FF33A1', '#57FF33', '#5733FF', '#FF5733', '#33FF57',
          '#3357FF', '#FF33A1', '#57FF33', '#5733FF', '#FF5733',
          '#33FF57', '#3357FF', '#FF33A1', '#57FF33', '#5733FF']

squarify.plot(sizes=df['Value'], label=df['Category'], color=colors, alpha=0.8)

plt.title('Resource Allocation in Health & Psychology', fontsize=24)

plt.axis('off')

plt.show()