#include <stdio.h>

int main(){
    char operator;
    double num1;
    double num2;
    double result;

    printf("Welcome to Aayana's Calculator");
    printf("Enter an operaror (+,-,*,/): ");
    scanf("%c", &operator); //take the character and save to operator address
    printf("Enter two numbers: ");
    scanf("%lf %lf", &num1, &num2);

    //do the operator task
    //switch case similar to if else statement
    switch (operator)
    {
    case '+':
        result = num1 + num2;
        printf("Result: %.2lf\n", result);
        break;
    case '-':
        result = num1 - num2;
        printf("Result: %.2lf\n", result);
        break;
    case '/':
        if (num2 != 0){
            result = num1 / num2;
            printf("Result: %.2lf\n", result);
            break;
        }else{
            printf("Error: Divsion by zero is not allwed.\n");
        }
    case '*':
        result = num1 * num2;
        printf("Result: %.2lf\n", result);
        break;
        
        
    default:
        printf("Error: Invalid Operator\n");
    }


}