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

def get_stable(symbol, vs_symbol):
    price = client.get_price(ids=symbol, vs_currencies=vs_symbol)[symbol][vs_symbol]

    return 1 / price


while True:
    usd = get_tick('usd')
    pln = get_tick('pln')
    btc = get_tick('btc')
    sats = get_tick('sats')
    with pipi.container():
        fst, scd, thd, fth, ffth, sxth =  st.columns([1, 1, 1, 1, 1, 1])

        fst.header('USD')
        for key, val in usd.items():
            fst.metric(key.upper(), value=f'{val}', delta=None)

        scd.header('USDT')
        usdtbtc = get_stable('tether', 'btc')
        usdtether = get_stable('tether', 'eth')
        scd.metric('BITCOIN', value = f'{usdtbtc:.2f}', delta=None)
        scd.metric('ETHEREUM', value = f'{usdtether:.2f}', delta=None)

        thd.header('USDC')
        usdcbtc = get_stable('usd-coin', 'btc')
        usdcether = get_stable('usd-coin', 'eth')
        thd.metric('BITCOIN', value = f'{usdcbtc:.2f}', delta=None)
        thd.metric('BITCOIN', value = f'{usdcether:.2f}', delta=None)

        fth.header('PLN')
        for key, val in pln.items():
            fth.metric(key.upper(), value=f'{val}', delta=None)

        ffth.header('BTC')
        for key, val in btc.items():
            if key != 'bitcoin':
                ffth.metric(key.upper(), value=f'{val}', delta=None)

        sxth.header('SATOSHI')
        for key, val in sats.items():
            if key != 'bitcoin':
                sxth.metric(key.upper(), value=f'{val}', delta=None)

    time.sleep(30)
    pipi.empty()
