import string

#Function to remove the punctuation in the text from the file
def remove_punctuation(input_string):
    translator = str.maketrans('', '', string.punctuation)
    return input_string.translate(translator)

#Function to sort and display the result
def top_10(words, count):
    for item in range(len(count) - 1):
        index = item
        while index >= 0 and count[index] < count[index + 1]:
            count.insert(index, count[index + 1])
            words.insert(index, words[index + 1])
            count.pop(index + 2)
            words.pop(index + 2)
            index -= 1
    for i in range(10):
         if i < len(words):
            print(words[i], count[i])

#Open the file, then remove the punctuation and add the line from file to list
file = open("Example.txt")
text = remove_punctuation(file.read()).lower().split()

#Creating a list of found words and their number in the text
result_list_words = list()
result_list_count = list()

#Finding words in the text and counting them
for index in range(len(text) - 1):
    target_list = list()
    target_list.append(text[index])
    target_list.append(text[index + 1])

    count = 0
    for target_index in range(len(text) - 1):
        if target_list[0] + target_list[1] == text[target_index] + text[target_index + 1]:
            count += 1    

    if count > 1 and result_list_words.count(target_list[0] + " " + target_list[1]) == 0:
            result_list_words.append(target_list[0] + " " + target_list[1])
            result_list_count.append(count)

top_10(result_list_words, result_list_count)