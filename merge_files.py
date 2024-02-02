import os

def merge_files(files):
    result = []
    for file in files:
        with open(os.path.join("C:\\Users\\Abu Aisha\\OneDrive\\Рабочий стол\\Git&GitHub Netology\\HW_5", file), 'r') as f:
            content = f.readlines()
            result.append((file, len(content), content))
    result.sort(key=lambda x: x[1])
    with open('result.txt', 'w') as f:
        for file, lines, content in result:
            f.write(f"{file}\n{lines}\n")
            f.writelines(content)
            f.write('\n')

files = ['1.txt', '2.txt']
merge_files(files)
