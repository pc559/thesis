word_count=$(ps2ascii thesis.pdf | wc -w)
page_count=$(pdftk thesis.pdf dump_data | grep NumberOfPages | cut -d' ' -f 2)
echo "$(date)"
echo "$word_count"
echo "$page_count"
relative_wc=$(bc <<< "scale=2; ${word_count}/60000.")
echo "$relative_wc"
echo "$(date),$word_count,$page_count" >> word_counts.csv
git add -u
read -p "Commit description: " desc
git commit -m "$desc"
git push
python3 wc_plotter.py
