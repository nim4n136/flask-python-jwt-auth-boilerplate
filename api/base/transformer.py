def rowTransform(row, columns = []):
    d = {}
    for column in row.__table__.columns:
        if columns == []:
            d[column.name] = str(getattr(row, column.name))
        else:
            if column.name not in columns:
                continue
            d[column.name] = str(getattr(row, column.name))
    return d


def rowsTransform(rows, columns = []):
    list_rows = []
    for row in rows:
        list_rows.append(rowTransform(row, columns))
    return list_rows
