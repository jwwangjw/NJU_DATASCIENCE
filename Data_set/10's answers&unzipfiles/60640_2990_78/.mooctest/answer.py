#include <stdio.h>

#include <stdlib.h>

#include<string.h>

int main()

{

    char buf1[20],buf2[10];       //这里没有考虑是否buf1的空间是否够加上buf2，默认够。。。考虑的更详细，应该用数据                                                      结构里面的知识；

    scanf("%s%s",buf1,buf2);

    strcat(buf1,buf2);

    puts(buf1);

    return 0;

}