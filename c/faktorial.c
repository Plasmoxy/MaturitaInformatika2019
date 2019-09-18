#include <stdio.h>
#include <stdlib.h>
#include <errno.h>

const int NSTR = 100;

int faktorial(int n) {
    return 0;
}

int main() {
    char* endptr;
    char str[NSTR];

    printf("Zadajte cislo: ");
    fgets(str, NSTR, stdin);
    
    long cislo = strtol(str, &endptr, 10);
    printf("%c\n", *endptr);
    printf("c = %ld\n", cislo);
}
