#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>

int main() {
    char* SPOLUHLASKY = "bcdfghjklmnprstvwxz";
    char* SAMOHLASKY = "aeiou";
    size_t SAM_SIZE = sizeof(SAMOHLASKY);
    size_t SPO_SIZE = sizeof(SPOLUHLASKY);

    int n = 5;
    char slovo[n*2];
    memset(slovo, '*', n*2);

    srand(time(NULL));

    for (int i = 0; i <= n*2; i += 2) {
        slovo[i] = SPOLUHLASKY[rand() % (SPO_SIZE-1)];
        slovo[i+1] = SAMOHLASKY[rand() % (SAM_SIZE-1)];
    }

    printf("%s\n", slovo);
}