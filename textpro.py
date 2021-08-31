def is_question(sentence: str):
    question_words = ('how', 'why', 'what', 'who', 'when')
    sentence = sentence.lower()

    return sentence.startswith(question_words)


result = []
while True:
    says = input("Say something: ")
    if says == "\end":
        print(" ".join(result))
        break
    else:
        punctuation = '?' if is_question(says) else '.'
        result.append(says.capitalize() + punctuation)
        continue
