import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv')

# 2
df['overweight'] = df['weight'] / (df['height']**2)

# 3
df.loc[df['overweight'] <= 25, 'overweight'] = 0
df.loc[df['overweight'] > 25, 'overweight'] = 1

df.loc[df['cholesterol'] == 1, 'cholesterol'] = 0
df.loc[df['cholesterol'] > 1, 'cholesterol'] = 1
df.loc[df['gluc'] == 1, 'gluc'] = 0
df.loc[df['gluc'] > 1, 'gluc'] = 1


# 4
def draw_cat_plot():
    # 5
    df_cat = pd.melt(df, id_vars=["cardio"], 
    value_vars=["cholesterol","gluc","smoke","alco","active","overweight"],
     var_name="variable",
      value_name="value")


    # 6
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='count')
    

    # 7
    fig = sns.catplot(x="variable",          # Categorical features on x-axis
    hue="value",           # 0 or 1 category (binary features)
    col="cardio",          # Split by cardio
    data=df_cat,           # Use the grouped DataFrame
    kind="bar",            # Use bar chart
    height=5,              # Set height of the plot
    aspect=1.2             # Control the aspect ratio)
    )


    # 8
    plt.show()


    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = None

    # 12
    corr = None

    # 13
    mask = None



    # 14
    fig, ax = None

    # 15



    # 16
    fig.savefig('heatmap.png')
    return fig
