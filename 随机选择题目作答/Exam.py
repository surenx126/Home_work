import random
from Question_Bank import *     #调用题库


Q1 = dict(question = NO_1,answer = Answer_1)    # 将题目和答案放到一个字典里
Q2 = dict(question = NO_2,answer = Answer_2)
Q3 = dict(question = NO_3,answer = Answer_3)
Q4 = dict(question = NO_4,answer = Answer_4)
Q5 = dict(question = NO_5,answer = Answer_5)
q_bank = [Q1,Q2,Q3,Q4,Q5]       # 将字典放到一个列表里。生成题库和答案列表

questions = random.sample(q_bank,3)     # 从列表随机抽取3道题，并且不重复

your_score = 0
for i in range(0,len(questions)):
    print(questions[i]['question'])     # 打印题目
    options = ['A','B','C','D','AB','AC','AD','BC','BD','CD','ABC','ABD','ACD','BCD','ABCD']    # 定义答案的所有组合，不知道是否有自动将字符串组合的方法
    your_choice = input('Choice the answer: ').upper()      # 将字符串中的小写字母转为大写字母
    if your_choice in options:
        correct = your_choice == questions[i]['answer']
        if correct:
            your_score = your_score + 1     # 答对成绩加1
    else:
        print('Invalid Words')
if your_score >= 2:
    print('PASS')
    result = 'PASS'
else:
    print('FAIL')
    result = 'FAIL'

with open('Exam.txt','a+') as f:
    f.write(result)
    f.write('\n')
