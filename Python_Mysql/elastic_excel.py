import pandas as pd
from elasticsearch import Elasticsearch
from functools import reduce
####### NOTE -- Mandatory ---> Host local elastic search server with default settings if
########  hosted with credential then modify code to use the elastic search.
es = Elasticsearch() # get default connection

def read_excel(file_name):
    """ :param": filename
        :return: pandas dataframe
    """
    product_info = pd.read_excel(file_name, sheet_name='product_listing')
    group_info = pd.read_excel(file_name, sheet_name='group_listing')
    return product_info, group_info

def put_date_into_elastic(data_frame,index_name):
    """
    Puts data in elastic search
    :param data_frame:
    :param index_name:
    :return: status
    """
    for col, row in data_frame.iterrows():
       response =  es.index(index=index_name, id = int(col), doc_type='dict', body=dict(row))
       print(" One row created")

def get_data_from_elastic(index_name, data_length) :
    """
    Fetch data from elastic search
    :param index_name:
    :param data_length:
    :return:
    """
    ids = [i for i in range(data_length)]
    response = es.mget(index=index_name, body={'ids':ids})
    return response

def custom_print(data):
    for item in  data['docs']:
        print(item)

#RUN FILE

product_info, group_info = read_excel('beginner_assignment01.xlsx') # TODO uncomment to read data from excel

# create product info in elastic search
# put_date_into_elastic(product_info, 'product_info') # TODO comment if data has already put in
#create group info in elastic search
# put_date_into_elastic(group_info, 'group_info')  # TODO comment if data has already put in

#get product info from elastic
custom_print(get_data_from_elastic('product_info', len(product_info))) # TODO uncomment if data has been put into elastic
custom_print(get_data_from_elastic('group_info',len(group_info))) # TODO uncomment if data has been put into elastic



