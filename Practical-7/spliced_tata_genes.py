# 伪代码 / Pseudocode

# 1. 导入 re 模块 / Import re module
#    用途：匹配剪接组合和 TATA盒 / Purpose: Match splice combo and TATA box

# 2. 导入 os 模块 / Import os module
#    用途：检查文件路径 / Purpose: Check file paths

# 3. 获取用户输入的剪接组合 / Get user input for splice combination
#    3.1 定义输出文件名 / Define output filename based on input

# 4. 定义输入文件的绝对路径 / Define absolute path for input file
#    4.1 检查文件是否存在 / Check if file exists

# 5. 打开输入文件和输出文件 / Open input and output files
#    5.1 打开输入文件，读模式 / Open input file in read mode
#    5.2 打开输出文件，写模式 / Open output file in write mode

# 6. 初始化变量 / Initialize variables
#    6.1 定义 current_gene_name = '' / Define current_gene_name = ''
#    6.2 定义 current_sequence = '' / Define current_sequence = ''

# 7. 逐行读取输入文件 / Read input file line by line
#    7.1 遍历每一行 / Loop through each line
#    7.2 去掉换行符 / Remove newline
#    7.3 如果行以 '>' 开头 / If line starts with '>'
#        7.3.1 如果 current_sequence 不为空 / If current_sequence is not empty
#            7.3.1.1 定义剪接模式（如 GT.*AG） / Define splice pattern (e.g., GT.*AG)
#            7.3.1.2 检查是否有剪接模式和 TATA盒 / Check for splice pattern and TATA box
#            7.3.1.3 如果都有，计算 TATA盒数量并写入 / If both exist, count TATA boxes and write
#        7.3.2 检查行是否有 'gene_name=' / Check if line has 'gene_name='
#              如果有，提取 gene_name= 后的值 / If yes, extract value after gene_name=
#              如果没有，用行的第一个字段（去掉 '>'） / If no, use first field (remove '>')
#        7.3.3 重置 current_sequence / Reset current_sequence
#    7.4 否则 / Else
#        7.4.1 将行加到 current_sequence / Append line to current_sequence

# 8. 处理最后一条记录 / Process the last record
#    8.1 如果 current_sequence 不为空 / If current_sequence is not empty
#    8.2 检查剪接模式和 TATA盒 / Check splice pattern and TATA box
#    8.3 如果都有，计算 TATA盒数量并写入 / If both exist, count TATA boxes and write

# 9. 关闭文件 / Close files
#    9.1 关闭输入文件 / Close input file
#    9.2 关闭输出文件 / Close output file

import re  # 导入正则表达式模块 / Import regex module
import os  # 导入 os 模块 / Import os module

os.chdir("Practical-7") # Determine my path

# 获取用户输入的剪接组合 / Get user input for splice combination
splice_combo = input("Enter splice combination (GTAG, GCAG, ATAC): ")
output_filename = f"{splice_combo}_spliced_genes.fa"  # 定义输出文件名 / Define output filename

# 定义输入文件的路径 / Define path for input file
input_filename = r'Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa'
if os.path.exists(input_filename):  # 检查文件是否存在 / Check if file exists
    print(f"Input file {input_filename} exists")
else:  # 如果文件不存在 / If file does not exist
    print(f"Input file {input_filename} does not exist")
    print("Please check the path")

# 打开输入文件和输出文件 / Open input and output files
input_file = open(input_filename, 'r')  # 打开输入文件，读模式 / Open input file in read mode
output_file = open(os.path.join(r'C:\Users\10403\Desktop\IBI1_2024-25\Practical-7', output_filename), 'w')  # 打开输出文件，写模式 / Open output file in write mode

# 初始化变量 / Initialize variables
current_gene_name = ''  # 当前基因名 / Current gene name
current_sequence = ''   # 当前序列 / Current sequence

# 逐行读取输入文件 / Read input file line by line
for line in input_file:
    line = line.strip()  # 去掉换行符 / Remove newline
    if line.startswith('>'):  # 如果行以 '>' 开头 / If line starts with '>'
        if current_sequence:  # 如果 current_sequence 不为空 / If current_sequence is not empty
            splice_pattern = splice_combo[:2] + '.*' + splice_combo[2:]  # 定义剪接模式 / Define splice pattern
            if re.search(splice_pattern, current_sequence, re.IGNORECASE) and re.search(r'TATA[AT]A[AT]', current_sequence, re.IGNORECASE):  # 检查剪接和 TATA盒 / Check splice and TATA box
                tata_count = len(re.findall(r'TATA[AT]A[AT]', current_sequence, re.IGNORECASE))  # 计算 TATA盒数量 / Count TATA boxes
                output_file.write(f'>{current_gene_name} TATA_count={tata_count}\n{current_sequence}\n')  # 写入结果 / Write result
        # 检查有没有 'gene_name=' / Check if 'gene_name=' exists
        if 'gene_name=' in line:  # 如果有 'gene_name=' / If 'gene_name=' is present
            current_gene_name = line.split('gene_name=')[1].split()[0]  # 提取 gene_name= 后的值 / Extract value after gene_name=
        else:  # 如果没有 'gene_name=' / If 'gene_name=' is not present
            current_gene_name = line.split()[0][1:]  # 用第一个字段（去掉 '>'） / Use first field (remove '>')
            print(f"Warning: Line {line} has no gene_name=, using {current_gene_name}")
        current_sequence = ''  # 重置 current_sequence / Reset current_sequence
    else:  # 如果不是 '>' 开头 / If line does not start with '>'
        current_sequence += line  # 将行加到 current_sequence / Append line to current_sequence

# 处理最后一条记录 / Process the last record
if current_sequence:  # 如果 current_sequence 不为空 / If current_sequence is not empty
    splice_pattern = splice_combo[:2] + '.*' + splice_combo[2:]  # 定义剪接模式 / Define splice pattern
    if re.search(splice_pattern, current_sequence, re.IGNORECASE) and re.search(r'TATA[AT]A[AT]', current_sequence, re.IGNORECASE):  # 检查剪接和 TATA盒 / Check splice and TATA box
        tata_count = len(re.findall(r'TATA[AT]A[AT]', current_sequence, re.IGNORECASE))  # 计算 TATA盒数量 / Count TATA boxes
        output_file.write(f'>{current_gene_name} TATA_count={tata_count}\n{current_sequence}\n')  # 写入结果 / Write result

# 关闭文件 / Close files
input_file.close()  # 关闭输入文件 / Close input file
output_file.close()  # 关闭输出文件 / Close output file