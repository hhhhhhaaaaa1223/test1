# Open the file in read mode
file_path = '/c:/Users/gina.huynh/test1/test1/topic-02.txt'  # Replace with your file path
try:
    with open(file_path, 'r') as file:
        # Read the contents of the file
        data = file.read()
        print(data)  # You can modify this line to process the data as needed
except FileNotFoundError:
    print(f"File '{file_path}' not found.")