
'''
(模拟龟兔赛跑)本练习中要模拟龟兔赛跑的寓言故事。用随机数产生器建立模拟龟兔赛跑的程序。
对手从70个方格的第1格开始起跑，每格表示跑道上的一个可能位置，终点线在第70格处。
第一个到达终点的选手奖励一个新鲜萝卜和莴苣。兔子要在山坡上睡一觉，因此可能失去冠军。
有一个每秒钟滴答一次的钟，程序应按下列规则调整动物的位置：


用变量跟踪动物的位置(即位置号1到70)。每个动物从位置1开始，如果动物跌到第1格以外，则移回第1格。
产生随机整数1≤i≤10)，以得到上表中的百分比。对于乌龟，1≤i≤5时快走，6≤i≤7时跌跤，8≤i≤10时慢走，
兔子也用相似的方法。
起跑时，打印：
BANG  !!!!!
AND THEY' RE OFF  !!!!!
时钟每次滴答一下(即每个重复循环)，打印第70格位置的一条线，显示乌龟的位置T和兔子的位置H。
如果两者占用一格，则乌龟会咬兔子，程序从该位置开始打印 OUCH!!!。
除T、H和OUCH!!!以外的其他打印位置都是空的。
打印每一行之后，测试某个动物是否超过了第70格，如果是,则打印获胜者，停止模拟。
如果乌龟赢，则打印TORTOISE WINS!!!YAY!!!。如果兔子赢，则打印Hare wins．Yush。
如果两个动物同时赢，则可以同情弱者，让乌龟赢，或者打印It's a tie。
如果两者都没有赢，则再次循环，模拟下一个时钟滴答。
准备运行程序时，让一组拉拉队看比赛，你会发现观众有多么投入。

'''
import time
from tqdm import  *

# 定义乌龟类
class Tortoise(object):
    # t:表示乌龟当前位置
    def __init__(self):
         self.t = 1

    def run(self):
         from random import  randint

         # 随机生成1-10的整数
         num = randint(1,10)
         if num >= 1 and num <= 5:
             self.t +=3
         elif num >=6 and num<=7:
             self.t -=6
         elif num>=8 and num<=10:
             self.t +=1

         if self.t<1:
             self.t=1
         #print("乌龟走到第%d格"%(self.t))


         return self.t

# 定义兔子类
class Rabbit(object):
    # h: 兔子当前位置
    def __init__(self):
        self.h=1

    def run(self):
        from random import  randint
        num = randint(1,10)


        if num >= 1 and num <= 2:
            self.h += 0
        elif num>=3 and num<=4:
            self.h += 9
        elif num == 5:
            self.h -= 12
        elif num >= 6 and num <= 8:
            self.h += 1
        elif num >=9 and num <= 10:
            self.h-=2

        if self.h < 1:
            self.h = 1
        #print("兔子走到第%d格"%(self.h))

        return  self.h

def main():
     END=70
     # 定义乌龟
     tortoise=Tortoise()
     # 定义兔子
     rabbit=Rabbit()

     bar=tqdm(range(END))

     while True:
      #每隔一秒中执行一次
      time.sleep(1)
      t=tortoise.run()
      h=rabbit.run()

      # for t  in bar:
      #      bar.set_description('乌龟的进度%d'%(t//END))
      # for h in tqdm(range(END)):
      #      pass

      if t==h and t<70:
          print("乌龟咬兔子!!!--OUCH")

      if t>=END:
          print("TORTOISE WINS!!!YAY!!!")
          return

      if h>=END:
          print("Hare wins．Yush!!!")
          return



if __name__ == '__main__':
    main()



































