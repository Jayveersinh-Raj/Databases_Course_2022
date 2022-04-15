#!/usr/bin/python
import psycopg2

hostname = 'localhost'
database = 'dvdrental'
username = 'postgres'
pwd = 'jyvr2891'
port_id = 5432

try:
        conn = psycopg2.connect(
            host = hostname,
            dbname = database,
            user = username,
            password = pwd,
            port = port_id
        )
        conn.close()

except Exception as error:
     print(error)