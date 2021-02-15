import string
import exercice_test
from collections import Counter

exercice_test.book = exercice_test.book.translate(str.maketrans('', '', string.punctuation))
exercice_list = (exercice_test.book.split())

book_count = dict(Counter(exercice_list))
print(book_count)

sentence_wanted_not_gud = "I want the money bitch"
sentence_wanted_working = "road speek nice minites"
sentence_wanted_more_occ = "breeding breeding breeding"

def check_sentence(sentence):
    split_sentence = (sentence.split())
    words_count = dict(Counter(split_sentence))
    print(words_count.items() <= book_count.items())


check_sentence(sentence_wanted_not_gud)
check_sentence(sentence_wanted_working)
check_sentence(sentence_wanted_more_occ)
