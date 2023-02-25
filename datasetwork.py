import pandas as pd
import numpy as np
import plotly.graph_objects as go
from prophet import Prophet

# Load the data
df = pd.read_csv('spy.csv')
df['Date'] = pd.to_datetime(df['Date'])

# Create a Prophet model
model = Prophet()
model.fit(df[['Date', 'Close']].rename(columns={'Date': 'ds', 'Close': 'y'}))

# Make future predictions
future = model.make_future_dataframe(periods=365*8, freq='D')

# Make interval predictions
forecast = model.predict(future)
forecast['yhat_upper'] = forecast['yhat_upper'] - df['Close'].mean()
forecast['yhat_lower'] = forecast['yhat_lower'] - df['Close'].mean()

# Create annotations for the events
events = [
    dict(x='2001-09-11', y=df['Close'].max(), text='September 11 Attacks', showarrow=True, arrowhead=1, ax=0, ay=-40),
    dict(x='2008-09-15', y=df['Close'].max(), text='Lehman Brothers Bankruptcy', showarrow=True, arrowhead=1, ax=0, ay=-40),
    dict(x='2020-02-20', y=df['Close'].max(), text='COVID-19 Pandemic', showarrow=True, arrowhead=1, ax=0, ay=-40),
    dict(x='2021-11-01', y=df['Close'].max(), text='Some Future Event', showarrow=True, arrowhead=1, ax=0, ay=-40)
]

# Plot the predictions
fig = go.Figure()
fig.add_trace(go.Scatter(x=df['Date'], y=df['Close'], name='Actual'))
fig.add_trace(go.Scatter(x=forecast['ds'], y=forecast['yhat'], name='Prediction'))
fig.add_trace(go.Scatter(x=forecast['ds'], y=forecast['yhat_upper'], name='Upper Bound', line=dict(width=0), mode='lines', fillcolor='rgba(0,100,80,0.2)', fill='tonexty'))
fig.add_trace(go.Scatter(x=forecast['ds'], y=forecast['yhat_lower'], name='Lower Bound', line=dict(width=0), mode='lines', fillcolor='rgba(0,100,80,0.2)', fill='tonexty'))

# Add dots for the interval predictions
for i in range(0, len(forecast), 180):
    interval_data = forecast.iloc[i:i+180]
    fig.add_trace(go.Scatter(x=interval_data['ds'], y=interval_data['yhat'], name=f'Interval Prediction {i//180+1}', mode='markers', marker=dict(size=5)))

# Add annotations for the events
for event in events:
    fig.add_annotation(event)

# Update the layout
fig.update_layout(title='S&P 500 Closing Prices (Interactive)',
                  xaxis_title='Year',
                  yaxis_title='Closing Price',
                  hovermode='x unified')

# Show the plot
fig.show()
