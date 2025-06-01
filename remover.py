def modify_urls_in_place(filepath):
    """
    Reads URLs from a text file, adds '||' to the start and '^' to the end
    of each URL, and overwrites the original file with the modified URLs.

    Args:
        filepath (str): The path to the text file containing URLs.
    """
    modified_lines = []
    try:
        with open(filepath, 'r') as infile:
            for line in infile:
                # Remove leading/trailing whitespace, especially newlines
                url = line.strip()
                if url:  # Ensure the line is not empty
                    modified_lines.append(f"||{url}^")
        
        # Write the modified lines back to the same file, overwriting its content
        with open(filepath, 'w') as outfile:
            for modified_url in modified_lines:
                outfile.write(f"{modified_url}\n") # Add a newline character for each URL

        print(f"Successfully modified URLs in '{filepath}' in place.")
    except FileNotFoundError:
        print(f"Error: The file '{filepath}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# --- Example Usage ---
if __name__ == "__main__":
    # Create a dummy input file for demonstration purposes
    # In a real scenario, you would already have your 'urls.txt'
    file_name = "url-list.txt"


    print(f"Processing URLs in '{file_name}' and modifying the file in place...\n")
    modify_urls_in_place(file_name)
    print("\nProcessing complete.")
