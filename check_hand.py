def compare_files(file1_path, file2_path):
    try:
        with open(file1_path, 'r') as file1, open(file2_path, 'r') as file2:
            # Читаем содержимое файлов построчно
            lines1 = file1.readlines()
            lines2 = file2.readlines()

            # Находим первую строку, в которой происходит расхождение
            for i, (line1, line2) in enumerate(zip(lines1, lines2)):
                if line1 != line2:
                    print(f"Первое расхождение в строке {i + 1}:")
                    print(f"Файл 1: {line1.strip()}")
                    print(f"Файл 2: {line2.strip()}")
                    return

            # Если файлы идентичны
            print("Содержимое файлов идентично.")

            # Если файлы разной длины
            if len(lines1) != len(lines2):
                print("Файлы имеют разную длину.")
    except FileNotFoundError:
        print("Один из файлов не найден.")

# Пример использования:
file1_path = "std.out"
file2_path = "std2.out"
compare_files(file1_path, file2_path)
