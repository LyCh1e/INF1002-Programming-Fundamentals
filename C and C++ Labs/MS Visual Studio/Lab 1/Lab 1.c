#include <stdio.h>
#include <stdbool.h>

int main()
{
    int p1Number = 0;
    int roundsLeft = 10;
    int p2Number = 0;

    while (true)
    {
        printf("Player 1, enter a number between 1 and 1000:\n");
        scanf("%d", &p1Number);
        if (p1Number < 1 || p1Number > 1000)
        {
            printf("That number is out of range.\n");
        }
        else
        {
            break;
        }
    }

    while (roundsLeft > 0)
    {
        if (roundsLeft > 1)
        {
            printf("Player 2, you have %d guesses remaining.\nEnter your guess:\n", roundsLeft);
        }
        else if (roundsLeft == 1)
        {
            printf("Player 2, you have %d guess remaining.\nEnter your guess:\n", roundsLeft);
        }
        scanf("%d", &p2Number);

        if (p2Number < 1 || p2Number > 1000)
        {
            printf("That number is out of range.\n");
        }
        else
        {
            if (p2Number > p1Number)
            {
                printf("Too high.\n");
            }
            else if (p2Number < p1Number)
            {
                printf("Too low.\n");
            }
            else if (p2Number == p1Number)
            {
                printf("Player 2 wins.\n");
                return 0;
            }
            roundsLeft--;
        }
    }
    printf("Player 1 wins.\n");
    return 0;
}
