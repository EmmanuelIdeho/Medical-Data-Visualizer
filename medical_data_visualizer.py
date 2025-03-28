import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv')

# 2
df['overweight'] = np.where(df['weight'] / (df['height'] / 100) ** 2 > 25, 1, 0)

# 3
#df.loc[df['overweight'] <= 25, 'overweight'] = 0
#df.loc[df['overweight'] > 25, 'overweight'] = 1

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
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')
    

    # 7
    fig = sns.catplot(
    x="variable",          # Categorical features on x-axis
    y = "total",
    hue="value",           # 0 or 1 category (binary features)
    col="cardio",          # Split by cardio
    data=df_cat,           # Use the grouped DataFrame
    kind="bar",            # Use bar chart
    height=5,              # Set height of the plot
    aspect=1             # Control the aspect ratio)
    )


    # 8
    plt.show()


    # 9
    fig.figure.savefig('catplot.png')
    plt.close(fig.figure)
    return fig.figure


# 10
def draw_heat_map():
    # 11
    df_heat = df.loc[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
        ]

    # 12
    corr = df_heat.corr()

    # 13
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # 14
    fig, ax = plt.subplots(figsize=(12, 8))

    # 15
    sns.heatmap(
    corr,               # Correlation matrix data
    annot=True,                 # Display correlation values
    cmap="RdBu_r",            # Color scheme
    fmt=".1f",                  # Format for correlation values (1 decimal place)
    linewidths=0.5,             # Line width between cells
    cbar=True,                  # Show color bar
    square=True,                # The heatmap should not be a square
    mask=mask,                  # Apply the upper triangle mask
    ax=ax,                      # Use the correct axis
    vmin=-0.08,                 # Color range minimum
    vmax=0.24                   # Color range maximum
    )
    plt.show()




    # 16
    fig.savefig('heatmap.png')
    plt.close(fig)
    return fig
