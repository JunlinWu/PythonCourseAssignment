# coding=utf-8
# 上面这行的作用是为了可以在该编译环境下顺利地使用中文注释



##### 八皇后问题解集求解 #####
# 引入排列函数（permutations）所在的内建模块itertools（迭代工具）
import itertools

# 考虑到按照每格有棋子或无棋子完全穷举棋盘状态则需要2^64次穷举数量实在过于庞大，故首先对穷举初始集进行"同行同列仅有一枚棋子"的约束
# 故用向量的形式（索引表示顺序八行rows：(&0, &1, &2, &3, &4, &5, &6, &7)，对应数字表示该行的某列上填有棋子）表示棋盘状态
# 棋盘状态存于向量cols中
# 例如cols = (0, 4, 7, 5, 2, 6, 1, 3)则表示棋盘从第一行到第八行分别在第1, 5, 8, 6, 3, 7, 2, 4列放有八个棋子

# 由此则可首先用range简单构造第一个例子，然后对其用全排列则可导出所有的满足"同行同列仅有一枚棋子"约束的棋盘状态，作为穷举初始集
# 第一个例子由自己随便输入一个例子也可以，如：cols = [0, 4, 1, 5, 3, 2, 7, 6]
cols = range(8)

# 全排列函数使用itertools中的permutations
# 设八皇后问题的解集为：Answers
Answers = []
n = 0
for ans in itertools.permutations(cols):
  if (8 == len(set(ans[i] + i for i in cols)) == len(set(ans[i] - i for i in cols))):
           #分别排除 左下&右上角的对角线 和 左上&右下角的对角线
    Answers.insert(n, ans)
    n = n + 1

# 打印解集Answers
# print Answers

print "八皇后问题的所有解如下："
for ans in Answers:
  print ans
print "共有", len(Answers), "组解。\n"



##### 最小步数求解 #####
# 给定一个棋盘状态mycols（输入式）
# mycols = (0, 0, 0, 0, 0, 0, 0, 0)  # 需要走7步
# mycols = (5, 5, 5, 5, 5, 5, 5, 5)  # 需要走7步
# mycols = (0, 1, 2, 3, 4, 5, 6, 7)  # 需要走7步
# mycols = (0, 4, 7, 5, 2, 6, 1, 3)  # 需要走0步
# mycols = (0, 4, 3, 5, 2, 6, 1, 3)  # 需要走1步
# mycols = (0, 4, 3, 5, 2, 3, 1, 4)  # 需要走3步

# 给定一个棋盘状态mycols（随机式）
import random
mycols = (random.randint(0, 7), random.randint(0, 7), random.randint(0, 7), random.randint(0, 7), random.randint(0, 7), random.randint(0, 7), random.randint(0, 7), random.randint(0, 7))

print "给定棋盘状态为：", mycols

# 设最小步数为step，因为有八行共八个棋子，调整一行只需一步，任何一种棋盘模式通过调整所有八行一定可以完成变换，故step的最大值不超过8
# 对比全解集，给定棋盘状态中有几个位置的值与解值对不上的就代表需要调整几步，由此求出全解集范围内最小
step = 8
step_ans = []
for ans in Answers:
  m = 0
  for i in range(8):
    if (mycols[i] != ans[i]):
      m = m + 1
  if (m < step):
    step = m
    step_ans = ans
    # print step
    # print ans
print "对应最小步数为：", step, "；其调整好后的八皇后解为：", step_ans



print "\n注释：由于棋盘可以旋转，故以上结果可拓展为所有情况。"