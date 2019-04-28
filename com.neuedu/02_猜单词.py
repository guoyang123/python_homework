
'''
需求
给定单词数组（不少于10个），程序随机选择其中的一个，并显示单词字符长度个横线（-），用户有5次猜测机会，用户每次猜一个字母，如果正确，则将在相应的位置上显示出来；如错误则猜测机会减一，重复该过程，直至单词的全部字母全部猜出或者猜测次数用完，最后宣布用户胜利或失败。
实例
例如随机选出的单词是apple，程序先打印- - - - -
用户输入p，程序打印
-pp--
用户输入e，程序打印
-pp-e
用户输入t，程序打印
-pp-e
您还有4次机会
用户输入a，程序打印
app-e
用户输入l，程序打印
apple
恭喜您，取得胜利。
任务注意事项
请注意代码风格的整齐、优雅
代码中含有必要的注释


'''
from random import  randint
# 判断给定的字符，在指定的字符串中是否存在及存在的位置
def position(str,c):
    indexs=[]
    if c in str:
       _index=str.index(c)
       indexs.append(_index)
       beforeIndex = _index
       while True:
           substr=str[beforeIndex+1:len(str)]
           if c in substr:
               _index=substr.index(c)

               beforeIndex+=_index+1
               indexs.append(beforeIndex)
           else :
               return indexs

    return indexs



def  guessWord():
     words=['apple','orange','banana','peach','lemon','pear','avocado','mango','mandarin','pomegranate']
     index=randint(0,9)
     word=words[index]
     print(word)
     preWord = ["-" for _ in range(len(word))]
     for _ in range(len(preWord)):
         print("-",end="")
     print("")
     total=5

     while True:
         print("")
         c=input("请输入一个字符")
         if len(c)>1:
             total-=1
             print("只能输入一个字符，浪费了一次机会还剩%d次机会"%(total))
             continue
         else:

             indexsInword=position(word,c)
             if indexsInword.__len__()>0:
                 for replaceIndex in range(indexsInword.__len__()):
                     preWord[indexsInword[replaceIndex]]=c

             else :
                 total-=1
                 print("输出的字符错误，还剩%d次机会"%(total))
         for x in range(len(preWord)):
             print(preWord[x], end="")

         if total==0:
             print("game over,很遗憾，挑战失败!")
             return

         isSucc=True
         for x in range(len(preWord)):
             if preWord[x]!=word[x]:
                 isSucc=False

         if isSucc:
             print("")
             print("恭喜，挑战成功！！！")
             return


if __name__ == '__main__':
    guessWord()
