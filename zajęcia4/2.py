import smtplib
import email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

with open('tresc_mail.txt', 'r') as file:
    tresc = file.read()

mail_nadawca = input("Podaj adres e-mail nadawcy: ")
haslo = input("Podaj hasło: ")
mail_odbiorca = input("Podaj adres e-mail odbiorcy: ")
tytul = input("Podaj tytuł wiadomości: ")

wiadomosc = MIMEMultipart()
wiadomosc["From"] = mail_nadawca
wiadomosc["To"] = mail_odbiorca
wiadomosc["Subject"] = tytul

wiadomosc.attach(MIMEText(tresc, "plain"))

try:
    serwer_smtp = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    serwer_smtp.login(mail_nadawca, haslo)
    serwer_smtp.sendmail(mail_nadawca, mail_odbiorca, wiadomosc.as_string())
    serwer_smtp.quit()
    print("Wiadomość została wysłana pomyślnie.")
except Exception as e:
    print(f"Wystąpił błąd podczas wysyłania wiadomości: {e}")
