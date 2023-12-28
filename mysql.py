from sqlalchemy import create_engine

from sql.database import *
from src.config import logger

class MySQL(Database):
    """
    Simple Wrapper class for interacting with MySQL database
    """
    timeout = 10

    def __init__(self, properties: dict):
        super().__init__(dbname=properties['dbname'],
                         host=properties['host'],
                         port=properties['port'],
                         user=properties['user'],
                         pwd=properties['pwd'])

    def _connect(self):
        """
        Creates a connection object for the database
        Automatically called when using "with" keyword.
        """
        engine = create_engine(f'''mysql+pymysql://{self.user}:{self.pwd}@{self.host}/{self.dbname}''',
                               connect_args={'connect_timeout': self.timeout})
        self.con = engine.connect()

    def query(self, query: str, params: dict) -> pd.DataFrame:
        """
        :param query: the SQL query to be executed
        :param params: the parameters of the query (in any)
        :return: DataFrame containing results of query
        """
        return pd.read_sql_query(sql=query, con=self.con, params=params)


def run_mysql_qry(query: str, properties: dict, params=None) -> pd.DataFrame:
    if params is None:
        params = dict()

    with MySQL(properties=properties) as my:
        logger.debug(f'''[{properties['dbname']}] query: {query}''')
        return my.query(query, params=params)


def run_mysql_stm(stm: str, properties: dict, params=None):
    if params is None:
        params = dict()

    with MySQL(properties=properties) as my:
        param_stm = stm % params
        logger.debug(f'''[{properties['dbname']}] stm: {param_stm}''')
        my.con.execute(param_stm)
        logger.info(f'Statement has been successfully executed')


def load_dataframe_into_mysql_table(df: pd.DataFrame, table: str, properties: dict):
    with MySQL(properties=properties) as my:
        logger.info(f'''[{properties['dbname']}]: loading data into table {table}''')
        df.to_sql(table, con=my.con, index=False, if_exists='append')
        del df
