/*******************************************************************************
Task Description:
    Unix systems provide a utility known as grep that searches the lines of a
    file for a given pattern of characters. (The pattern is known as a regular
    expression and the name grep comes from “global regular expression print”).
    We won’t learn how to use files until Week 12, so we’ll just search a string
    entered at the keyboard. We’ll also support only very simple patterns.

    Write a program, called tinyGrep.c, that performs as follows:
    1.	The program asks the user to enter a line of text of up to 255 characters.
    2.	The program asks the user to enter a pattern (a string), also of up to
        255 characters.
    3.	The program asks the user whether the match should be case-sensitive or
        case-insensitive.
    4.	The program outputs whether the pattern occurs anywhere in the line of
        text, and, if it does, the index of the string at which the first instance
        of the pattern occurs.

    The rules for patterns are as follows:
    •	Any English letter matches itself. If the match is case-sensitive,
        lower-case letters match only lower-case letters, and upper-case letters
        match only upper-case letters. If the match is case-insensitive,
        lower-case letters match upper-case letters, and vice versa.
    •	A dot (.) matches any character.
    •	An underscore (_) matches any form of whitespace (i.e. any character for
        which isspace() returns a true value).
    •	All other characters match only themselves.

    The following table shows some examples.
        --------------------------------------------------------------------------------
        | Text                    | Pattern | Case-sensitive | Output                  |
        --------------------------------------------------------------------------------
        | The cat sat on the mat. | cat     | N              | Matches at position 4.  |
        | The cat sat on the mat. | rat     | N              | No match.               |
        | The cat sat on the mat. | at      | N              | Matches at position 5.  |
        | The cat sat on the mat. | .at     | N              | Matches at position 4.  |
        | The cat sat on the mat. | the     | N              | Matches at position 0.  |
        | The cat sat on the mat. | the     | Y              | Matches at position 15. |
        | The cat sat on the mat. | ...     | Y              | Matches at position 0.  |
        | "Hello," said the cat.  | ,       | N              | Matches at position 6.  |
        --------------------------------------------------------------------------------

    You might like to proceed as follows:
        1.	Write a main program that reads the strings and case-sensitivity
            information as described above.
        2.	Don’t use sys.argv[] for user inputs. Use other functions such
            as scanf(), fgets(), fgetc(), etc.,
        3.	Ignoring the pattern-matching rules for now, write a loop that simply
            searches the input text for an occurrence of the pattern string using
            strncmp() or similar function.
        4.	Replace strncmp() with a new function that matches case-sensitively
            or case-insensitively depending on the user’s answer to this question.
        5.	There is no white space in the print after the colons (:).
        6.	Modify your new function to handle dot and underscore characters
            according to the rules above.

Sample Program inputs and outputs:
Example - 1:
    Enter a line of text (up to 255 characters):
    The cat sat on the mat.
    Enter a pattern (up to 255 characters):
    cat
    Should the match be case-sensitive? (Y/N):
    N
    Matches at position 4.

Example - 2:
    Enter a line of text (up to 255 characters):
    The cat sat on the mat.
    Enter a pattern (up to 255 characters):
    rat
    Should the match be case-sensitive? (Y/N):
    N
    No match.
 *******************************************************************************/
#include <stdio.h>
#include <stdbool.h>
#include <ctype.h>
#include <string.h>

int findPattern(const char *inputPattern, const char *inputText, char caseSensitiveValue)
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

            if (caseSensitiveValue == 'N') // Check if case sensitivity is to be applied or not
            {
                textletter = tolower(textletter);
                patternLetter = tolower(patternLetter);
            }

            if (patternLetter == '.') // If the pattern letter is a dot or an underscore
            {
                continue;
            }
            else if (patternLetter == '_' || patternLetter == ' ') // Else if the letter is a blank space
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
    return 1; // No match found in the text array
}

int main()
{
    char inputText[256];
    char inputPattern[256];
    char caseSensitiveInput;
    char caseSensitiveValue;
    int matchedPattern = 0;

    // Ask for strings to match
    printf("Enter a line of text (up to 255 characters):\n");
    fgets(inputText, sizeof(inputText), stdin);

    // Ask for pattern
    printf("Enter a pattern (up to 255 characters):\n");
    fgets(inputPattern, sizeof(inputPattern), stdin);

    // Ask for case sesitivity
    printf("Should the match be case-sensitive? (Y/N):\n");
    scanf("%c", &caseSensitiveInput);

    // Remove newline characters ("\n") if they exist
    inputText[strcspn(inputText, "\n")] = 0;
    inputPattern[strcspn(inputPattern, "\n")] = 0;

    // Set caseSensitiveValue = 'Y' or  caseSensitiveValue = 'N' from their lower case
    caseSensitiveValue = toupper(caseSensitiveInput);

    matchedPattern = findPattern(inputPattern, inputText, caseSensitiveValue);

    if (matchedPattern != 1)
    {
        printf("Matches at position %d.\n", matchedPattern);
    }
    else
    {
        printf("No match.\n");
    }

    return 0;
}
