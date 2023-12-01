from pathlib import Path
import re

path = Path(__file__).parent / "./day1-input.txt"
file = open(path)
textData = file.read()
file.close()


def extract_calibration_values(text_data: str):
    total = 0
    text_split_by_line = text_data.split("\n")
    for line in text_split_by_line:
        number_list = re.findall(r"\d", line)
        if len(number_list) == 0:
            continue
        first_num = number_list[0]
        last_num = '' if len(number_list) == 0 else number_list[-1]
        total += int(first_num + last_num)
    return total


print(extract_calibration_values(textData))
