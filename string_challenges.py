# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[len(word)-1])

# Вывести количество букв а в слове
word = 'Архангельск'
total = 0
for letter in word:
    if letter.lower() == "а":
        total +=1
print(total)	

# Вывести количество гласных букв в слове
word = 'Архангельск'
total = 0
for letter in word:
    if letter.isalpha():
        if letter.lower() in 'аеёиоуыэюя':
                total += 1
print(total)

# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
print(sentence.count(" ") + 1)  


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
count = 0
print(sentence[0],'\n')
for letter in sentence:
    if letter == " ":
	count = 1
    elif count = 1:
 	print(letter,"\n")
	count = 0		

# Вывести усреднённую длину слова.
sentence = 'Мы приехали в гости'
mediana = (len(sentence) - sentence.count(" ")) / (sentence.count(" ") + 1)  
print(mediana)