
#!/usr/bin/python3
from pandas import DataFrame, read_csv

raw_file = './net_scan_A.csv'
df = read_csv(raw_file, sep=';')
df.head()

#data cleaning here
df_1 = df
#remove redundant rows of column headings
df_1 = df_1[df_1['host'].str.contains('host')==False]
#remove unneeded cols
df_1 = df_1.drop(columns= {'hostname_type','state','reason',
                           'conf','protocol'})
#format col headings
df_1 = df_1.rename(columns={'host':'IP Address','hostname':'Hostname','port':'Open Port',
                            'name':'Service', 'product':'Service Product', 'cpe':'Operating System',
                            'extrainfo':'Additional Info', 'version':'Version'})
#rearrange col into logical order
df_1 = df_1[['IP Address','Hostname','Operating System',
           'Open Port','Service','Service Product',
           'Version','Additional Info']]
#clean up OS information
df_1['Operating System'] = df_1['Operating System'].str.strip('cpe:').str.strip('/a:').str.strip('/o:')

#new clean dataframe 
clean_df = df_1

clean_df.head()

#clean_df.to_csv('./cleaned_scan.csv')

#to get number of unique IP addresses and how many total ports are open in the network
ip_port_df = clean_df[['IP Address','Open Port']]
ip_port_df.head()

#how many ports:
n_port = ip_port_df['Open Port'].drop_duplicates().count()
print(n_port)

#how many unique ip addresses
n_ip = ip_port_df['IP Address'].drop_duplicates().count()
print(n_ip)

