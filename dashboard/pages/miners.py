import streamlit as st
from ethermine import Ethermine
import time

st.set_page_config(page_title='MINERS', layout='wide', page_icon=':moneybag:')
ethermine = Ethermine()
ad = st.secrets['wallet']
pholder = st.empty()


while True:
    source = ethermine.miner_current_stats(ad)
    list_of_workers = [x for x in ethermine.miner_workers(ad)]
    with pholder.container():
        left_column, middle_column = st.columns([2, 1])
        left_column.header('MURZYNY:')
        left_column.write('---')
        for items in list_of_workers:
            left_column.metric(items['worker'], items['reportedHashrate']/10**6)
            if items['reportedHashrate'] < 100:
                left_column.warning('COS SIE ZEPSULO!')

        reported_rate = int(source['reportedHashrate']/10**6)
        usd_per_min = source['usdPerMin']
        coin_per_min = source['coinsPerMin']
        btc_per_min = source['btcPerMin']
        uhour = (usd_per_min * 60) / reported_rate
        chour = coin_per_min / reported_rate * 60
        btchour = btc_per_min / reported_rate * 60
        middle_column.header('1MH MOC')
        middle_column.write('---')
        middle_column.write(f'1MH = {uhour:.16f} USD PER HOUR')
        middle_column.write(f'1MH = {chour:.16f} ETH PER HOUR')
        middle_column.write(f'1MH = {btchour:.16f} BTC PER HOUR')
        middle_column.write('---')
        middle_column.header('MEGAHUJASZE ZA GODZINKE RUCHANKA ;)')
        middle_column.subheader(f'{reported_rate}')
        middle_column.write(f'{usd_per_min * 60} USD')
        middle_column.write(f'{coin_per_min * 60} ETH')

        
    time.sleep(60)
    pholder.empty()
