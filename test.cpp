#include "unordered_map"
#include "iostream"
int main() {
    //Q1
    printf("Question 1.\n");
    while (1) {
        char q;
        printf("Please enter the Celcius degree: ");
        scanf(" %c", &q);


        if (q == 'q') {
            printf("Program is terminated.\n");
            break;
        }

        printf("decimal is: %d\n", q);

        int c = q - '0';

        printf("c is %d", c);

        int F = 9 / 5 * c + 32;
        printf("The themperature in Fahrenheit is %d\n", F);
    }
}