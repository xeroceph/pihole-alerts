"""
xeroceph - https://github.com/xeroceph/pihole-alerts
GNU General Public License GPL v3.0 - https://www.gnu.org/licenses/gpl-3.0.en.html
"""

from config import *
import smtplib
import email

def sendMail(i):
    try:
        # set up vars
        payload = 'Hit reported for blacklist item ' + i + ' within the last 24 hours'
        msg = email.message_from_string(payload)
        msg['From'] = emailAddr
        msg['To'] = emailAddr
        msg['Subject'] = "Pihole-alerts notification"
        text = msg.as_string()

        # instantiate the session
        s = smtplib.SMTP(mailserver, mailserverPort)
        s.ehlo()
        s.starttls()
        s.ehlo()
        s.login(emailAddr, password)
    
        # send the notification
        s.sendmail(emailAddr, emailAddr, text)
        s.quit()
    except:
        pass
