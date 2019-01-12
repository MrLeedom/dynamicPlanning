'''
这是一个组装背包的案例问题,类似q表的感觉
'''
import numpy as np

#定义重量
weight = {}
weight['water'] = 3
weight['book'] = 1
weight['food'] = 2
weight['jacket'] = 2
weight['camera'] = 1

#定义价值
worth = {}
worth['water'] = 10
worth['book'] = 3
worth['food'] = 9
worth['jacket'] = 5
worth['camera'] = 6

#存放行标对应的物品名
table_name = {}
table_name[0] = "water"
table_name[1] = 'book'
table_name[2] = 'food'
table_name[3] = 'jacket'
table_name[4] = 'camera'

#创建矩阵,用来保存价值表
table = np.zeros((len(weight),6))

#创建矩阵，用来保存每个单元格中的价值是如何得到的（物品名）
table_class = np.zeros((len(weight),6),dtype=np.dtype((np.str_,500)))

for i in range(0,len(weight)):
    for j in range(0,6):
        #获取重量
        this_weight = weight[table_name[i]]
        #获得价值
        this_worth = worth[table_name[i]]
        #获取上一个单元格(i-1,j)的值
        if(i>0):
            before_worth = table[i-1,j]
            #获取(i-1,j-重量)
            temp = 0
            if(this_weight<=j):
                temp = table[i-1][j-this_weight]
            #(i-1,j-this_weight)＋求当前商品价值
            #判断this_worth能不能用，即重量有没有超标，如果重量超标了是不能加的
            synthesize_worth = 0
            if(this_weight-1<=j):
                synthesize_worth = this_worth + temp
            #与上一个单元格比较，哪个大写入哪个
            if(synthesize_worth > before_worth):
                table[i,j] = synthesize_worth
                if(temp == 0):
                    #他自己就超过了
                    table_class[i][j] = table_name[i]
                else:
                    #他自己和(i-1,j-this_weight)
                    table_class[i][j] = table_name[i] + ',' +table_class[i-1][j-this_weight]
            else:
                table[i][j] = before_worth
                table_class[i][j] = table_class[i-1][j]
        else:
            #没有(i-1,j)，那更没有(i-1,j-重量)，就等于当前商品价值，或者重量不够
            if(this_weight<= j+1):
                table[i][j] = this_worth
                table_class[i][j] = table_name[i]
print(table)
print('=====================')
print(table_class)