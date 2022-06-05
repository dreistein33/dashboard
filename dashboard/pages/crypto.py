import streamlit as st
from pycoingecko import CoinGeckoAPI
import time

st.set_page_config(page_title='CRYPTO', layout='wide', page_icon=':moneybag:')
client = CoinGeckoAPI()
crypto_names = ['bitcoin', 'ethereum', 'tron']


pipi = st.empty()


def get_tick(symbol):
    crypto_dict = {}
    for items in crypto_names:
        crypto_dict[items] = client.get_price(ids=items, vs_currencies=symbol)[items][symbol]

    return crypto_dict

while True:
    usd = get_tick('usd')
    time.sleep(5)
    pln = get_tick('pln')
    time.sleep(5)
    btc = get_tick('btc')
    time.sleep(5)
    sats = get_tick('sats')
    time.sleep(5)
    with pipi.container():
        fst, scd, thd, fth, ffth, sxth =  st.columns([1, 1, 1, 1, 1, 1])

        fst.header('USD')
        for key, val in usd.items():
            fst.metric(key.upper(), value=f'{val} USD', delta=None)

        scd.header('USDT')
        for key, val in usd.items():
            scd.metric(key.upper(), value=f'{val} USDT', delta=None)

        thd.header('USDC')
        for key, val in usd.items():
            thd.metric(key.upper(), value=f'{val} USDC', delta=None)

        fth.header('PLN')
        for key, val in pln.items():
            fth.metric(key.upper(), value=f'{val} PLN', delta=None)

        ffth.header('BTC')
        for key, val in btc.items():
            ffth.metric(key.upper(), value=f'{val} BTC', delta=None)

        sxth.header('SATOSHI')
        for key, val in sats.items():
            sxth.metric(key.upper(), value=f'{val} SATO', delta=None)

    time.sleep(90)
    pipi.empty()
