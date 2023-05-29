import re
from calendar import month_name

def clean_journal_ref(journal):
    if type(journal) == str:
        # make lower
        journal = journal.lower()

        # Remove new line characters
        journal = journal.replace('\n', ' ')

        # replace a&a with astronomy.and.astrophysics
        journal = journal.replace('a&a', 'astronomy.and.astrophysics')

        # Split string on 'erratum' and remove second half
        journal = journal.split("erratum")[0]

        # make all strings start and end with a dot (.0)
        journal = '.' + journal + '.'

        # replace any spacial character or space with a .
        journal = re.sub('[\W_]', '.', journal)

        # Remove numbers
        journal = re.sub('\d+', '.', journal)

        words_to_replace = ['pp', 'no', 'volume', 'vol', 'issue', 'pages',]
        month_names = list(month_name[1:])
        month_names_short = [x[3:] for x in month_names]

        words_to_replace += month_names
        words_to_replace += month_names_short


        for mini_word in words_to_replace:
            journal = journal.replace('.'+mini_word+'.', '.')

        # replace common abbreviations
        for key, value in {'.j.': '.journal.of.', '.rev.': '.review.',
                           '.phys.': '.physics.', '.physical.': '.physics.'}.items():
            journal = journal.replace(key, value)

        if 'physics.review' in journal:
            journal = '.physics.review.'


        # Remove single letters
        journal = re.sub('[.][a-zA-Z](?:[.]|$)', '.', journal)

        # remove repeated dots
        journal = re.sub('\.{2,}', '.', journal)

        # strip dots at the start and end
        journal = journal.strip('.')

    return journal