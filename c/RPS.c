//header files/ libraries
#include <stdio.h> // standard input output
#include <stdlib.h> //random num
#include <time.h> //random seed
#include <windows.h>//sleep

int main(){

    //Variables
    char Player1;//character
    char Player2;
    
    int P1_Score = 0;
    int P2_Score = 0;

    int mode = 0;

    //random seed
    srand(time(0));
    

    while (1){//true 
        printf("Welcome to Rock, Paper, Scissors.\n");
        printf("Select Mode\n");
        printf("1.)Player vs Player\n2.)Player vs Computer \n3.)Quit\n");
        
        scanf("%d", &mode);//saves an int to mode variable address
        if (mode == 1){
            PvP();//Player vs Player
            Sleep(1000);//makes code wait //sleep(1000)
        }
        else if (mode == 2){
            PvAI();//Player vs Computer
            Sleep(1000);
        }
        else if (mode == 3){
            Sleep(1000);
            printf("Thanks for playing.\n");
            break;
        }
        else{
            printf("Invalid Choice. \nPlease pick 1,2 or 3 \n");
        }
    }
    return 0 ;


}

void PvP(){
    char P1Choice;
    char P2Choice;
    printf("Player 1 Please enter your choice.");
    printf("r: Rock, p: Paper, s: Scissors.");
    getchar();//Clears the newline character 
    scanf("%c", &P1Choice);//saves character into P1Choice
}


void PvAI(){
    char P1Choice;
    char CompChoice;
}


void runTime(){
    int num = 1;
    while (num > 10){
        printf('yoooooooooo\n');
        num++;
        Sleep(1000);
    }
    printf("done");

}
