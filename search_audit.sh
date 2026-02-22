#!/bin/bash
echo "Enter the name, wallet, or keyword you are looking for:"
read keyword
echo "Searching in /sdcard/Download/ for: $keyword..."

# This searches all text and html files for your keyword
grep -ri "$keyword" /sdcard/Download/ | tee search_results.txt

echo "-----------------------------------------------"
echo "Search complete. Results saved to search_results.txt"
