import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# Load the data
data = pd.read_csv('spy.csv')
data['Date'] = pd.to_datetime(data['Date'])

# Split the data into training and testing sets
train_data = data[data['Date'] < '2019-01-01']
test_data = data[data['Date'] >= '2019-01-01']

# Add a Days column to the training data
train_data['Days'] = (train_data['Date'] - train_data['Date'].iloc[0]).dt.days

# Fit a 2nd degree polynomial to the training data
poly_model = np.polyfit(train_data['Days'], train_data['Close'], deg=2)

# Generate predicted prices
days_in_8_years = 365 * 8
n_intervals = 16  # Number of 6-month intervals to predict in 8 years
last_date = data['Date'].iloc[-1]
predicted_days = pd.date_range(start=last_date, periods=n_intervals+1, freq='6M')[1:]
predicted_days = (predicted_days - predicted_days.min()) + last_date
predicted_prices = np.polyval(poly_model, (predicted_days - last_date).days.values)

# Create a line chart of the predicted prices
fig = go.Figure()

# Add the actual closing prices
fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], mode='lines', name='Actual'))

# Add the predicted closing prices
fig.add_trace(go.Scatter(x=predicted_days, y=predicted_prices, mode='lines', name='Predicted'))

# Set the title and axes labels
fig.update_layout(title='Predicted Prices of the S&P 500',
                  xaxis_title='Year',
                  yaxis_title='Closing Price')

# Show the plot
fig.show()
