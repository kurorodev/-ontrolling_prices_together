import pandas as pd

def get_exel_data():
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    df = pd.read_excel('app/data/12_02.xlsx',index_col=0, skiprows=2)
    for index, row in df.iterrows():
        l.append(row)
    rows_list = []
    data_dict = {'data': [rows_list]}
    return data_dict

