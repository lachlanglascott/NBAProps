import mysql.connector
from mysql.connector import Error

connection = mysql.connector.connect(host='sportsbetting.c2oy3qveiway.ap-southeast-2.rds.amazonaws.com',
                                    database='nba',
                                    user='glascottl',
                                    password='Huntercoff26')
                                    
if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)

    mySql_Create_Table_Query = """CREATE TABLE Laptop ( 
                             Id int(11) NOT NULL,
                             Name varchar(250) NOT NULL,
                             Price float NOT NULL,
                             Purchase_date Date NOT NULL,
                             PRIMARY KEY (Id)) """

    cursor = connection.cursor()
    result = cursor.execute(mySql_Create_Table_Query)
    print("Laptop Table created successfully ")

    
    
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")


from sqlalchemy import create_engine
engine = create_engine('sqlite://', echo=False)

full_df.to_sql("full_df", con = connection, if_exists = 'append')



import pymysql

# create cursor
cursor=connection.cursor()

# creating column list for insertion
cols = "`,`".join([str(i) for i in full_df.columns.tolist()])

# Insert DataFrame recrds one by one.
for i,row in data.iterrows():
    sql = "INSERT INTO `nba_player_measures` (`" +cols + "`) VALUES (" + "%s,"*(len(row)-1) + "%s)"
    cursor.execute(sql, tuple(row))

    # the connection is not autocommitted by default, so we must commit to save our changes
    connection.commit()





# import the module
from sqlalchemy import create_engine
import pymysql

# create sqlalchemy engine
engine = create_engine("mysql+pymysql://{user}:{pw}@{db}"
                       .format(user="glascottl",
                               pw="Huntercoff26",
                               db="sportsbetting.c2oy3qveiway.ap-southeast-2.rds.amazonaws.com"))
                               
engine = create_engine("mysql+pymysql://glascottl:Huntercoff26@sportsbetting.c2oy3qveiway.ap-southeast-2.rds.amazonaws.com:3306/nba")
con = engine.raw_connection()
cursor = connection.cursor()
                               
full_df.to_sql('nba_player_measures', con = engine, if_exists = 'append', chunksize = 1000)      

full_df.to_sql('nba_player_measures', con = engine, if_exists = 'append', chunksize = 1000)

full_df.to_sql('nba_player_measures', engine, index=False, if_exists='append', chunksize=1000)









import pandas as pd
import sqlalchemy as db
from sqlalchemy import create_engine
import MySQLdb



mysql_con = mysql.connector.connect(host='sportsbetting.c2oy3qveiway.ap-southeast-2.rds.amazonaws.com',
                                    database='nba',
                                    user='glascottl',
                                    password='Huntercoff26')
mysql_cur = mysql_con.cursor()


engine = create_engine("mysql+pymysql://{user}:{pw}@{db}"
                       .format(user="glascottl",
                               pw="Huntercoff26",
                               db="sportsbetting.c2oy3qveiway.ap-southeast-2.rds.amazonaws.com"))
                               
#connection = engine.raw_connection()
conn = engine.connect()

mysql_ta = pd.read_sql("""select * from new_table order by 1 asc limit 10""",mysql_con)

full_df.to_sql('dummy_table', mysql_con, if_exists = 'replace',index=False)
full_df.to_sql('nba', con = engine, if_exists='append', index=False)

metadata = db.MetaData()
census = db.Table('new_table', metadata, autoload=True, autoload_with=engine)

connection = engine.connect()
d = pd.read_sql("SELECT * FROM new_table", con = connection)








DATABASE_URL = "mysql+pymysql://glascottl:Huntercoff26@sportsbetting.c2oy3qveiway.ap-southeast-2.rds.amazonaws.com:3306/nba"

from sqlalchemy import create_engine
engine = create_engine(DATABASE_URL)

from sqlalchemy import text
        
connection = engine.connect()
d = pd.read_sql("SELECT * FROM new_table", con = connection)
metadata = db.MetaData()

census = db.Table('new_table', metadata, autoload=True, autoload_with=engine)

query = db.select([census]) 
query = text("SELECT * FROM new_table")
ResultProxy = connection.execute(query)

ResultSet = ResultProxy.fetchall()
df = pd.DataFrame(ResultSet)




#### CREATE TABLE
# engine = db.create_engine('sqlite:///test.sqlite') #Create test.sqlite automatically
# connection = engine.connect()
# metadata = db.MetaData()

emp = db.Table('emp', metadata,
              db.Column('Id', db.Integer()),
              db.Column('name', db.String(255), nullable=False),
              db.Column('salary', db.Float(), default=100.0),
              db.Column('active', db.Boolean(), default=True)
              )

metadata.create_all(engine) #Creates the table


#Inserting record one by one
query = db.insert(emp).values(Id=1, name='naveen', salary=60000.00, active=True) 
ResultProxy = connection.execute(query)

#Inserting many records at ones
query = db.insert(emp) 
values_list = [{'Id':'2', 'name':'ram', 'salary':80000, 'active':False},
               {'Id':'3', 'name':'ramesh', 'salary':70000, 'active':True}]
ResultProxy = connection.execute(query,values_list)


results = connection.execute(db.select([emp])).fetchall()
df = pd.DataFrame(results)
df.columns = results[0].keys()
df.head(4)






mysql_host = 'sportsbetting.c2oy3qveiway.ap-southeast-2.rds.amazonaws.com'
mysql_dbname = 'nba'
mysql_user = 'glascottl'
mysql_pwd = 'Huntercoff26'
msql_port = 3306

mysql_properties = {
    'host': mysql_host,
    'dbname': mysql_dbname,
    'user': mysql_user,
    'pwd': mysql_pwd,
    'port': msql_port
}

load_dataframe_into_mysql_table(full_df, 'nba_player_measures', mysql_properties)


engine = create_engine(f'''mysql+pymysql://{mysql_user}:{mysql_pwd}@{mysql_host}/{mysql_dbname}'''
                               .format(mysql_user=mysql_user,
                               mysql_pwd=mysql_pwd,
                               mysql_host=mysql_host,
                               mysql_dbname=mysql_dbname))
con = engine.connect()

