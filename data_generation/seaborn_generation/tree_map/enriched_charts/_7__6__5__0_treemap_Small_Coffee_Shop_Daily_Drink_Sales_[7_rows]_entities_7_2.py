
import pandas as pd
import matplotlib.pyplot as plt
import squarify

data = {
    'Category': [
        'Ethics', 'Epistemology', 'Metaphysics', 'Aesthetics', 'Logic',
        'Political Philosophy', 'Philosophy of Mind', 'Philosophy of Science',
        'Existentialism', 'Phenomenology', 'Analytic Philosophy',
        'Continental Philosophy', 'Stoicism', 'Hedonism', 'Nihilism',
        'Utilitarianism', 'Deontology', 'Virtue Ethics', 'Bioethics', 'Environmental Ethics'
    ],
    'Values': [
        180, 200, 190, 160, 170,
        185, 175, 195, 155, 145,
        165, 135, 125, 115, 105,
        95, 85, 75, 65, 155
    ]
}

df = pd.DataFrame(data)

colors = [
    '#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#A133FF',
    '#FFBD33', '#33FFBD', '#BD33FF', '#FF3333', '#33FF33',
    '#FF33FF', '#3333FF', '#A1FF33', '#33A1FF', '#A133FF',
    '#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#A133FF'
]

fig, ax = plt.subplots(1, figsize=(20, 15))

squarify.plot(sizes=df['Values'], label=df['Category'], alpha=0.8, color=colors)

plt.axis('off')

plt.title('Philosophy Topics and Their Importance', fontsize=24, pad=20)

plt.show()