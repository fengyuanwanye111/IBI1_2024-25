seq = 'ATGCAAGTGGTGTGTCTGTTCTGAGAGGGCCTAA'

# 伪代码 / Pseudocode
# 1. 定义序列变量 seq
#    Define the sequence variable seq
# 2. 创建两个空列表：gt_positions 和 ag_positions
#    Create two empty lists: gt_positions and ag_positions
# 3. 遍历序列，找到所有 GT 的位置，存入 gt_positions
#    Loop through the sequence, find all GT positions, store in gt_positions
# 4. 遍历序列，找到所有 AG 的位置，存入 ag_positions
#    Loop through the sequence, find all AG positions, store in ag_positions
# 5. 创建一个变量 max_length 初始化为 0
#    Create a variable max_length initialized to 0
# 6. 对每个 GT 位置：
#    For each GT position:
#    6.1 对每个在 GT 后面的 AG 位置：
#        For each AG position after GT:
#        6.1.1 计算内含子长度 = AG 位置 - GT 位置 + 1
#              Calculate intron length = AG position - GT position + 1
#        6.1.2 如果这个长度大于 max_length，更新 max_length
#              If this length is greater than max_length, update max_length
# 7. 输出 max_length
#    Print max_length

gt_positions = []
ag_positions = []
for i in range(len(seq) - 1):
    if seq[i:i+2] == "GT":  # 检查是否为 GT / Check if it's GT
        gt_positions.append(i)
    if seq[i:i+2] == "AG":  # 检查是否为 GT / Check if it's GT
        ag_positions.append(i)
print("GT positions:", gt_positions) # 测试用 / For testing
print("AG positions:", ag_positions) # 测试用 / For testing

max_length = 0
for gt in gt_positions:
    for ag in ag_positions:
        if ag > gt:  # 确保 AG 在 GT 后面 / Ensure AG is after GT
            intron_length = ag - gt + 2  # 计算长度 / Calculate length
            if intron_length > max_length:  # 更新最大长度 / Update max length
                max_length = intron_length
print("Largest intron length:", max_length)