def modify_urls_in_file(input_filepath):
    """
    Reads URLs from a text file, adds '||' to the start and '^' to the end
    of each URL, and prints the modified URLs.

    Args:
        input_filepath (str): The path to the input text file containing URLs.
    """
    try:
        with open(input_filepath, 'r') as file:
            for line in file:
                # Remove leading/trailing whitespace, especially newlines
                url = line.strip()
                if url:  # Ensure the line is not empty
                    modified_url = f"||{url}^"
                    print(modified_url)
    except FileNotFoundError:
        print(f"Error: The file '{input_filepath}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# --- Example Usage ---
if __name__ == "__main__":

    print("Processing URLs from 'urls.txt':\n")
    modify_urls_in_file("url-list.txt")
    print("\nProcessing complete.")

