import easyocr
import os
import csv

directory = "app/model/train"
files = os.listdir(directory)
print(files)

def text_recognition(file_path, text_file_name="result.csv"):
    reader = easyocr.Reader(["ru"])
    result = reader.readtext(file_path, detail=0, paragraph=False)

    with open(text_file_name, 'w') as file:
            csv.writer(file).writerows(result)

    return result

def main():
    for path in files:
        file_path = "app/model/train/" + path
        print(text_recognition(file_path=file_path))

if __name__ == "__main__":
    main()