sentence = input("문장: ")
find = input("찾을 단어: ")
lower_sentence = sentence.lower()
print("위치: %d"%lower_sentence.find(find))