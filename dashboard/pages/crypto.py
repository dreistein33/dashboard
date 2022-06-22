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


def calculate_difference(old_data, new_data):
    differences = {'bitcoin': 0, 'ethereum': 0, 'tron': 0}
    sharedKeys = {'bitcoin', 'ethereum', 'tron'}
    for key in sharedKeys:
        if old_data[key] != new_data[key]:
            differences[key] = new_data[key] - old_data[key]

    return differences


HUSD = {'bitcoin': 0, 'ethereum': 0, 'tron': 0}
HPLN = {'bitcoin': 0, 'ethereum': 0, 'tron': 0}
HBTC = {'bitcoin': 0, 'ethereum': 0, 'tron': 0}
HSATS = {'bitcoin': 0, 'ethereum': 0, 'tron': 0}
HUSDTBTC = 0
HUSDTETHER = 0
HUSDCBTC = 0
HUSDCETHER = 0


while True:
    usd = get_tick('usd')
    pln = get_tick('pln')
    btc = get_tick('btc')
    sats = get_tick('sats')
    with pipi.container():
        fst, scd, thd, fth, ffth, sxth =  st.columns([1, 1, 1, 1, 1, 1])

        fst.header('USD')
        for key, val in usd.items():
            fst.metric(key.upper(), value=f'{val}', delta=f'{calculate_difference(HUSD, usd)[key]:.2f}')
        fst.write('')
        fst.write('')
        fst.write('')
        fst.write('')
        fst.write('')
        fst.write('')
        fst.write('')        
        fst.image('https://alternative.me/crypto/fear-and-greed-index.png')

        scd.header('USDT')
        usdtbtc = get_stable('tether', 'btc')
        usdtether = get_stable('tether', 'eth')
        scd.metric('BITCOIN', value = f'{usdtbtc:.2f}', delta=f'{(usdtbtc-HUSDTBTC):.2f}')
        scd.metric('ETHEREUM', value = f'{usdtether:.2f}', delta=f'{(usdtether-HUSDTETHER):.2f}')

        thd.header('USDC')
        usdcbtc = get_stable('usd-coin', 'btc')
        usdcether = get_stable('usd-coin', 'eth')
        thd.metric('BITCOIN', value = f'{usdcbtc:.2f}', delta=f'{(usdcbtc-HUSDCBTC):.2f}')
        thd.metric('BITCOIN', value = f'{usdcether:.2f}', delta=f'{(usdcether-HUSDCETHER):.2f}')

        fth.header('PLN')
        for key, val in pln.items():
            fth.metric(key.upper(), value=f'{val}', delta=f'{calculate_difference(HPLN, pln)[key]:.2f}')

        ffth.header('BTC')
        for key, val in btc.items():
            if key != 'bitcoin':
                ffth.metric(key.upper(), value=f'{val}', delta=f'{calculate_difference(HBTC, btc)[key]:.2f}')

        sxth.header('SATOSHI')
        for key, val in sats.items():
            if key != 'bitcoin':
                sxth.metric(key.upper(), value=f'{val}', delta=f'{calculate_difference(HSATS, sats)[key]:.2f}')
                
    HUSD = usd
    HPLN = pln
    HBTC = btc
    HSATS = sats
    HUSDTBTC = usdtbtc
    HUSDTETHER = usdtether
    HUSDCBTC = usdcbtc
    HUSDCETHER = usdcether

    time.sleep(90)
    pipi.empty()
