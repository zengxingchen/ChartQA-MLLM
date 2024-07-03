
import matplotlib.pyplot as plt
import pandas as pd

data = {
    "Topic": ["Philosophy", "Ethics", "Logic", "Aesthetics", "Metaphysics", "Epistemology", 
              "Political Philosophy", "Philosophy of Mind", "Philosophy of Language", 
              "Philosophy of Science", "Ancient Philosophy", "Medieval Philosophy", 
              "Modern Philosophy", "Contemporary Philosophy", "Phenomenology", "Existentialism", 
              "Pragmatism", "Structuralism", "Post-Structuralism", "Analytic Philosophy", 
              "Continental Philosophy", "Eastern Philosophy", "African Philosophy", 
              "Latin American Philosophy", "Feminist Philosophy", "Environmental Philosophy", 
              "Philosophy of Religion", "Philosophy of Technology", "Philosophy of Mathematics", 
              "Philosophy of Art", "Philosophy of Literature", "Philosophy of History", 
              "Philosophy of Education", "Philosophy of Law", "Philosophy of Music", "Philosophy of Sport"],
    "Expenditure (Million USD)": [320, 280, 450, 150, 200, 370, 310, 220, 180, 400, 140, 170, 250, 300, 
                                  230, 210, 190, 160, 120, 270, 290, 310, 220, 200, 180, 260, 330, 
                                  340, 230, 180, 150, 140, 210, 290, 240, 200]
}

df = pd.DataFrame(data)

fig, ax = plt.subplots(figsize=(16, 10))

ax.fill_between(df['Topic'], df['Expenditure (Million USD)'], color='#ff7f0e', alpha=0.7)

ax.set_title('Annual Expenditure on Different Philosophical Fields', fontsize=20, pad=20)
ax.set_xlabel('Philosophical Fields', fontsize=15)
ax.set_ylabel('Expenditure (Million USD)', fontsize=15)

for i, txt in enumerate(df['Expenditure (Million USD)']):
    ax.annotate(txt, (df['Topic'][i], df['Expenditure (Million USD)'][i]), textcoords="offset points", xytext=(0,5), ha='center')

plt.xticks(rotation=90)
plt.tight_layout()
plt.show()