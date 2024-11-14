'''7) Write a python program to read any text file and find the number of words, lines and characters in it.
Write the number of words, lines and characters in output file with name output.txt.'''
# Function to count lines, words, and characters


def count_text_file(input_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()  # Read all lines from the input file

    # Initialize counters
    line_count = len(lines)
    word_count = 0
    char_count = 0

    # Process each line
    for line in lines:
        words = line.split()  # Split line into words
        word_count += len(words)
        char_count += len(line)  # Include whitespace characters in the character count

    return line_count, word_count, char_count

# Write the results to an output file
def write_output(output_file, line_count, word_count, char_count):
    with open(output_file, 'w') as file:
        file.write(f"Lines: {line_count}\n")
        file.write(f"Words: {word_count}\n")
        file.write(f"Characters: {char_count}\n")

# Main function
def main():
    input_file = 'input.txt'  # Name of the input file
    output_file = 'output.txt'  # Name of the output file

    # Count lines, words, and characters in the input file
    line_count, word_count, char_count = count_text_file(input_file)

    # Write results to the output file
    write_output(output_file, line_count, word_count, char_count)

    print("Counting completed! Check the output.txt file for results.")

# Run the main function
if __name__ == "__main__":
    main()
