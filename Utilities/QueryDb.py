from Utilities.Conn import GetConnection;
import json;

def QueryData(tableName, dict):
    conn = GetConnection()
    cursor = conn.cursor()
    where = GenerateWhere(dict)
    query = 'SELECT * FROM ' + tableName + ' ' + where
    cursor.execute(query)
    rows = cursor.fetchall()
    data = []
    for row in rows:
        data.append(list(row))
    jsonResponse = json.dumps(data, default=str)
    return jsonResponse


def GenerateWhere(dict):
    where = 'WHERE '
    for key in dict.keys():
        if(where != 'WHERE '):
            where = where + ' AND '
        where  = where + key + "='" + dict[key] + "'"
    
    if(where == 'WHERE '):
        return ''
    
    return where
