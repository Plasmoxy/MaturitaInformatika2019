#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <math.h>

int pocetCifier(int x) {
    return (int)( floor(log10(x)) ) + 1;
}

int main() {
    char input[50];
    printf("Zadajte n: ");
    fgets(input, 100, stdin);
    int n = strtol(input, NULL, 10);

    /*
    real    0m0.319s
    user    0m0.172s
    sys     0m0.047s
    */
    // int n = 1000;
    

    int dlzka = pocetCifier(n) + 2;

    for (int x = 1; x <= n; x++) {
        for (int y = 1; y <= n; y++) {
            printf("%*d", dlzka, x*y);
        }
        printf("\n");
    }
}