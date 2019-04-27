import sys
import collections

commandNum = int(input())
queue = collections.deque()

for i in range(commandNum):
    command = sys.stdin.readline()

    if 'push' in command:
        queue.appendleft(command.split()[1])
    elif 'pop' in command:
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.pop())
    elif 'size' in command:
        print(len(queue))
    elif 'empty' in command:
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif 'front' in command:
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])
    elif 'back' in command:
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])


'''

#include<stdio.h>
#include<stdlib.h>
#include<string.h>
//
void Push(int Q[], int X);
void Pop(int Q[]);
void Size(int Q[]);
void Empty(int Q[]);
void Front(int Q[]);
void Back(int Q[]);

int main()
{
   int get;//반복 횟수
   char ch[6];//명령 받을 변수
   int push=0;//push할때 정수 저장할변수
   int *que = NULL;
   scanf("%d", &get);
   que = malloc(sizeof(int)*get);
   for (int i = 0; i < get; i++)
      que[i] = -1;
   for (int i = 0; i < get; i++)
   {
      scanf("%s", &ch);
      if (strcmp(ch, "push") == 0)
      {
         scanf("%d", &push);
         Push(que, push);
      }
      else if (strcmp(ch, "pop") == 0)
         Pop(que);
      else if (strcmp(ch, "size") == 0)
         Size(que);
      else if (strcmp(ch, "empty") == 0)
         Empty(que);
      else if (strcmp(ch, "front") == 0)
         Front(que);
      else if (strcmp(ch, "back") == 0)
         Back(que);
   }

}

//Push X 정수X를 큐에 넣음
void Push(int Q[], int X)
{
   int i = 0;
   while (1)
   {
      if (Q[i] == -1)
      {
         Q[i] = X;
         break;
      }
      else
         i++;
   }
}
//Pop 큐의 가장 앞의 수를 빼고 그 수를 출력한다 정수없으면 -1출력
void Pop(int Q[])
{
   int po = Q[0];
   int i = 0;
   while (1)
   {
      if (Q[i] != -1)
      {
         Q[i] = Q[i + 1];
         i++;
      }
      else break;
   }
   printf("%d\n", po);
}
//Size 큐에 들어있는 정수의개수를 출력
void Size(int Q[])
{
   int i = 0;
   while (Q[i] != -1)
      i++;
   printf("%d\n", i);
}
//Empty 큐가 비어있으면 1 아니면 0을 출력한다
void Empty(int Q[])
{
   if (Q[0] == -1)
      printf("1\n");
   else
      printf("0\n");
}
//Front 큐의 가장 앞에 있는 정수를 출력한다 정수가 없으면 -1을 출력
void Front(int Q[])
{
   printf("%d\n", Q[0]);
}
//Back 큐의 가정 뒤에있는 정수를 출력 정수가 없으면 -1을 출력
void Back(int Q[])
{
   int i = 0;
   while (1)
   {
      if (Q[i] != -1)
      {
         i++;
      }
      else
      {
         if (i == 0)
         {
            printf("%d\n", Q[i]);
            break;
         }
         else
         {
            printf("%d\n", Q[i - 1]);
            break;
         }
      }
   }
}

'''