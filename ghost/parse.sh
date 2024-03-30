#!/bin/sh

# Check if a file is provided as an argument
if [ $# -eq 0 ]; then
    echo "Usage: $0 <filename>"
    exit 1
fi

# Regex pattern used in signup process
pattern="^[a-z0-9\._]+$"

# checking
while IFS= read -r line; do
    if [[ $line =~ $pattern && ${#line} -lt 25 ]]; then
        echo "$line"
    fi
    echo "whee"
done < "$1"

exit 0