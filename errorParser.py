import os
import re


# Define a function to find errors in a .tzlog file and write them to an output file
def find_errors_in_tzlog(file_path, output_file):
    error_pattern = r'error[:]?'
    # Define a pattern to skip lines containing specific messages
    skip_pattern = r'(No (Model|Make) found in metadata|\[AIE\] WARN  Using an engine plan file across different models of devices is not recommended and is likely to affect performance or even cause errors)'
    
    # Open the .tzlog file for reading
    with open(file_path, 'r') as file:
        for line_number, line in enumerate(file, start=1):
            # Check if the line contains 'error' (case-insensitive) and does not match the skip_pattern
            if re.search(error_pattern, line, re.IGNORECASE) and not re.search(skip_pattern, line):
                filename = os.path.basename(file_path)  # Get the filename without the path
                error_message = line.strip()  # Remove leading/trailing whitespace from the line
                # Write the error message along with the filename and line number to the output file
                output_file.write(f"{filename} (line {line_number}): {error_message}\n")

# Define a function to process all .tzlog files in a folder
def process_tzlog_folder(input_folder):
    # Create an 'output_folder' named 'notes' in the same directory as the 'input_folder'
    output_folder = os.path.join(input_folder, 'notes')
    # Create the 'output_folder' if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Open 'tzNotes.txt' in the 'output_folder' for writing
    with open(os.path.join(output_folder, 'tzNotes.txt'), 'w') as output_file:
        # Recursively traverse all files in 'input_folder'
        for root, _, files in os.walk(input_folder):
            for file_name in files:
                # Process files with the '.tzlog' extension
                if file_name.endswith('.tzlog'):
                    file_path = os.path.join(root, file_name)
                    # Call 'find_errors_in_tzlog' to search for errors in the file and write them to the output file
                    find_errors_in_tzlog(file_path, output_file)

if __name__ == "__main__":
    # Prompt the user to input the folder path they want to process
    input_folder = input("enter targeted folder path: ")
    # Call 'process_tzlog_folder' to begin processing .tzlog files in the specified folder
    process_tzlog_folder(input_folder)

