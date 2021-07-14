read -p "Commit description: " desc
make
word_count=$(ps2ascii thesis.pdf | wc -w)
page_count=$(pdftk thesis.pdf dump_data | grep NumberOfPages | cut -d' ' -f 2)
relative_wc=$(bc <<< "scale=2; ${word_count}/60000.")
echo "$(date),$word_count,$page_count,$desc" >> word_counts.csv
git add -u
git commit -m "$desc"
git push
echo "$(date)"
echo "$word_count"
echo "$page_count"
echo "$relative_wc"
python3 wc_plotter.py
