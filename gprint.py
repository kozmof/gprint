from typing import List
from unicodedata import east_asian_width


def count_wide_char(line: str):
    count = 0
    for char in line:
        if east_asian_width(char) in ["W", "F", "A"]:
            count += 1
    return count


def grid_text(*texts, margin: int = 3, enable_east_asian_width: bool = False) -> str:
    whole_max_len: List[int] = []
    max_height: int = 0

    for text in texts:
        lines = text.split("\n")
        height = len(lines)

        if enable_east_asian_width:
            max_len = max([len(line) + count_wide_char(line) for line in lines])
        else:
            max_len = max([len(line) for line in lines])

        whole_max_len.append(max_len)
        if max_height < height:
            max_height = height

    result_lines = ["" for _ in range(max_height)]

    last_col_pos = len(texts) - 1

    for col_pos, text in enumerate(texts):
        lines = text.split("\n")
        for line_pos, line in enumerate(lines):
            if enable_east_asian_width:
                if col_pos == last_col_pos:
                    padding = " " * (whole_max_len[col_pos] - len(line) - count_wide_char(line))
                else:
                    padding = " " * (whole_max_len[col_pos] - len(line) - count_wide_char(line)) + " " * margin
            else:
                if col_pos == last_col_pos:
                    padding = " " * (whole_max_len[col_pos] - len(line))
                else:
                    padding = " " * (whole_max_len[col_pos] - len(line)) + " " * margin
            result_lines[line_pos] += f"{line}{padding}"

        if len(lines) < max_height:
            line_padding = max_height - len(lines)
            for n in range(line_padding):
                rest_line_pos = n + len(lines)
                if col_pos == last_col_pos:
                    result_lines[rest_line_pos] += " " * whole_max_len[col_pos] 
                else:
                    result_lines[rest_line_pos] += " " * whole_max_len[col_pos] + " " * margin

    result = "\n".join(result_lines)
    return result


def gprint(*texts, margin: int = 3, enable_east_asian_width: bool = False) -> None:
    result = grid_text(*texts, margin=margin, enable_east_asian_width=enable_east_asian_width)
    print(result)