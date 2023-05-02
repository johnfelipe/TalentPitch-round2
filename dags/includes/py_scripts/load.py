
from sqlalchemy import create_engine
import pandas as pd

def load():
    df = pd.read_csv(r"dags/includes/py_scripts/Traffic_Flow_Map_Volumes.csv")
    df = df.dropna()
    print(df.head())

    # create a SQLAlchemy engine
    engine = create_engine('postgresql://airflow:airflow@host.docker.internal:5432/airflow')


    # write the DataFrame to PostgreSQL
    df.to_sql(name='traffic_flow_map', con=engine, if_exists='replace', index=False)

