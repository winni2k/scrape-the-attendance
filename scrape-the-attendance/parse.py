import pandas as pd
from bs4 import BeautifulSoup


def main(input, output):
    print(f'Reading {input}')
    print(f'Writing CSV to {output}')

    with open(input) as fh:
        soup = BeautifulSoup(fh.read(), "html.parser")
    table = soup.find_all(id='tablesorterSSSF')[0]
    header = []
    for col in table.thead.tr:
        header.append(col.text)
    header[1] = 'section'
    rows = []
    for row in table.tbody.find_all('tr'):
        fields = [t.text for t in row.find_all('td', class_='sangare')]
        for field in row.find_all('td', class_='stat'):
            fields.append(next(o.text for o in field.find_all('option') if o.has_attr('selected')))
        rows.append(fields)

    # drop summering row
    df = pd.DataFrame.from_records(rows[:-1], columns=header)
    df.to_csv(output, index=False)


if __name__ == '__main__':
    import sys

    main(sys.argv[1], sys.argv[2])
