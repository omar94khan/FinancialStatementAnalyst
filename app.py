import yfinance as yf
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import sklearn as sk
import requests
import os
import time
import streamlit as st

tic_list = pd.read_csv('./LOV.csv')

def pretty(df : pd.DataFrame()):
    df = df.iloc[::-1]
    df.columns = pd.to_datetime(df.columns).strftime('%Y %B')
    return df


def main():
    st.header('Financial Statement Analyst', divider = True)

    st.write("Welcome to the Financial Statement Analyst. Where all the information you need is at your fingertips! \n\n")
    st.write("Please select your stock of choice.")
    selection = st.selectbox(label="", options = list(tic_list['List Name']), label_visibility="collapsed")
    if selection:
        tic = tic_list.set_index('List Name').loc[selection][0]

    statement = st.selectbox(label="Select your Financial Statement", options = ['Income Statement', 'Balance Sheet', 'Cash Flow Statement'])

    if st.button(label = 'Generate'):
        if statement == 'Income Statement':
            df = yf.Ticker(tic).get_financials(pretty = True)
            df = pretty(df)
            st.write(df)
        elif statement == 'Balance Sheet':
            df = yf.Ticker(tic).get_balance_sheet(pretty = True)
            df = pretty(df)
            st.write(df)
        elif statement == 'Cash Flow Statement':
            df = yf.Ticker(tic).get_cash_flow(pretty= True)
            df = pretty(df)
            st.write(df)
            
main()