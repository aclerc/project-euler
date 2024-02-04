from pathlib import Path


def score_names_file(fpath: Path) -> int:
    raw_content = fpath.open().readlines()
    names_list = raw_content[0].split(",")
    names_list = [x.strip('"') for x in names_list]
    names_list = sorted(names_list)
    total_score = 0
    for i, name in enumerate(names_list):
        name_worth = 0
        for letter in name:
            name_worth += ord(letter.upper()) - ord("A") + 1
        name_score = (i + 1) * name_worth
        print(f"{name} scores {name_score}")
        total_score += name_score
    return total_score


if __name__ == "__main__":
    print(
        "Using names.txt begin by sorting it into alphabetical order. Then working out the alphabetical value for "
        "each name, multiply this value by its alphabetical position in the list to obtain a name score. For "
        "example, when the list is sorted into alphabetical order, COLIN, which is worth 3+15+12+9+14=53, is "
        "the 938th name in the list. So, COLIN would obtain a score of 938*53=49714. What is the total of all "
        "the name scores in the file?",
    )
    fpath = Path(__file__).parents[1] / "input_data" / "0022_names.txt"
    print(score_names_file(fpath))
