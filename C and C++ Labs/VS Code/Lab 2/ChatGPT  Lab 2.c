#include <stdio.h>
#include <string.h>
#include <ctype.h>

// Function to perform matching considering the pattern rules
int matchPattern(const char *text, const char *pattern, int caseSensitive)
{
    int textLen = strlen(text);
    int patternLen = strlen(pattern);

    for (int i = 0; i <= textLen - patternLen; i++)
    {
        int match = 1;

        for (int j = 0; j < patternLen; j++)
        {
            char textChar = text[i + j];
            char patternChar = pattern[j];

            // Handle case sensitivity
            if (!caseSensitive)
            {
                textChar = tolower(textChar);
                patternChar = tolower(patternChar);
            }

            // Match pattern rules
            if (patternChar == '.')
            {
                // '.' matches any character
                continue;
            }
            else if (patternChar == '_')
            {
                // '_' matches any whitespace
                if (!isspace(textChar))
                {
                    match = 0;
                    break;
                }
            }
            else
            {
                // Check for exact character match
                if (textChar != patternChar)
                {
                    match = 0;
                    break;
                }
            }
        }

        // If a match was found
        if (match)
        {
            return i;
        }
    }

    // No match found
    return -1;
}

int main()
{
    char text[256];
    char pattern[256];
    char caseSensitiveInput;
    int caseSensitive;

    // Get user input
    printf("Enter a line of text (up to 255 characters):\n");
    fgets(text, sizeof(text), stdin);

    printf("Enter a pattern (up to 255 characters):\n");
    fgets(pattern, sizeof(pattern), stdin);

    // Remove newline characters if they exist
    text[strcspn(text, "\n")] = 0;
    pattern[strcspn(pattern, "\n")] = 0;

    // Ask for case sensitivity
    printf("Should the match be case-sensitive? (Y/N):\n");
    scanf(" %c", &caseSensitiveInput);
    caseSensitive = (caseSensitiveInput == 'Y' || caseSensitiveInput == 'y');

    // Find the pattern in the text
    int matchIndex = matchPattern(text, pattern, caseSensitive);

    // Output results
    if (matchIndex != -1)
    {
        printf("Matches at position %d.\n", matchIndex);
    }
    else
    {
        printf("No match.\n");
    }

    return 0;
}
