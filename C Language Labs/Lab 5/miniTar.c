/*******************************************************************************
Task Description:
    The tar program (for “tape archive”) creates an uncompressed binary file
    archive by joining a collection of files end to end. At the start of each
    file in the archive is a fixed-length header that stores information about
    the file, represented as a C structure as follows:

    struct header {
        char name[NAMSIZ];
        char mode[8];
        char uid[8];
        char gid[8];
        char size[12];
        char mtime[12];
        char chksum[8];
        char linkflag;
        char linkname[NAMSIZ];
        char magic[8];
        char uname[TUNMLEN];
        char gname[TGNMLEN];
        char devmajor[8];
        char devminor[8];
    };

    For the purposes of this exercise, we only need to worry about the name and
    size fields of the structure struct header.
    The name field contains the name of the file, while the size field contains
    the length of the file in bytes. Note that the size field is a string, not
    an integer, so it needs to be converted using atoi() to perform arithmetic
    on it. We can ignore (no need to comment out and no need to initialise) all
    the other fields in our program.

    A tar archive thus has the form:

    struct header | file1 data | struct header | file2 data | struct header | file3 data | ...

    The header sections always have the same length, sizeof(struct header), but
    the length of each file is given by the size field in the header.

    Write a program called minitar that accepts the two given file names
    (“File1.txt” and “File2.txt”) on the command line
                (minitar File1.txt File2.txt)
    and generate an archive file (“Result.tar”) containing all these files,
    with the name and size fields filled in as described above. For this task,
    the file open/write/read mode for Result.tar is “binary”.

    Note:
        1.	Make the program flexible to accept any number of input files:
            File1.txt, File2.txt, …
        2.	Use sys.argv[] for user inputs.
        3.	‘tar’ files are typically binary. Make sure that the file
            open and write mode for Result.tar is “binary”.
        4.	Best Practices for Writing File Size in Tar Headers
            •	‘tar’ format specification traditionally uses octal representation
                for numeric fields, including file sizes. This is a convention that
                dates to the early days of Unix and ensures compatibility with
                other tar implementations.
            •	Use Octal Representation: Using octal representation
                for the file size to maintain compatibility with the tar format.
                The snprintf function with the format "%011lo" ensures the size is
                zero-padded to 11 characters, which is the standard for tar headers.
                o	Ensure Correct Padding: The size field should be properly padded
                    with leading zeros to fit the 11-character width. This is crucial for
                    the tar format to be correctly interpreted by other tools.
                o	%: Indicates the start of a format specifier.
                o	0: Pads the output with leading zeros.
                o	11: Specifies the width of the output, ensuring it is 11 characters long.
                o	l: Indicates that the argument is of type long.
                o	o: Formats the number as an octal (base-8) number.
                o	Example:
                    >	For File1.txt, the file size in octal is 00000000037
                    >	For File2.txt, the file size in octal is 00000000076
            •	Handle Large Files: If you need to handle very large files (greater than 8 GB),
                consider using the GNU tar format or another extended format that supports
                larger sizes, as the traditional tar format has limitations. We will ignore
                this scenario for this task.
        5.	Add error handlers and comments where necessary.

    Hints:
        See http://www.cplusplus.com/reference/cstdio/fread/ for an example of
        how to find the length of a file and read it into memory. Note that
        reading the whole file into memory at once may require quite a lot of
        memory; you might like to try finding a more efficient method of copying
        data from the input file to the output file.
*******************************************************************************/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/*
 * Standard Archive Format - Standard TAR - USTAR
 * from https://www.fileformat.info/format/tar/corion.htm
*/

#define RECORDSIZE 512
#define NAMSIZ 100 // maximum length of a filename string
#define TUNMLEN 32 // maximum length of a username string in .tar
#define TGNMLEN 32 // maximum length of a group name string int .tar

struct header
{
    char name[NAMSIZ];
    char mode[8]; // ignore
    char uid[8];  // ignore
    char gid[8];  // ignore
    char size[12];
    char mtime[12];        // ignore
    char chksum[8];        // ignore
    char linkflag;         // ignore
    char linkname[NAMSIZ]; // ignore
    char magic[8];         // ignore
    char uname[TUNMLEN];   // ignore
    char gname[TGNMLEN];   // ignore
    char devmajor[8];      // ignore
    char devminor[8];      // ignore
};

void write_header(FILE *tarFile, const char *fileName, long fileSize)
{
    struct header hdr;

    // Zero out the header
    memset(&hdr, 0, sizeof(struct header));

    // Set filename
    strncpy(hdr.name, fileName, NAMSIZ - 1);

    // Set file size in octal format with proper padding
    snprintf(hdr.size, sizeof(hdr.size), "%011lo", fileSize);

    // Write header to .tar file
    fwrite(&hdr, sizeof(struct header), 1, tarFile);
}

void write_content(FILE *fileInput, FILE *tarFile, long fileSize)
{
    char buffer[RECORDSIZE];
    size_t readBytes;
    long totalWritten = 0;

    // Copy file content
    while ((readBytes = fread(buffer, 1, sizeof(buffer), fileInput)) > 0)
    {
        fwrite(buffer, 1, readBytes, tarFile);
        totalWritten += readBytes;
    }

    // Add padding if needed
    if (totalWritten < fileSize)
    {
        memset(buffer, 0, sizeof(buffer));
        fwrite(buffer, 1, fileSize - totalWritten, tarFile);
    }
}

int main(int argc, char *argv[])
{
    FILE *tarFile, *inputFile;
    long fileSize;

    // Check command line arguments
    if (argc < 2)
    {
        printf("Enter at least one file name (e.g File.txt).\n");
        return 1;
    }

    // Open tar file for binary writing
    tarFile = fopen("Result.tar", "wb");
    if (!tarFile)
    {
        printf("Error: Cannot create Result.tar\n");
        return 1;
    }

    // Process each input file
    for (int i = 1; i < argc; i++)
    {
        // Open file to enter input
        inputFile = fopen(argv[i], "rb");
        if (!inputFile)
        {
            printf("Error: Cannot open %s\n", argv[i]);
            continue;
        }

        // Get file the size
        fseek(inputFile, 0, SEEK_END);
        fileSize = ftell(inputFile);
        fseek(inputFile, 0, SEEK_SET);

        // Write header
        write_header(tarFile, argv[i], fileSize);

        // Write content int othe file
        write_content(inputFile, tarFile, fileSize);

        // Close file
        fclose(inputFile);
        printf("Added %s (size: %ld bytes)\n", argv[i], fileSize);
    }

    // Close .tar file
    fclose(tarFile);
    printf("Archive 'Result.tar' created successfully.\n");

    return 0;
}
