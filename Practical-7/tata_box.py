# 伪代码 / Pseudocode

# 1. 导入 re 模块 / Import re module
#    用途：用于正则表达式匹配 TATA盒 / Purpose: For regex matching of TATA box

# 2. 导入 os 模块 / Import os module
#    用途：检查文件路径 / Purpose: Check file paths

# 3. 定义输入文件的绝对路径 / Define absolute path for input file
#    3.1 打印当前工作目录 / Print current working directory
#    3.2 检查文件是否存在 / Check if file exists
#    3.3 如果不存在，提示用户 / If not exists, notify user

# 4. 打开输入文件和输出文件 / Open input and output files
#    4.1 打开输入文件，读模式 / Open input file in read mode
#    4.2 打开输出文件，写模式 / Open output file in write mode

# 5. 初始化变量 / Initialize variables
#    5.1 定义 current_gene_name = '' 用于存基因名 / Define current_gene_name = '' to store gene name
#    5.2 定义 current_sequence = '' 用于存序列 / Define current_sequence = '' to store sequence

# 6. 逐行读取输入文件 / Read input file line by line
#    6.1 遍历每一行 / Loop through each line
#    6.2 去掉换行符 / Remove newline
#    6.3 如果行以 '>' 开头 / If line starts with '>'
#        6.3.1 如果 current_sequence 不为空 / If current_sequence is not empty
#            6.3.1.1 检查是否有 TATA盒（忽略大小写） / Check for TATA box (case insensitive)
#            6.3.1.2 如果有，写入输出文件 / If found, write to output file
#        6.3.2 检查行是否有 'gene_name=' / Check if line has 'gene_name='
#              如果有，提取 gene_name= 后的值 / If yes, extract value after gene_name=
#              如果没有，用行的第一个字段（去掉 '>'） / If no, use first field of line (remove '>')
#        6.3.3 重置 current_sequence / Reset current_sequence
#    6.4 否则 / Else
#        6.4.1 将行加到 current_sequence / Append line to current_sequence

# 7. 处理最后一条记录 / Process the last record
#    7.1 如果 current_sequence 不为空 / If current_sequence is not empty
#    7.2 检查是否有 TATA盒 / Check for TATA box
#    7.3 如果有，写入输出文件 / If found, write to output file

# 8. 关闭文件 / Close files
#    8.1 关闭输入文件 / Close input file
#    8.2 关闭输出文件 / Close output file

import re  # 导入正则表达式模块 / Import regex module for TATA box matching
import os  # 导入 os 模块 / Import os module for path checking

os.chdir("Practical-7") # Determine my path

# 定义输入文件的绝对路径 / Define absolute path for input file
print("Current working directory:", os.getcwd())  # 打印当前工作目录 / Print current working directory
filename = r'C:Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa'  # 输入文件绝对路径 / Absolute path to input file
if os.path.exists(filename):  # 检查文件是否存在 / Check if file exists
    print(f"File {filename} exists")
else:  # 如果文件不存在 / If file does not exist
    print(f"File {filename} does not exist")
    print("Please check if the path is correct")

# 打开输入文件和输出文件 / Open input and output files
input_file = open(filename, 'r')  # 打开输入文件，读模式 / Open input file in read mode
output_file = open(r'C:tata_genes.fa', 'w')  # 打开输出文件，写模式 / Open output file in write mode

# 初始化变量 / Initialize variables
current_gene_name = ''  # 当前基因名 / Current gene name
current_sequence = ''   # 当前序列 / Current sequence

# 逐行读取输入文件 / Read input file line by line
for line in input_file:
    line = line.strip()  # 去掉换行符 / Remove newline
    if line.startswith('>'):  # 如果行以 '>' 开头 / If line starts with '>'
        if current_sequence:  # 如果 current_sequence 不为空 / If current_sequence is not empty
            print(f"Checking sequence: {current_gene_name}, Length: {len(current_sequence)}")  # 检查序列并打印长度 / Check sequence and print length
            if re.search(r'TATA[AT]A[AT]', current_sequence, re.IGNORECASE):  # 检查 TATA盒，忽略大小写 / Check TATA box, case insensitive
                print(f"Found TATA box in: {current_gene_name}")  # 找到 TATA盒 / Found TATA box
                output_file.write(f'>{current_gene_name}\n{current_sequence}\n')  # 写入基因名和序列 / Write gene name and sequence
            else:
                print(f"No TATA box in: {current_gene_name}")  # 没找到 TATA盒 / No TATA box found
        # 检查有没有 'gene_name=' / Check if 'gene_name=' exists
        if 'gene_name=' in line:  # 如果有 'gene_name=' / If 'gene_name=' is present
            current_gene_name = line.split('gene_name=')[1].split()[0]  # 提取 gene_name= 后的值 / Extract value after gene_name=
        else:  # 如果没有 'gene_name=' / If 'gene_name=' is not present
            current_gene_name = line.split()[0][1:]  # 用第一个字段（去掉 '>'） / Use first field (remove '>')
            print(f"Warning: Line {line} has no gene_name=, using {current_gene_name}")  # 警告：没有 gene_name= / Warning: No gene_name=
        current_sequence = ''  # 重置 current_sequence / Reset current_sequence
    else:  # 如果不是 '>' 开头 / If line does not start with '>'
        current_sequence += line  # 将行加到 current_sequence / Append line to current_sequence

# 处理最后一条记录 / Process the last record
if current_sequence:  # 如果 current_sequence 不为空 / If current_sequence is not empty
    print(f"Checking last sequence: {current_gene_name}, Length: {len(current_sequence)}")  # 检查最后序列并打印长度 / Check last sequence and print length
    if re.search(r'TATA[AT]A[AT]', current_sequence, re.IGNORECASE):  # 检查 TATA盒，忽略大小写 / Check TATA box, case insensitive
        print(f"Found TATA box in: {current_gene_name}")  # 找到 TATA盒 / Found TATA box
        output_file.write(f'>{current_gene_name}\n{current_sequence}\n')  # 写入基因名和序列 / Write gene name and sequence
    else:
        print(f"No TATA box in: {current_gene_name}")  # 没找到 TATA盒 / No TATA box found

# 关闭文件 / Close files
input_file.close()  # 关闭输入文件 / Close input file
output_file.close()  # 关闭输出文件 / Close output file