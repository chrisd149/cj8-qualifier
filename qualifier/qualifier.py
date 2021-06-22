from typing import Any, List, Optional


def make_table(rows: List[List[Any]], labels: Optional[List[Any]] = None, centered: bool = False) -> str:
    """
    :param rows: 2D list containing objects that have a single-line representation (via `str`).
    All rows must be of the same length.
    :param labels: List containing the column labels. If present, the length must equal to that of each row.
    :param centered: If the items should be aligned to the center, else they are left aligned.
    :return: A table representing the rows passed in.
    """
    
    row_length = None
    if not labels:
        cols = 1
        table_data = ""

        # First loop for finding longest str length
        for item in rows:
            if row_length is None:
                row_length = len(str(item))
            elif len(str(item)) > row_length:
                row_length = len(str(item))

        # Second loop to create rows
        for item in rows:
            row = f"│{str(item[cols - 1]).center(row_length)}│\n"
            table_data = table_data + row
        top_row_border = ("┌{}┐\n".format("".join([("─" * row_length)])))
        bottom_row_border = ("└{}┘".format("".join([("─" * row_length)])))
        table = top_row_border + table_data + bottom_row_border
    else:
        cols = len(labels)

    """
    str_list_data = str(list_data)[1:-1]
    str_list_data = str(str_list_data).replace(',|', ' ')
    table = (str_list_data)
    """

    return table

table = make_table(
    rows=[
        ["Lemon"],
        ["Sebastiaan"],
        ["KutieKatj9"],
        ["Jake"],
        ["Not Joe"]
    ]
)

print(table)