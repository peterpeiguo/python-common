def query(connection, query, condition): 
    cursor = connection.cursor()
    cursor.prepare(query)
    cursor.execute(None, {})
    result = []
    for row in cursor:
        result.append(row)
    cursor.close()

    return result