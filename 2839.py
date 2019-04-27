kg = int(input())
if kg >= 5:
    num5 = kg // 5
    num5na = kg % 5
    if num5na != 0:
        while True:
            num3 = num5na // 3
            num3na = num5na % 3
            if num3na != 0:
                if num5 == 0:
                    print(-1)
                    break
                else:
                    num5 -= 1
                    num5na += 5
            else:
                print(num5 + num3)
                break
    else:
        print(num5)
elif kg == 3:
    print(1)
else:
    print(-1)

'''
include<stdio.h>
#include<stdlib.h>
#include<time.h>
int main()
{
	int get;
	scanf("%d", &get);
	int box5 = 0, box3 = 0;
	box5 = (get / 5);
	get %= 5;
	int c=0;
	while (1)
	{
		if (get == 0)
		{
			break;
		}
		else if (get % 3 == 0)
		{
			get -= 3;
			box3++;
		}
		else if (get != 0)
		{
			if (box5 != 0)
			{
				get += 5;
				box5--;
			}
			else if (box5 == 0 && get != 0)
			{
				c = box5 + box3 + 1;
				break;
			}
		}
	}
	printf("%d", box5 + box3-c);
'''