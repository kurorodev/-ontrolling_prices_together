import easyocr
import os

directory = "train"
files = os.listdir(directory)
print(files)

def text_recognition(file_path, text_file_name="result.csv"):
    reader = easyocr.Reader(["ru", "en"])
    result = reader.readtext(file_path, allowlist="0123456789", detail=0, paragraph=False)

    with open(text_file_name, "w") as file:
        for line in result:
            file.write(f"{line}")

    return result

def main():
    for path in files:
        file_path = "train/" + path
        print(text_recognition(file_path=file_path))

if __name__ == "__main__":
    main()