#include <stdio.h> //Standard input-output
#include <stdlib.h> //For random num
#include <time.h> //random seed

int main(){
    //Variable
    int RandNumber = 0;
    int UserGuess = 0;
    int Attempts = 0;
    const int MAXATTEMPTS = 5;

    srand(time(0));
    RandNumber = rand() % 100 + 1; // random 1 to 100
    //printf("Random number %d", RandNumber);
    printf("Welcome to random guessing game\n");
    printf("I have selected a number between 1 and 100.\n");
    printf("You have %d attempts to guess it \n", MAXATTEMPTS);

    //attems = maxAttemps
    while (Attempts < MAXATTEMPTS){ //attmps > 0
        printf("Enter your guess\n");
        scanf("%d, &UserGuess\n");//reads user input
        Attempts++; //increases counter

        if (UserGuess == RandNumber){
            printf("You got it right in %d attemps\n", Attempts);
            break;
        }
        else if(UserGuess > RandNumber){
            printf("You  guessed too high\n");
        }
        else if(UserGuess < RandNumber){
            printf("You gueesed too low\n");
        }
    }
    printf("You lost");

    return 0; //end of program
}
