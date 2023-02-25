# data-science-test

## Predicting the S&P 500 Closing Prices
This project uses different models to predict the closing prices of the S&P 500 stock market index based on historical data. The models used include polynomial regression, Prophet, and ARIMA.

## Getting Started
To get started with this project, you will need to have Python 3 and the following Python libraries installed:

pandas
numpy
matplotlib
scikit-learn
fbprophet
pmdarima
plotly
Once you have these libraries installed, you can run the code in datawork.py to load the data, create the models, and generate the predictions.

## Files
spy.csv: The original data file containing the historical closing prices of the S&P 500 index. [Kaggle]https://www.kaggle.com/datasets/gkitchen/s-and-p-500-spy
spy2.csv: A new data file that includes the original data and the predicted closing prices.
datasetwork.py: The main Python script for this project that loads the data, creates the models, and generates the predictions.
README.md: This file that provides an overview of the project and instructions for getting started.
##Models
#### Polynomial Regression
This model uses a 2nd degree polynomial to fit the historical closing prices of the S&P 500 index and generates predictions for 8 years.

### Prophet
This model uses Facebook's Prophet library to fit the historical closing prices of the S&P 500 index and generates predictions for 8 years.

### ARIMA
This model uses the AutoRegressive Integrated Moving Average (ARIMA) method to fit the historical closing prices of the S&P 500 index and generates predictions for 8 years.

## Additional Features
The code also includes the ability to plot major events on the graph, such as the 2001 WTC attacks and other economic events.

### Interactive Plot
The code generates an interactive plot using Plotly that allows the user to hover over the graph to see the actual and predicted closing prices of the S&P 500 index.

## Conclusion
This project demonstrates the use of different models to predict the closing prices of the S&P 500 index based on historical data. The results show that the models are able to generate accurate predictions for a long-term period. The code also includes additional features such as the ability to plot major events on the graph and an interactive plot using Plotly.

# Disclaimer:
The information provided by this program is for general informational purposes only. The program and its creators make no representations or warranties of any kind, express or implied, about the completeness, accuracy, reliability, suitability, or availability of the program or the information contained therein. Any reliance you place on such information is strictly at your own risk. In no event will the program or its creators be liable for any loss or damage including without limitation, indirect or consequential loss or damage, or any loss or damage whatsoever arising from loss of data or profits arising out of, or in connection with, the use of this program. This program does not constitute financial, investment, or trading advice, and should not be relied upon as such. Any investment decisions made based on the predictions provided by this program are made at your own risk.



