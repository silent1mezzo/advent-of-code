from argparse import ArgumentParser
from pathlib import Path

PYTHON_TEMPLATE = """
data = []

def read_input():
    with open('input.txt') as reader:
        for line in reader.readlines():
            data.append(int(line))

def part_1():
    pass

def part_2():
    pass


read_input()
print(f"Answer for part 1: {part_1()}")
print(f"Answer for part 2: {part_2()}")

""".strip() + "\n"

def main() -> None:
    parser = ArgumentParser(description="Create skeleton files for a day.")
    parser.add_argument("day", type=int, help="the day to create files for")

    args = parser.parse_args()

    project_root = Path(__file__).parent
    day_str = f"day{args.day:02}"
    day_directory = project_root / f"{day_str}"
    if day_directory.is_dir():
        raise RuntimeError(f"{day_directory} already exists")

    for file, content in [
        (day_directory / "input.txt", ""),
        (day_directory / f"{day_str}.py", PYTHON_TEMPLATE),
    ]:
        file.parent.mkdir(parents=True, exist_ok=True)
        with file.open("w+", encoding="utf-8") as f:
            f.write(content)

        print(f"Successfully created {file.relative_to(project_root)}")

if __name__ == "__main__":
    main()