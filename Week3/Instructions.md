# Exercise #1

In this exercise, you will analyze the file reading performance for three different cases. Your task is to create three different functions that open a text file (approximately 10MB in size) and read it in the following ways:

- **Function #1:** Reads the file character by character.
- **Function #2:** Reads the file line by line.
- **Function #3:** Reads the file in blocks of 4096 bytes (4KB).

You should print on the screen the time it took for each function to complete its task. Are you surprised by the results? Why is there a difference between each of the functions?

Note: To create text files of that size, you can create a file as follows:

```python
with open("large_text.txt", "w") as f:
    for _ in range(230000):  # ~10MB total
        f.write("The quick brown fox jumps over the lazy dog.\n")
```

# Exercise #2

Write a Python program that allows you to save and retrieve a list of dictionaries from a binary file. You are free to create the structure and add any data you want, as long as it is a list of dictionaries. For example:

```python
list_of_dicts = [ 
    {"a":"10", "b":"20"}, 
    {"c":"30", "d":"40"}, 
    {"e":"50", "f":"60"} 
    ]
```