import mechanize


browser = mechanize.Browser()
browser.set_handle_robots(False)
url = "https://www.pythonanywhere.com/login/"

browser.set_handle_equiv(True)
browser.set_handle_gzip(True)
browser.set_handle_redirect(True)
browser.set_handle_referer(True)

browser.open(url)
for form in browser.forms():
    print(form)

browser.select_form(nr=0)
browser.form['auth-username'] = ''
browser.form['auth-password'] = ''
browser.submit()
