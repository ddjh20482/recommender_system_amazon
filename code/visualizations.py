
# visualization packages
import matplotlib.pyplot as plt
from matplotlib.axes._axes import _log as matplotlib_axes_logger
from matplotlib.ticker import FuncFormatter

# Standard data manipulation packages
import pandas as pd
import numpy as np


def result_1(review_dist):
    
    fig, ax = plt.subplots(figsize=(7,8))
    plt.rcParams.update({'font.size': 15})
    ax.bar(review_dist.review_rating, 
           review_dist.percentage, 
           color = ['tab:blue', 'tab:blue', 'tab:blue', 'tab:blue', 'tab:red'])
    for i, v in enumerate(review_dist.percentage):
        ax.text(i + 0.75, v + 0.005, str(round(v, 2)), color='blue', fontweight='bold', fontsize = 15)
    ax.yaxis.set_major_formatter('{x:.0%}')
    ax.set_ylim(0, review_dist.percentage.max() + 0.05)
    ax.set_title("Rating Distribution", fontsize=30)
    plt.xlabel('Ratings')
    plt.xticks(fontsize= 13)
    plt.yticks(fontsize= 13)
    plt.show()
    
    pass

def result_2(list_5):
    
    fig, ax = plt.subplots(figsize=(10, 10))

    ax.scatter(list_5.user[list_5.p_value <= 0.05], 
               list_5.p_value[list_5.p_value <= 0.05], 
               color = 'tab:red')
    ax.scatter(list_5.user[list_5.p_value > 0.05], 
               list_5.p_value[list_5.p_value > 0.05], 
               color = 'silver')

    ax.set_title("P-value Distribution", fontsize=30)
    plt.xlim([0, 100])
    plt.xlabel('Customers with the number of Items Rated')
    plt.ylabel('P-values')
    plt.show()
    
    pass

def result_3(data):
    
    fig, ax = plt.subplots(figsize=(8, 8))

    ax.hist(data, bins='auto')
    ax.set_title("Distribution of Expected Rating on One Customer", fontsize=20);
    
    pass