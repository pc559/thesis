word_count=$(ps2ascii thesis.pdf | wc -w)
echo "$(date)"
echo "$word_count"
relative_wc=$(bc <<< "scale=2; ${word_count}/60000.")
echo "$relative_wc"
echo "$(date),$word_count" >> word_counts.csv
