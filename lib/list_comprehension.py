def return_evens(num_list):
    """Returns a list of even numbers from the given list."""
    return [num for num in num_list if num % 2 == 0]

def make_exclamation(sentence_list):
    """Returns a list of sentences with an exclamation mark added at the end."""
    return [sentence + "!" for sentence in sentence_list]
