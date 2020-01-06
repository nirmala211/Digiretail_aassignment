import mysql.connector as connector
import pandas as pd



# change db credentials according to your db
db_credentials = {
    'host' : "db4free.net",
    'user' : "nirmala",
    'password' : "nirmala123",
    'database' : 'nirmala'
}

elastic_credentials = {}

#making db connection
connection = connector.connect(**db_credentials)
cursor = connection.cursor()

# Queries

db_create = """create database Digiretail"""

table_create_product = """ create table ProductInfo (
  id int(11)  NOT NULL AUTO_INCREMENT,
  ProductName varchar(200),
  ModelName   varchar(200),
  ProductSerialNo  bigint,
  GroupAssociated  varchar(200),
  ProductMRP_(rs) int(11),
  PRIMARY KEY (id) """
table_create_group = """create table GroupInfo(
  id int(11) NOT NULL AUTO_INCREMENT,
  GroupName varchar(200),
  GroupDescription varchar(200),
  isActive boolean ,
  PRIMARY KEY (id)
  )"""
fetch_product = """select * from ProductInfo"""
fetch_group = """select * from GroupInfo"""

insert_product = "Insert into ProductInfo (ProductName, ModelName, ProductSerialNo, GroupAssociated, ProductMRP) values {0}"
insert_group = "Insert into GroupInfo(GroupName, GroupDescription, isActive) values {0}"

def read_excel(file_name):
    """ :param": filename
        :return: pandas dataframe
    """
    product_info = pd.read_excel(file_name, sheet_name='product_listing')
    group_info = pd.read_excel(file_name, sheet_name='group_listing')
    return product_info, group_info

def create_db():
    """ creates db"""
    cursor.execute(db_create)

def create_tables():
    """ creates table"""
    cursor.execute(table_create_group)
    cursor.execute(table_create_product)

def insert_into_db(dataframe, query):
    """
    Puts data into database
    :param: dataframe
        :param : query
        :return none
        """
    for col, row in dataframe.iterrows():
        cursor.execute(query.format(tuple(row)))
        print (tuple(row))
        connection.commit()

def fetch_data_from_db(query):
    """Fetches data from database
    :param : query
    :return : result
    """
    cursor.execute(query)
    result = cursor.fetchall()
    return result

def custom_print(data):
    for item in data:
        print(item)

#RUN FILE
#create_db() #TODO: Uncomment only if  you haven't created db
#create_tables() #TODO: Uncomment only if you haven't created tables
# product_info, group_info = read_excel('beginner_assignment01.xlsx') # TODO uncomment to read data from excel file
# insert Product data into db
# insert_into_db(product_info, insert_product) #TODO: comment it once inserted
# insert into group data into db
# insert_into_db(group_info, insert_group) # TODO:comment it once inserted
print (" >>>>>>>>>>>>>>>>>>>>>>>>> Product Info <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
custom_print (fetch_data_from_db(fetch_product)) # TODO uncomment if data has been push to db
print (" >>>>>>>>>>>>>>>>>>>>>>>>> Group Info <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
custom_print (fetch_data_from_db(fetch_group))    # TODO uncomment if data has been push to db

