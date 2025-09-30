def get_num_words(file_contents):
    words = file_contents.split()
    return len(words)

def get_count_characters(file_contents):
    character_counter_dict = {}

    words = file_contents.lower().split()

    for word in words:
        for char in word:
            if char in character_counter_dict.keys():
                character_counter_dict[char] += 1
            else:
                character_counter_dict[char] = 1

    return character_counter_dict

def sort_count_characters(character_dictionary):
    return dict(sorted(character_dictionary.items(), key=lambda x: x[1], reverse=True))
