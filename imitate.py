import random

# 输入抛硬币的次数
num_flips = int(input("请输入抛硬币的次数："))

# 初始化正面朝上的次数
num_heads = 0

# 模拟抛硬币并统计正面朝上的次数
for _ in range(num_flips):
    # 随机生成0或1，表示硬币的正反面
    result = random.randint(0, 1)
    if result == 1:
        num_heads += 1

# 计算正面朝上的概率
probability = num_heads / num_flips

# 打印结果
print("正面朝上的概率为：", probability)
