def vowels(text, vowels = 'aeiou'):
    count = 0
    for i in text.lower():
        if i in vowels:
            count += 1
    return count
print(vowels('python is fun'))
