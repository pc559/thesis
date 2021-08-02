fname = 'thesis.bib'

with open(fname) as bib:
    lines = bib.readlines()
    lines = [line for line in lines if ('eprint' in line and not 'eprinttype' in line)]
    print(lines[:5])
    print('Number of eprints:', len(lines))
    lines = ["".join(filter(str.isdigit, line)) for line in lines]
    print(lines[:5])
    eprints = set(lines)
    print('Number of unique eprints:', len(eprints))

