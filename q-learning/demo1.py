import numpy as np
import random

#建立q表
q = np.zeros((6,6))
q = np.matrix(q)

#建立R表
r = np.array([[-1,-1,-1,-1,0,-1],
            [-1,-1,-1,0,-1,100],
            [-1,-1,-1,0,-1,-1],
            [-1,0,0,-1,0,-1],
            [0,-1,-1,0,-1,100],
            [-1,0,-1,-1,0,100]])
r = np.matrix(r)

#贪婪指数
gamma = 0.8

#开始训练,主要是生成q表
for i in range(1000):
    #对每一个训练，随机选择一种状态
    state = random.randint(0,5)
    while state != 5:
        #选择ｒ表中非负的值的动作
        r_pos_action = []
        for action in range(6):
            if r[state,action] >= 0:
                r_pos_action.append(action)
        next_state = r_pos_action[random.randint(0,len(r_pos_action)-1)]
        q[state,next_state] = r[state,next_state] + gamma*q[next_state].max()   #这边直接max就可以了
        state = next_state
print(q)

#验证代码部分
for i in range(10):
    print('第{}次验证'.format(i+1))
    #训练好q表，按照q表进行路径选择
    state = random.randint(0,5)
    print('机器人处于房间{}'.format(state))
    count = 0
    while state != 5:
        if count > 20:#如果尝试次数大于２０次，表示失败
            print('fail')
            break
        #选择最大的q_max
        q_max = q[state].max()

        q_max_action = []
        for action in range(6):
            if q[state,action] == q_max:#选择可行的下一个动作
                q_max_action.append(action)
        #随机选择一个可行的动作
        next_state = q_max_action[random.randint(0,len(q_max_action)-1)]
        print('the robot goes to '+str(next_state)+'.')
        state = next_state