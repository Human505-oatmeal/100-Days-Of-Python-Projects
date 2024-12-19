# constants for file paths
INPUT_NAMES_FILE = "./Input/Names/invited_names.txt"
STARTING_LETTER_FILE = "./Input/Letters/starting_letter.txt"


def list_names() -> list:
    """Returns a list of names as strings."""
    try:
        with open(INPUT_NAMES_FILE, "r") as file:
            return [name.strip() for name in file.readlines()]
    except FileNotFoundError:
        print(f"Error: {INPUT_NAMES_FILE} not found.")
        return []


def read_starting_letter(name: str) -> str:
    """Returns 'starting letter' template"""
    try:
        with open(STARTING_LETTER_FILE, "r") as file:
            return file.read().replace("[name]", str(name))
    except FileNotFoundError:
        print(f"Error: {STARTING_LETTER_FILE} not found.")
        return ""


def write_to_files():
    """Creates personalized letters for each name."""
    names = list_names()

    if not names:
        print("Failed to personalize letters. Insufficient data.")
        return

    for name in names:
        with open(f"Output/ReadyToSend/letter_for_{name}.txt", "w") as file:
            file.write(read_starting_letter(name))

    print("Letters are ready to send!")


if __name__ == "__main__":
    write_to_files()
