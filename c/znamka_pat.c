#include <stdio.h>
#include <stdlib.h>

#define MIN_USPESNOST 0.33f

int main() {
    char input[50];
    
    printf("Zadajte maximalny pocet bodov: ");
    fgets(input, 50, stdin);
    int maxBodov = strtol(input, NULL, 10);

    printf("Zadajte pocet bodov: ");
    fgets(input, 50, stdin);
    int body = strtol(input, 0, 10);

    float uspesnost = (float)(body) / (float)(maxBodov);
    printf("Uspesnost: %.2f%%\n", uspesnost*100);

    if (uspesnost > MIN_USPESNOST) {
        printf("Presiel si.\n");
    } else {
        printf("Bohuzial si nepresiel.\n");
    }
}