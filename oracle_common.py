def query(connection, query, condition): 
    cursor = connection.cursor()
    cursor.prepare(query)
    cursor.execute(None, condition)
    result = []
    for row in cursor:
        result.append(row)
    cursor.close()

    return result