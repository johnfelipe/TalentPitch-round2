import psycopg2
from sqlalchemy import create_engine
import pandas as pd

def trans_data():
    conn = psycopg2.connect(
        host="host.docker.internal",
        database="airflow",
        user="airflow",
        password="airflow"
    )

    cur = conn.cursor()
    cur.execute("SELECT * FROM traffic_flow_map")
    rows = cur.fetchall()
    db_df = pd.DataFrame(rows, columns=['OBJECTID', 'STNAME', 'COUNT_LOCATION', 'YEAR', 'SEGKEY', 'AAWDT', 'INPUT_STUDY_ID'])
    print(db_df.head())

    cur.close()
    conn.close()


    # adding weather reference
    w_ref = pd.read_csv(r"dags/includes/py_scripts/weather_ref.csv")
    merged_df = pd.merge(db_df,w_ref,on='OBJECTID',how='left')

    engine = create_engine('postgresql://airflow:airflow@host.docker.internal:5432/airflow')
    # write the DataFrame to PostgreSQL
    merged_df.to_sql(name='traffic_flow_map_trans', con=engine, if_exists='replace', index=False)