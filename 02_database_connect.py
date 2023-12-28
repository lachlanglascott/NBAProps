# import the module
from sqlalchemy import create_engine
import pymysql

# create sqlalchemy engine  
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

engine = create_engine(f'''mysql+pymysql://{mysql_user}:{mysql_pwd}@{mysql_host}/{mysql_dbname}'''
                               .format(mysql_user=mysql_user,
                               mysql_pwd=mysql_pwd,
                               mysql_host=mysql_host,
                               mysql_dbname=mysql_dbname))
con = engine.connect()
                               
#full_df_dates.to_sql('nba_player_measures', con = engine, if_exists = 'replace', index = False, index_label=None)      

#df = pd.read_sql("""select  * from nba_player_measures limit 100""",con)
#df


tables = pd.read_sql("""SELECT table_name FROM information_schema.tables WHERE table_schema = 'nba'""",con)
tables

#tables = pd.read_sql("""SELECT * FROM nba_player_measures_21_22""",con)
#tables
