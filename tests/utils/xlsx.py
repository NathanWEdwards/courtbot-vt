from xlsxwriter import Workbook


def xlsx_file(filename, rows):
    """
    :param filename: {str} the full path and filename to write an xlsx file.
    :param rows: {List<List>} A list the rows
    """
    row_count = len(rows)
    # Create an xlsx workbook and worksheet
    workbook = Workbook(filename)
    worksheet = workbook.add_worksheet()
    # Populate xlsx cells
    for row_index in range(row_count):
        row = rows[row_index]
        column_count = len(row)
        for column_index in range(column_count):
            worksheet.write(row_index, column_index, row[column_index])
    workbook.close()
