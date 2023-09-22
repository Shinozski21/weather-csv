with open("mytext.txt") as file:
    contents = file.read()
    print(contents)

with open("my_text2.txt", mode="a") as file:
    file.write("\nNew text.")

