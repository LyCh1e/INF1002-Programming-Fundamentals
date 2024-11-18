/*******************************************************************************
Task Description:
    One way to sort a collection of items is called insertion sort. The idea is
    to start with an empty list, then insert items one at a time into it, placing
    them in their correct position in the order each time. Your task is to
    implement this algorithm using a linked list in a program insertionSort, so
    that the program can sort an arbitrary number of words entered by the user.

    Every node in the list should store one word, composed entirely of lower-case
    characters. The word may also contain apostrophes and hyphens, but not spaces,
    quotes, or any other characters that do not normally appear in the middle of
    English words. The word may be up to 32 characters long.

    The program should repeatedly ask the user to enter a word. The program should
    automatically convert upper-case letters into lower-case ones, but reject words
    containing characters other than letters, apostrophes, and hyphens.

    Each new word should be inserted into the list into its correct position in
    alphabetical order. For example, if the list currently contains the words
    "cat", "dog", and "monkey", and the user enters the word "elephant", the new
    word should be inserted between "dog" and "monkey". You can use strcmp() to
    determine whether a word comes before or after another in the alphabet (hyphens
    and apostrophes will be sorted according to their ASCII values).

    The program stops asking for words when the user enters the special text
    "***". The program should then print out the words, in order, one per line.

    Finally, the program should de-allocate all the memory that is has created and terminate.
    Note:
    1.	Use #define and comments as usual.
    2.	Check for memory allocation failures and report an error if they occur but
        continue to execute the program.
    3.	There is no white space in the print after the colons (:).
    4.	Don’t use sys.argv[] for user inputs. Use other functions such as
        scanf(), fgets(), fgetc(), etc.,

Some sample output is shown below, with the user input shown in red:
Example – 1:
    Please enter a word:
    cat
    Please enter a word:
    dog
    Please enter a word:
    monkey
    Please enter a word:
    elephant
    Please enter a word:
    ***
    All the entered words in order:
    cat
    dog
    elephant
    monkey

Example – 2:
    Please enter a word:
    hello
    Please enter a word:
    good-bye
    Please enter a word:
    it's
    Please enter a word:
    invalid word
    Invalid word.
    Please enter a word:
    valid
    Please enter a word:
    "quote"
    Invalid word.
    Please enter a word:
    another
    Please enter a word:
    ***
    All the entered words in order:
    another
    good-bye
    hello
    it's
    valid
*******************************************************************************/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <stdbool.h>

#define MAX_WORD_LENGTH 32
#define STOP_INPUT "***"

typedef struct Node
{
    char word[MAX_WORD_LENGTH + 1];
    struct Node *next;
} Node;

int validWord(const char *inputWord)
{
    if (strlen(inputWord) > MAX_WORD_LENGTH)
    {
        return false;
    }

    if (strlen(inputWord) == 0)
    {
        return false;
    }

    while (*inputWord)
    {
        if (isspace(*inputWord) || (!isalpha(*inputWord) && *inputWord != '-' && *inputWord != '\''))
        {
            return false;
        }
        inputWord++; // Increments the pointer to the next character
    }
    return true;
}

void lowerCase(char *inputWord)
{
    while (*inputWord)
    {
        *inputWord = tolower(*inputWord);
        inputWord++; // Increments the pointer to the next character
    }
}

Node *createNewNode(const char *inputWord)
{
    Node *newNode = (Node *)malloc(sizeof(Node));
    if (newNode == NULL)
    {
        return NULL;
    }

    strncpy(newNode->word, inputWord, MAX_WORD_LENGTH);
    newNode->word[MAX_WORD_LENGTH] = '\0'; // Remove "null" values from the array
    newNode->next = NULL;
    return newNode;
}

void printWords(Node *nodePtr)
{
    Node *currentPtr = nodePtr;
    while (currentPtr != NULL)
    {
        printf("%s\n", currentPtr->word);
        currentPtr = currentPtr->next;
    }
}

Node *insertInOrder(Node *nodePtr, Node *newNode)
{
    // If list is empty or the new node need ot eb the first
    if (nodePtr == NULL || strcmp(newNode->word, nodePtr->word) < 0)
    {
        newNode->next = nodePtr;
        return newNode;
    }

    // Look for the postion the node belongs to
    Node *currentPtr = nodePtr;
    while (currentPtr->next != NULL && strcmp(newNode->word, currentPtr->next->word) > 0)
    {
        currentPtr = currentPtr->next;
    }

    // Insert the node
    newNode->next = currentPtr->next;
    currentPtr->next = newNode;

    return nodePtr;
}

void freeNodeMemory(Node *nodePtr)
{
    Node *currentPtr = nodePtr;
    while (currentPtr != NULL)
    {
        Node *nextPtr = currentPtr->next;
        free(currentPtr);
        currentPtr = nextPtr;
    }
}

int main()
{
    Node *nodePointer = NULL;
    char inputWord[MAX_WORD_LENGTH + 1];

    while (true)
    {
        printf("Please enter a word:\n");

        // Check if input word is off correct format
        if (fgets(inputWord, MAX_WORD_LENGTH + 1, stdin) == NULL)
        {
            printf("Error reading input.\n");
            continue;
        }

        inputWord[strcspn(inputWord, "\n")] = false;

        // Check if user wants to stop
        if (strcmp(inputWord, STOP_INPUT) == false)
        {
            break;
        }

        lowerCase(inputWord);

        if (!validWord(inputWord))
        {
            printf("Invalid word.\n");
            continue;
        }

        Node *newNode = createNewNode(inputWord);
        if (newNode == NULL)
        {
            printf("Memory allocation failed.\n");
            continue;
        }

        nodePointer = insertInOrder(nodePointer, newNode);
    }

    printf("All the entered words in order:\n");
    printWords(nodePointer);

    freeNodeMemory(nodePointer);
    return 0;
}
