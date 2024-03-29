# import subprocess

# # Функция для выполнения программы с заданным входом и получения её вывода
# def run_program(input_data, program_code):
#     # Компилируем программный код в памяти
#     # compile_process = subprocess.Popen(['g++', '-x', 'c++', '-o', 'temp_program', '-'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
#     compile_process = subprocess.Popen(['g++', '-std=c++17','-x', 'c++', '-o', 'temp_program', '-'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
#     _, compile_stderr = compile_process.communicate(input=program_code)

#     # if compile_stderr:
#     #     return f"Ошибка компиляции:\n{compile_stderr}"

#     # Выполняем программу
#     run_process = subprocess.Popen(['./temp_program'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
#     stdout, stderr = run_process.communicate(input=input_data)

#     return stdout.strip()

# # Пример входных данных и кода программы
# # input_data = "5\n"
# # program_code = """
# # #include <iostream>
# # using namespace std;

# # int main() {
# #     int n;
# #     cin >> n;
# #     cout << "Число: " << n << endl;
# #     return 0;
# # }







import subprocess

# Функция для выполнения программы с заданным входом и получения её вывода
def run_program(input_data, program_code):
    # Пример входного файла с данными
    input_data_file = 'std.in'

    # Чтение входных данных из файла
    input_data = read_data_from_file(input_data_file)
    # Компилируем программный код в памяти
    compile_process = subprocess.Popen(['g++', '-std=c++17', '-x', 'c++', '-o', 'temp_program', '-'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    _, compile_stderr = compile_process.communicate(input=program_code)

    # if compile_stderr:
    #     return f"Ошибка компиляции:\n{compile_stderr}"

    # Выполняем программу
    run_process = subprocess.Popen(['./temp_program'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    stdout, stderr = run_process.communicate(input=input_data)

    return stdout.strip()

# Функция для чтения данных из файла
def read_data_from_file(filename):
    with open(filename, 'r') as file:
        return file.read()



# Пример программного кода (в данном случае, он остается без изменений)
# program_code = """
# #include <iostream>
# using namespace std;

# int main() {
#     int n;
#     cin >> n;
#     cout << "Число: " << n << endl;
#     return 0;
# }
# """

# # Выполняем программу с входными данными из файла
# output = run_program(input_data, program_code)
# print('Результат работы программы:')
# print(output)
