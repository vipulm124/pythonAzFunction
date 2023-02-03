from Utilities.Conn import GetConnection;
import json;

def QueryData(tableName):
    conn = GetConnection()
    cursor = conn.cursor()
    query = 'SELECT * FROM ' + tableName
    cursor.execute(query)
    rows = cursor.fetchall()
    data = []
    for row in rows:
        data.append(list(row))
    jsonResponse = json.dumps(data, default=str)
    return jsonResponse
