
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Input data as a list of dictionaries
data = [
    {'Month': 'January', '6-12 Years': '20%', '13-18 Years': '25%', '19-35 Years': '35%', '36-50 Years': '10%', '51+ Years': '10%'},
    {'Month': 'February', '6-12 Years': '22%', '13-18 Years': '22%', '19-35 Years': '35%', '36-50 Years': '11%', '51+ Years': '10%'},
    {'Month': 'March', '6-12 Years': '18%', '13-18 Years': '30%', '19-35 Years': '30%', '36-50 Years': '12%', '51+ Years': '10%'},
    {'Month': 'April', '6-12 Years': '15%', '13-18 Years': '25%', '19-35 Years': '40%', '36-50 Years': '10%', '51+ Years': '10%'},
    {'Month': 'May', '6-12 Years': '20%', '13-18 Years': '20%', '19-35 Years': '30%', '36-50 Years': '15%', '51+ Years': '15%'},
    {'Month': 'June', '6-12 Years': '25%', '13-18 Years': '15%', '19-35 Years': '30%', '36-50 Years': '20%', '51+ Years': '10%'},
    {'Month': 'July', '6-12 Years': '30%', '13-18 Years': '20%', '19-35 Years': '25%', '36-50 Years': '15%', '51+ Years': '10%'},
    {'Month': 'August', '6-12 Years': '35%', '13-18 Years': '18%', '19-35 Years': '27%', '36-50 Years': '10%', '51+ Years': '10%'}
]

# Transform to dataframe and replace percentage strings with floats
df = pd.DataFrame(data)
for col in df.columns[1:]:
    df[col] = df[col].str.rstrip('%').astype('float') / 100

# Melt the dataframe to long form to work with seaborn
df_long = df.melt(id_vars='Month', var_name='Age Group', value_name='Percentage')

# Pivot the data for stacked bars
pivot_df = df_long.pivot(index='Month', columns='Age Group', values='Percentage')

# Plot the 100% stacked bar chart using seaborn
colors = sns.color_palette("cubehelix", len(df.columns) - 1)  # Colormap for distinction
pivot_df.plot(kind='bar', stacked=True, color=colors, figsize=(10, 7))

# Beautify the plot
plt.title('Monthly Age Group Distribution in 100% Stacked Bar Chart')
plt.xlabel('Month')
plt.ylabel('Percentage')
plt.legend(title='Age Group', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()