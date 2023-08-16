import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    plt.scatter(x=df['Year'], y=df['CSIRO Adjusted Sea Level'])
    plt.xlim([1850, 2075])

    # Create first line of best fit
    slope, intercept, r, p, se = linregress(x=df['Year'], y=df['CSIRO Adjusted Sea Level'])
    xBesterman = np.arange(df['Year'].min(), 2051, 1)
    yBesterman = xBesterman*slope + intercept
    plt.plot(xBesterman, yBesterman)
  
    # Create second line of best fit
    slope, intercept, r, p, se = linregress(x=df['Year'].loc[df['Year'] >= 2000] , y=df['CSIRO Adjusted Sea Level'].loc[df['Year'] >= 2000])
    xBesterwoman = np.arange(2000, 2051, 1)
    yBesterwoman = xBesterwoman * slope + intercept
    plt.plot(xBesterwoman, yBesterwoman)

    # Add labels and title
    plt.title("Rise in Sea Level")
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()