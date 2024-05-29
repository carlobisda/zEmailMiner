#NAME:      zzEmailMiner
#Version:   1.0
#License:   MIT
#Author:    Carlo Bisda

import re

# Open the input file for reading
with open('input.txt', 'r') as input_file:
    # Read the contents of the input file into a string
    input_text = input_file.read()

# Use a regular expression to extract all email addresses from the input text
email_addresses = re.findall(r'<(.*?)>', input_text)

# Open the output file for writing
with open('output.txt', 'w') as output_file:
    # Write the extracted email addresses to the output file, converting them to lowercase
    for email_address in email_addresses:
        output_file.write(email_address.lower() + '\n')
