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

    // zadanie cisla with error checking
    long cislo = strtol(str, &endptr, 10);
    if ( *(endptr+1) != 0 ) {
        printf("Musite zadat cislo!\n");
        return -1;
    }

    printf("c = %ld\n", cislo);
}
