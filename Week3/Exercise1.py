import time  # Import the time module for measuring execution time

# Path of the file we are going to read
FILE = "large_text.txt"

def time_function(func, label):
    start = time.time()
    func()
    end = time.time()
    print(f"Time taken to {label}: {end - start} seconds")

def read_by_characters():
    with open(FILE, mode="r") as file:
        while file.read(1):
            pass

def read_by_lines():
    with open(FILE, mode="r") as file:
        while file.readline():
            pass

def read_by_chunks():
    with open(FILE, mode="r") as file:
        while file.read(4096):
            pass

if __name__ == "__main__":
    time_function(read_by_characters, "read by characters")
    time_function(read_by_lines, "read by lines")
    time_function(read_by_chunks, "read by chunks")