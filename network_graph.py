import plotly.graph_objects as go

# Sample data for network nodes and edges
nodes = ['URL1', 'Advertising', 'Email Sharing', 'URL2', 'Cookies']
edges = [('URL1', 'Advertising'), ('URL1', 'Email Sharing'), ('URL2', 'Cookies')]

# Create node and edge trace
node_trace = go.Scatter(
    x=[0, 1, 2, 1, 0],
    y=[1, 2, 1, 0, 1],
    mode='markers+text',
    marker=dict(size=20),
    text=nodes
)
edge_trace = go.Scatter(
    x=[0, 1, 1, 1, 1, 2],
    y=[1, 2, 1, 1, 0, 1],
    line=dict(width=0.5, color='#888'),
    hoverinfo='none',
    mode='lines'
)

# Create figure
fig = go.Figure(data=[edge_trace, node_trace],
                layout=go.Layout(
                    title='Network Graph of Label Conflicts',
                    showlegend=False))
fig.show()
