import requests
import datetime
import os
from decouple import config


def get_code_position(text):
    start_tag = '<pre><code>'
    end_tag = '</code></pre>'
    start = text.rfind(start_tag) + len(start_tag)
    end = text.rfind(end_tag)

    return start, end


def get_title(day, year):
    base_url = f"https://adventofcode.com/{year}/day/{day}"
    response = requests.get(base_url)
    text = response.text

    start_tag = '<h2>'
    end_tag = '</h2>'
    start = text.rfind(start_tag) + len(start_tag)
    end = text.rfind(end_tag)

    title = text[start + 4:end - 4]

    return title


def download_input(day, year):
    base_url = f"https://adventofcode.com/{year}/day/{day}"
    session_cookie = config('SESSION_COOKIE')

    if not os.path.exists(f"inputs"):
        os.makedirs(f"inputs")
        os.makedirs(f"inputs/real")
        os.makedirs(f"inputs/sample")

    headers = {
        "Cookie": f"session={session_cookie}",
    }

    response = requests.get(base_url + '/input', headers=headers)

    # Download input
    if response.status_code == 200:
        input_text = response.text.strip()
        save_path = f"inputs/real/input_day_{day}.txt"
        with open(save_path, "w") as file:
            file.write(input_text)
        print(f"Input file for Day {day} saved as {save_path}")
    else:
        raise Exception(f"Failed to download input for Day {day}. Status code: {response.status_code}")

    # Download sample
    response = requests.get(base_url, headers=headers)
    start, end = get_code_position(response.text)

    if end == -1:
        raise Exception(f"Failed to download sample input for Day {day}. Sample code not found")
    else:
        save_path = f"inputs/sample/sample_input_day_{day}.txt"
        with open(save_path, "w") as file:
            file.write(response.text[start:end - 1])
        print(f"Sample input file for Day {day} saved as {save_path}")


def create_readme(readme_path, title, day, year):
    initial_readme = f"""# Advent Of Code {year}
This is my repository for the annual [**Advent of Code**](https://adventofcode.com/).

- [{title}](#day-1)

# Notes on each day's challenge

"""

    readme = f"""\n## [{title}](https://adventofcode.com/{year}/day/{day})<span id="day-{day}"><span>

```
┌─┬─┐   ╔═╦═╗
│■│█│ ▪ ║●║ ║ 
├─┼─┤   ╠═╬═╣
│□│¯│ ▫ ║○║ ║ 
└─┴─┘   ╚═╩═╝
Part 1:

Part 2:
```
"""

    # Create initial README if it doesn't exist
    if not os.path.exists(readme_path):
        with open(readme_path, 'a', encoding="utf-8") as file:
            file.write(initial_readme)

    # Append README's main content
    with open(readme_path, 'a', encoding="utf-8") as file:
        file.write(readme)

    # Add anchor in table of content
    if day > 1:
        with open(readme_path, 'r', encoding="utf-8") as file:
            content = file.read()

        previous_day_anchor = f'(#day-{day - 1})\n'
        index = content.find(previous_day_anchor)
        insert_text = f'- [{title}](#day-{day})\n'

        if index == -1:
            return
        insertion_point = index + len(previous_day_anchor)

        new_content = content[:insertion_point] + insert_text + content[insertion_point:]
        with open(readme_path, 'w', encoding="utf-8") as file:
            file.write(new_content)


def create_python(day):
    save_path = f"day_{day:02d}/part_1.py"
    save_path_2 = f"day_{day:02d}/part_2.py"

    python_file = f"""import platform, sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
base_path = '..' if platform.python_implementation() == 'CPython' else '.'

with open(base_path + '/inputs/real/input_day_{day}.txt', 'r') as file:
    input_lines = [i.rstrip("\\n") for i in file.readlines()]

with open(base_path + '/inputs/sample/sample_input_day_{day}.txt', 'r') as file:
    sample_lines = [i.rstrip("\\n") for i in file.readlines()]




def process(lines):
    return lines

print("Sample output:", process(sample_lines))
print("Answer:", process(input_lines))

# pypy ./{save_path}

"""

    if not os.path.exists(f"day_{day:02d}"):
        os.makedirs(f"day_{day:02d}")

    if not os.path.exists(save_path):
        with open(save_path, "w") as file:
            file.write(python_file)

    if not os.path.exists(save_path_2):
        with open(save_path_2, "w") as file:
            file.write('')


def create_day(day, year):
    title = get_title(day, year)
    readme_path = 'README.md'

    create_python(day)
    create_readme(readme_path, title, day, year)


if __name__ == "__main__":
    day = datetime.datetime.now().day
    year = datetime.datetime.now().year
    create_day(day, year)
    download_input(day, year)
