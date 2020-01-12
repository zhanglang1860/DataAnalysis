import plotly.io as pio
import plotly.graph_objects as go
import pandas as pd
import chart_studio.plotly as py
import chart_studio

chart_studio.tools.set_credentials_file(
    username='zhanglang86',  # 这儿就不放我自己的账号和api了
    api_key='MxJLQuDBGkAVEZI7f2J0'
)
# df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')
df1 = pd.read_csv(r'D:\Python数据分析教程\day03\code\youtube_video_data\GBvideos.csv')

# import plotly.express as px
#
# df = df[df['comment_total'] < 5000]
# fig = px.histogram(df, x="comment_total")
#
# fig.show()
# py.plot(fig, filename='pandas-multiple-scatter')


import plotly.graph_objects as go

# df = df[[df['likes'] < 10000] and [df['category_id'] < 5]]
df = df1[(df1['likes'] < 10000) & (df1['category_id'] > 20)]
print(df.head(5))
fig = go.Figure()
fig.add_trace(go.Scatter(
    x=df['likes'],
    y=df['dislikes'],
    name='likes-dislikes',
    # marker={'color': 'red',
    #         # 'symbol': 104,
    #         # 'size': 10
    #         },
    mode='markers',
    # xbins=dict(
    #     start=-3.0,
    #     end=4,
    #     size=0.5
    # ),
    marker={'color': df['category_id']}
    # fillcolor='#330C73',
    # opacity=0.75
))
fig.update_layout(
    title_text='Sampled Results',  # title of plot
    xaxis_title_text='Value',  # xaxis label
    yaxis_title_text='Count',  # yaxis label
    bargap=0.2,  # gap between bars of adjacent location coordinates
    bargroupgap=0.1  # gap between bars of the same location coordinates
)

fig.show()

# py.plot(fig, filename='pandas-multiple-scatter')
