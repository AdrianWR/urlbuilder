#!venv /usr/bin/python3

from google.cloud import bigquery
#from google.oauth2.service_account import Credentials
from urlbuilder import ScieloSearchLocations
from urlbuilder import URLBuilder
import centaurminer as mining
#import pandas_gbq
import sys
import os

# The order is important here.
# Be careful before changing any value.
url_schema = [
    {'name': 'article_url', 'type': 'STRING',   'mode': 'REQUIRED'},
    {'name': 'catalog_url', 'type': 'STRING',   'mode': 'REQUIRED'},
    {'name': 'is_pdf',      'type': 'INTEGER',  'mode': 'REQUIRED'},
    {'name': 'language',    'type': 'STRING'                      },
    {'name': 'status',      'type': 'STRING',   'mode': 'REQUIRED'},
    {'name': 'timestamp',   'type': 'DATETIME', 'mode': 'REQUIRED'},
    {'name': 'worker_id',   'type': 'STRING'                      },
    {'name': 'meta_info',   'type': 'STRING'                      }
]

job_config = bigquery.LoadJobConfig(schema=[
    bigquery.SchemaField('article_url', 'STRING', mode='REQUIRED'),
    bigquery.SchemaField('catalog_url', 'STRING', mode='REQUIRED'),
    bigquery.SchemaField('is_pdf', 'INTEGER', mode='REQUIRED'),
    bigquery.SchemaField('language', 'STRING'),
    bigquery.SchemaField('status', 'STRING', mode='REQUIRED'),
    bigquery.SchemaField('timestamp', 'TIMESTAMP', mode='REQUIRED'),
    bigquery.SchemaField('worker_id', 'STRING'),
    bigquery.SchemaField('meta_info', 'STRING'),
])


def main():

    # Google BigQuery Authentication. At first, we'll try to fetch
    # authentication data from a 'credentials.json' file at our 
    # working directory. If this file doesn't exist, we authenticate
    # with web login.
    try:
        client = bigquery.Client()
    except (KeyError, FileNotFoundError):
        print("Invalid credentials. Set GOOGLE_APPLICATION_CREDENTIALS to your credentials file.");
        exit(1);

    # Project, dataset and table configuration
    #pandas_gbq.context.credentials = credentials
    project_id   = os.environ["PROJECT_ID"]
    url_table_id = os.environ["TABLE_ID"]

    driver_path='/usr/lib/chromium-browser/chromedriver'
    miner = mining.MiningEngine(ScieloSearchLocations, driver_path=driver_path)
    URLBuilder.connect_to_gbq(client, project_id, url_table_id, job_config)
    scielo_builder = URLBuilder(miner)

    # Collect these number of URLs and store them in pd.DataFrame
    search_domain = 'https://search.scielo.org/'
    search_terms = sys.argv[1:-1]
    limit = int(sys.argv[-1])
    scielo_builder.collect(search_domain, search_terms, limit)


if __name__  == "__main__":
    main()
