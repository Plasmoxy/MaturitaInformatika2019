#include <stdio.h>
#include <stdlib.h>

int main() {
    char input[100];

    printf("Zadajte n: ");
    fgets(input, 100, stdin);
    int n = strtol(input, 0, 10);

    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= i; j++) {
            printf("%d ", j);
        }
        printf("\n");
    }
}