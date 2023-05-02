import psycopg2
import pandas as pd

def extract_data():
    conn = psycopg2.connect(
        host="host.docker.internal",
        database="airflow",
        user="airflow",
        password="airflow"
    )

    cur = conn.cursor()
    cur.execute("SELECT * FROM traffic_flow_map_trans")
    rows = cur.fetchall()


    ex_df = pd.DataFrame(rows, columns=['STNAME', 'YEAR', 'OBJECTID_CNT', 'COUNT_LOCATION_CNT',  'SEGKEY_CNT', 'AAWDT_CNT', 'INPUT_STUDY_ID_CNT', 'WEATHER'])

    cur.close()
    conn.close()

    df_final = ex_df["WEATHER"].value_counts().rename_axis('WEATHER_COND').reset_index(name='NUM_ACCIDENTS')


    df_final.to_csv("dags/includes/py_scripts/output/number_of_accidents_by_climates.csv", index=False)