import os
import json
import argparse

"""
Data was parsed using https://github.com/Adrien-Luxey/Da-Fonky-Movie-Script-Parser
"""


def parse(file_name):
    # all characters
    characters = set()

    # replace the errenous keys with values in the characters set
    errors = {
        "HANS                                 *": "HANS",
        "ARGYLE'S VOICE": "ARGYLE",
        "WOMAN (HOLLY)": "HOLLY",
        "MCCLANE'S VOICE": "MCCLANE",
        "MAN #1 (THEO)": "THEO",
        "SALESMAN'S VOICE": "SALESMAN"
    }

    with open(file_name, "r") as f:
        data = json.load(f)
        scripts = data["movie_script"]

        for script in scripts:
            if script["type"] == "speech":
                character = script["character"]
                if character in errors.keys():
                    character = errors[character]
                characters.add(character)

    print(characters)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Parse the json file")
    parser.add_argument("-f", "--file", help="The file to parse")
    args = parser.parse_args()

    parse(args.file)
