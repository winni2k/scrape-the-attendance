# Scrape and analyze the SSSF attendance page

## Scraping the page

1. Navigate to the [SSSF presence page](https://studentsangarna.se/internt/presence/)
2. In the first pulldown box, select "Alla"
3. In the second box select the timeframe of interest (for example "2019 Hösten")
4. Right-click on the page and click "Save As..."
5. Save only the html to your favorite location (for exmample `data/2019-12-03_hoest-2019.htm`)
6. Run `parse.py` on the saved html file (first argument) and specify the output CSV (second argument)
```bash
python3 parse.py data/2019-12-03_hoest-2019.htm data/2019-12-03_hoest-2019.csv
```

