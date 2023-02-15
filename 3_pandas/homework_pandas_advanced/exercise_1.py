#Для датафрейма log из материалов занятия создайте столбец source_type по правилам:

# если источник traffic_source равен Yandex или Google, то в source_type ставится organic;
# для источников paid и email из России ставим ad;
# для источников paid и email не из России ставим other;
# все остальные варианты берём из traffic_source без изменений.

import pandas as pd

log = pd.read_csv('visit_log.csv', sep=';')

log.loc[log.traffic_source.isin(['yandex', 'google']), 'source_type'] = 'organic'
log.loc[(log.traffic_source.isin(['paid', 'email'])) & (log.region == 'Russia'), 'source_type'] = 'ad'
log.loc[(log.traffic_source.isin(['paid', 'email'])) & (log.region != 'Russia'), 'source_type'] = 'other'
log.loc[pd.isnull(log.source_type), 'source_type'] = log.traffic_source

log.head(20)