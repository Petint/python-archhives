"""
Olvass be egész számokat, amíg 0 nem jön be.
Ha nem egész számot adnak meg, írd ki, hogy az nem egész szám,
ha viszont egész szám, akkor írd ki a felét.
A program legvégén minden esetben írd ki, hogy "Viszlát!"
"""
print('Egész számokat olvasunk be és kiírjuk mennyi a fele. Ha nem akarsz több számot megadni, írj be egy nullát!')
user_number = -1
while user_number != 0:
    user_number = int(input('Adj meg egy számot:'))
    if user_number > 0: print('A megadott szám fele:', user_number / 2)
print('Viszlát!')
