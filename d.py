start = 253650917
from b import check
from a import getCode
from c import run_program
import asyncio
from e import getLinks
def read_input_data(filename):
    with open(filename, 'r') as file:
        return file.readlines()



input_file_name = 'std.in'
output_file_name = 'std2.out'

correct = read_input_data(output_file_name)

input_to_send = read_input_data(input_file_name)
    
for i in range(244, 1, -1):
    # print(i)
    links = getLinks(1)
    for pattern in links:
        try:
            url = f'https://codeforces.com{pattern["href"]}'

            # print(url)
            if check(url):
                # print(url)

                code = asyncio.run(getCode(url))
                # print(code)
                out_of_to_check = run_program(input_to_send, code)
                # print(out_of_to_check)
                # if out_of_to_check.upper() != correct.upper():
                #     print(url)
                
                list_ = out_of_to_check.upper().split('\n')
                
                for j in range(len(list_)):
                    if list_[j].strip() != correct[j].strip():
                        print(list_[j], " ", correct[j])
                        print(url)
                        break
                        
                    
                    # with open("test.out", 'w') as file:
                    #     file.write(out_of_to_check.upper())
                    # exit(0)
        except:
            pass 
        
# code = asyncio.run(getCode('https://codeforces.com/contest/1950/submission/253744351'))
# print(code)

# out_of_to_check = run_program("3 2", code)

# print(out_of_to_check)
# program_code = """
# #include <bits/stdc++.h>
# using namespace std;

# int main() {
#     vector<vector<int>>v;
#     cout << "Число: " << ""<< endl;
#     return 0;
# }
# """

# print(run_program("", program_code))
    
        
    
