./spellcheck_all.sh
read -p "Commit description: " desc
make
word_count=$(ps2ascii thesis.pdf | wc -w)
page_count=$(pdftk thesis.pdf dump_data | grep NumberOfPages | cut -d' ' -f 2)
relative_wc=$(bc <<< "scale=2; ${word_count}/60000.")
next_percent=$(bc <<< "${relative_wc}*60000+600")
echo "$(date),$word_count,$page_count,$desc" >> word_counts.csv
git add -u
git commit -m "$desc"
git push
echo "$(date)"
echo "$word_count"
echo "$page_count"
echo "$relative_wc"
echo "Only $(bc <<< ${next_percent}-${word_count}) words until the next percent."
python3 wc_plotter.py
echo ""
echo "IMPT FIONA MSG"
python3 read_fionas_wholesomeness.py test.txt
