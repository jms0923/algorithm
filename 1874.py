import sys

lastNum = int(sys.stdin.readline())
goalList = []
ascendingOrder = []
pushNum = 1
printList = []

goalList = [int(sys.stdin.readline()) for i in range(lastNum)]
# for i in range(lastNum):
#     goalList.append(int(sys.stdin.readline()))

while goalList:
    if ascendingOrder:
        if goalList[0] == ascendingOrder[-1]:
            goalList.pop(0)
            ascendingOrder.pop()
            printList.append('-')
        elif goalList[0] < ascendingOrder[-1]:
            printList.append('NO')
            break
        else:
            ascendingOrder.append(pushNum)
            pushNum += 1
            printList.append('+')

    elif not ascendingOrder:
        ascendingOrder.append(pushNum)
        pushNum += 1
        printList.append('+')

if 'NO' not in printList:
    for i in printList:
        print(i)
else:
    print('NO')



'''

class Stack(object):

    def __init__(self):
        self.stack_data = []
        self.stack_size = 0

    def push(self, x):
        self.stack_data.append(x)
        self.stack_size += 1

    def pop(self):
        try:
            a = self.stack_data.pop()
            self.stack_size -= 1
        except:
            print(-1)

    def size(self):
        return self.stack_size

    def empty(self):
        if self.stack_size:
            return 0
        else:
            return 1

    def top(self):
        if self.stack_size:
            return self.stack_data[-1]
        else:
            return 0

import sys
v = Stack()
n = int(input())
res = [int(sys.stdin.readline()) for _ in range(n)]
out = []
i = j = 0
while(True):
    if v.top() == res[j]:
        v.pop()
        out.append('-')
        j += 1
        if j == n:
            print('\n'.join(out))
            break
    else:
        i += 1
        if i > n:
            print('NO')
            break
        out.append('+')
        v.push(i)

'''

'''

#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<malloc.h>
int main()
{
   int *arr = NULL;//스택 쌓을 변수
   int get;//반복횟수
   char GET[6];//명령어 받기
   int x;//push 정수받는 변수
   int stack=-1;//스택 쌓을 변수
   scanf("%d", &get);
   
   arr = malloc(sizeof(int)*get);
   for (int i = 0; i < get; i++)
      arr[i] = -1;
   for (int i = 0; i < get; i++)
   {
      scanf("%s", &GET);
      if (strcmp(GET,"push")==0)
      {
         stack++;
         scanf("%d", &x);
         arr[stack] = x;
         
      }
      else if (strcmp(GET,"pop")==0)
      {
         if (stack == -1)
         {
            printf("-1\n");
         }
            
         else
         {
            printf("%d\n", arr[stack]);
            arr[stack] = -1;
            stack--;
         }
      }
      else if (strcmp(GET, "size") == 0)
      {
         if (stack == -1)
         {
            printf("0\n");
         }
         else
         {
            printf("%d\n", stack+1);
         }
      }
      else if (strcmp(GET, "empty") == 0)
      {
         if (stack == -1)
            printf("1\n");
         else if (arr[stack] == -1)
            printf("1\n");
         else
            printf("0\n");
      }
      else if (strcmp(GET, "top") == 0)
      {
         if (stack == -1)
            printf("-1\n");
         else
            printf("%d\n", arr[stack]);
      }
   }
   free(arr);
}


'''