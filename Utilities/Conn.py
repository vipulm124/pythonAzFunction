import os;
import pyodbc;

def GetConnection():
    connString = os.environ["SQLConnectionString"]
    conn = pyodbc.connect(connString)
    return conn