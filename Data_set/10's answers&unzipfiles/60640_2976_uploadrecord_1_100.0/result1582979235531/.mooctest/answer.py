#include <stdio.h>

#include <stdlib.h>

#include <string.h>





char *remove_sub(char *s, char *sub){

	int len_s, len_sub, i, j;

	char *ns;

	len_s = strlen(s);

	len_sub = strlen(sub);

	for(i = 0; i <= len_s - len_sub;){

		for(j = 0 ; j < len_sub; ++j){

			if(s[i + j] == sub[j] || s[i + j] >= 'a' && s[i + j] <= 'z' && sub[j] >= 'A' && sub[j] <= 'Z' && s[i + j] - 'a' == sub[j] - 'A'

				|| s[i + j] >= 'A' && s[i + j] <= 'Z' && sub[j] >= 'a' && sub[j] <= 'z' && s[i + j] - 'A' == sub[j] - 'a')	continue;

			else break;

		}

		if(j == len_sub){

			for(j = 0 ; j < len_sub; ++j)	s[i + j] = ' ';

			i += j;

		}else ++i;

	}

	ns = (char*)calloc(len_s + 1, sizeof(char));

	for(i = j = 0; s[i] != '\0'; ++i){

		if(s[i] != ' ')	ns[j++] = s[i];

	}

	ns[j] = '\0';

	return ns;

}



int main(){

	char sub[30], s[1000], *ns;

	scanf("%s", sub);

	getchar();

	while(gets(s)){

		ns = remove_sub(s, sub);

		puts(ns);

		free(ns);

	}

	return 0;

}