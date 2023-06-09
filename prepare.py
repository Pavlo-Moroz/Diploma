import pandas as pd
data = pd.read_csv('us-counties-2020.csv',index_col='date',parse_dates=['date'])
filtered_data = data[data['state']=='California']

data = data.drop(columns=['county','fips','state','deaths'])

filtered_data = filtered_data.groupby('date').agg({'cases': 'sum', 'deaths': 'sum'})

filtered_data['count'] = filtered_data['cases']
filtered_data = filtered_data.drop(columns=['cases'])
filtered_data = filtered_data[:'2020-07-05']
filtered_data.to_csv('covid_data.csv')


old_data = pd.read_csv('Crime_Data_from_2010_to_2019.csv')
new_data = pd.read_csv('Crime_Data_from_2020_to_Present.csv')
data = old_data
data = pd.concat([old_data,new_data])
data = data[data['Crm Cd'].isin([236,626])]
not_delete = ['DATE OCC']
data = data.drop(columns=[column for column in data.columns if column not in not_delete])
data = data.groupby('DATE OCC').size().reset_index(name='count')
data.set_index("DATE OCC", inplace=True)
data = data['28-12-2015':'05-07-2020']
data.to_csv('crime_data.csv')
