#!/bin/bash

# Set the directory for output and check if it exists. Create if no
main="$PWD" # The root directory of the project
dir="${PWD}/pylint_result" # The directory to house all pylinting reports
if [ ! -d "$dir" ]; then
    mkdir $dir
fi

# $1 = Name of file (ex: lab4)
# $2 = Directory (ex: ./temp)
pylinter(){
    python_file="$main/$1.py"
    pylint_report="$dir/$1_pylint.txt"
    echo "Adding pylint result for $python_file - $pylint_report"
    if [ ! -f "$pylint_report" ]; then
        touch $pylint_report
    fi
    pylint "$main$python_file" > $pylint_report
}

# Pylinting files
pylinter "lab4" ""
#pylinter "validation" "Validation/"

# Done doing stuff. Exit
echo "Done performing pylinting"