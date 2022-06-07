import streamlit as st
import pandas as pd

class TaxCalculator(object):

    def __init__(self, file):
        self.file = pd.read_csv(file, sep=';')
        self.only_usd = self.file[self.file['Rynek'].str.contains('PLN')]

    def calculate_costs(self):
        buy_col = (self.only_usd.loc[self.only_usd['Rodzaj'] == 'Kupno'])
        cost = buy_col['Wartość'].str.replace(',', '.').astype(float).sum()
        return cost

    def calculate_income(self):
        sell_col = (self.only_usd.loc[self.only_usd['Rodzaj'] == 'Sprzedaż'])
        income = sell_col['Wartość'].str.replace(',', '.').astype(float).sum()
        return income

    def calculate_profit(self):
        profit = self.calculate_income() - self.calculate_costs()
        return float(profit)

    def calculate_tax(self):
        tax = 0.19 * self.calculate_profit()
        return float(tax)

    def return_profit_and_tax(self):
        costs = round(self.calculate_costs(), 2)
        income = round(self.calculate_income(), 2)
        round_profit = round(self.calculate_profit(), 2)
        round_tax = round(self.calculate_tax(), 2)
        profit_minus_tax = round_profit - round_tax

        return costs, income, round_profit, round_tax, profit_minus_tax

st.set_page_config(page_title='TAXES', page_icon=':heavy_multiplication_x:')

uploaded_file = st.file_uploader('Choose a file')

if uploaded_file is not None:
    dataframe = TaxCalculator(uploaded_file)
    cash_values = dataframe.return_profit_and_tax()
    st.metric(label='KOSZT', value=f'{cash_values[0]} PLN')
    st.metric(label='SPRZEDAZ', value=f'{cash_values[1]} PLN')

    if cash_values[2] < 0:
        st.metric(label='POZOSTALO DO PROFITU', value=f'{cash_values[2]} PLN')
    else:
        st.metric(label='PROFIT' value=f'{cash_values[2]} PLN')
         st.metric(label='PODATEK' value=f'{cash_values[3]} PLN')
         st.metric(label='PROFIT NETTO' value=f'{cash_values[4]} PLN')
