def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents


def number_of_characters(text):
    lower_text = text.lower()
    character_count = {}
    for ch in lower_text:
        if ch in character_count:
            character_count[ch] += 1
        else:
            character_count[ch] = 1
    return character_count

def sort_on(item):
    return item["num"]

def sorter(counts):
    result = []
    for ch, num in counts.items():
        result.append({"char": ch, "num": num})
    result.sort(reverse=True, key=sort_on)
    return result
