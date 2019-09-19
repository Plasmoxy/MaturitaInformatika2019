/*
program, ktory pre zadane n vytvori obrazok z hviezdiciek
-> piramida
*
**
***
****
...
*/

#include <stdio.h>
#include <stdlib.h>

int main() {
    char* endp;
    char str[100];

    printf("zadajte pocet riadkov: ");

    fgets(str, 100, stdin);
    int n = strtol(str, &endp, 10);
    if (*(endp+1) != 0) {
        printf("Zadajte cislo!\n");
        return -1;
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j <= i; j++) {
            printf("*");
        }
        printf("\n");
    }
}