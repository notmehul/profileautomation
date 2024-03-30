import re

def remove_hashtags_and_links(input_file, output_file):
    # Regular expression patterns to match hashtags and links
    hashtag_pattern = r'\b#\w+\b'
    link_pattern = r'https?://\S+'

    # Compile the patterns
    hashtag_regex = re.compile(hashtag_pattern)
    link_regex = re.compile(link_pattern)

    # Open input file for reading and output file for writing
    with open(input_file, 'r') as fin, open(output_file, 'w') as fout:
        for line in fin:
            # Initialize an empty string for the modified line
            modified_line = ''
            # Initialize a flag to check if we are in a URL
            in_url = False
            for char in line:
                # If the character is the start of a URL, set the flag
                if char == 'h':
                    in_url = True
                # If we are in a URL, continue until we find a space
                if in_url and char == ' ':
                    in_url = False
                    continue
                # If we are not in a URL, append the character
                if not in_url:
                    modified_line += char

            # Remove hashtags
            modified_line = re.sub(hashtag_regex, '', modified_line)
            # Remove links
            modified_line = re.sub(link_regex, '', modified_line)
            # Write the modified line to the output file
            fout.write(modified_line)

if __name__ == "__main__":
    input_file = "bioscopy.txt"
    output_file = "output.txt"
    remove_hashtags_and_links(input_file, output_file)
