text = "Information Technology Program, College of Computing"

char_count = {}
cleaned_text = ''.join(filter(str.isalnum, text))
cleaned_text = cleaned_text.upper()

for char in cleaned_text:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

sorted_char_count = sorted(char_count.items(), key=lambda x: (-x[1], x[0]))


for char, count in sorted_char_count:
    print(f"{char}: {count}")
