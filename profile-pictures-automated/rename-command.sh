#just run this
#exa | cat -n | while read n f; do mv -n "$f" "boys$n.jpeg"; done

# !/bin/sh

rename_files() {
    local dir="$1"
    local count=1
  
    # array of files to iterate over
    local files=("$dir"/*)

    for file in "${files[@]}"; do
        extension="${file##*.}"  # Get the file extension
        new_name="${dir}/boy${count}.${extension}" # new name
        mv "$file" "$new_name" #rename
        echo "Renamed: $file to $new_name" #tel rename
        ((count++))
    done
}

rename_files "/Users/radiohead/Downloads/slick/profile pictures/yes"

