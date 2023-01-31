#!/bin/bash

# Set the directory for output and check if it exists. Create if no
main="$PWD"
dir="${PWD}/pylint_result"
if [ ! -d "$dir" ]; then
    mkdir $dir
fi

# $1 = Name of file (ex: lab4)
# $2 = Directory (ex: ./temp)
pylinter(){
    python_file="$2$1.py"
    pylint_report="$dir/$1_pylint.txt"
    echo "Adding pylint result for $python_file - $pylint_report"
    if [ ! -f "$pylint_report" ]; then
        touch $pylint_report
    fi
    pylint $python_file > $pylint_report
}

# Pylinting files
pylinter "lab4" ""
pylinter "validation" "${main}/validation/"

# Done doing stuff. Exit
echo "Done performing pylinting"