import json
import openai
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import yfinance as yf

open.api_key = open('API_KEY','r').read()

def get_stock_price()