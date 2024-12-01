#Check if a String Is an Acronym of Words

words = ["alice","bob","charlie"]
s = "abc"

if len(words)!= len(s):
    print(False)
else:
    for i,word in enumerate(words):
        print(s[i], word[0])
        if s[i] != word[0]:
            print(False)
            break

print(True)

