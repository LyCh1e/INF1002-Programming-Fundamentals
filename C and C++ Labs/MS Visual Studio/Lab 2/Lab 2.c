#include <stdio.h>
#include <stdbool.h>
#include <ctype.h>
#include <string.h>

int findPattern(const char* inputPattern, const char* inputText, int caseSensitiveValue)
{
    int textLength = strlen(inputText);
    int patternLength = strlen(inputPattern);

    // Loop through the text array to notate each value in the text array
    for (int textIndex = 0; textIndex <= (textLength - patternLength); textIndex++)
    {
        int matchCase = true;

        // Loop through the pattern array to notate each value in the pattern array
        for (int patternIndex = 0; patternIndex < patternLength; patternIndex++)
        {
            char textletter = inputText[textIndex + patternIndex];
            char patternLetter = inputPattern[patternIndex];

            if (!caseSensitiveValue) // Check if case sensitivity is to be applied or not
            {
                textletter = tolower(textletter);
                patternLetter = tolower(patternLetter);
            }

            if (patternLetter == '.') // If the pattern letter is a dot or an underscore
            {
                continue;
            }
            else if (patternLetter == '_') // Else if the letter is a blank space
            {
                if (!isspace(textletter))
                {
                    matchCase = false;
                    break;
                }
            }
            else
            {
                if (textletter != patternLetter)
                {
                    matchCase = false;
                    break;
                }
            }
        }

        if (matchCase)
        {
            return textIndex; // Return the position where the match was found in the array
        }
    }
    return -1; // No match found in the text array
}

int main()
{
    char inputText[256];
    char inputPattern[256];
    char caseSensitiveInput;
    int caseSensitiveValue;
    int matchedPattern = 0;

    // Ask for strings to match
    printf("Enter a line of text (up to 255 characters):\n");
    fgets(inputText, sizeof(inputText), stdin);

    // Ask for pattern
    printf("Enter a pattern (up to 255 characters):\n");
    fgets(inputPattern, sizeof(inputPattern), stdin);

    // Ask for case sesitivity
    printf("Should the match be case-sensitive? (Y/N):\n");
    scanf_s("%c", &caseSensitiveInput);

    // Remove newline characters ("\n") if they exist
    inputText[strcspn(inputText, "\n")] = 0;
    inputPattern[strcspn(inputPattern, "\n")] = 0;

    // caseSensitiveValue = 1 (true) if 'Y' and caseSensitiveValue = 0 (false) if 'N'
    caseSensitiveValue = toupper(caseSensitiveInput);

    matchedPattern = findPattern(inputPattern, inputText, caseSensitiveValue);

    if (matchedPattern != -1)
    {
        printf("Matches at position %d.\n", matchedPattern);
    }
    else
    {
        printf("No match.\n");
    }

    return 0;
}
