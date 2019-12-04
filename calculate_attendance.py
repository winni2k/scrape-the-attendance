def main(input_csv, dates_of_interest, output):
    import pandas as pd
    dat = pd.read_csv(input_csv)

    dates_of_interest = dates_of_interest.split()
    print(f'Dates kept: {" ".join(dates_of_interest)}')
    dates = dat.loc[:, dates_of_interest]
    dates = dates \
        .replace('-', 0) \
        .replace('J', 1) \
        .replace('N', 0) \
        .replace('JS', 0.8) \
        .replace('%', 0.5) \
        .replace('?', 0) \
        .replace('NO', 0)
    print(f'Number of rehearsals: {len(dates.columns)}')
    att_sums = pd.concat([dat.iloc[:, 0:2], dates.sum(axis=1)], axis=1)
    att_sums = att_sums.rename(columns={0: 'cumulative_attendance'})

    att_sums['proportion_attended'] = att_sums.cumulative_attendance / len(dates.columns)
    print(att_sums)
    att_sums.to_csv(output, index=False)


if __name__ == '__main__':
    import sys

    main(sys.argv[1], sys.argv[2], sys.argv[3])
