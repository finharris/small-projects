'''
Password reset program 
Only accept a new password if it is:
1. At least eight characters long
2. Has lower case and upper case letters.
The password reset program should also make the user input their new password twice so that the computer knows that the user has not made any mistakes when typing their new password.
Extensions: 
1. Make some sort of algorithm to suggest how strong the password is (Weak, Medium, Strong) depending on length, whether or not the password has special characters in etc
2. Let the user input their username. The program should go to a text file with a list of usernames and old passwords, and the program should only let you change your password if 
you input your old password.

(((len(psw)-10) * -1) - 2) * -1
'''


class ResetPassword:
    def resetPassword():
        def definePasswordStrength(psw):
            import re

            def clamp(n, minn, maxn):
                return max(min(maxn, n), minn)

            score = 0

            lengthScore = (((len(psw)-10) * -1) - 2) * -1
            characterScore = len(re.findall(
                '\d', psw)) + (len(re.findall('[!"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~]', psw))*2)

            score = clamp(((100/36) * (lengthScore + characterScore)), 0, 100)

            if score < 15:
                return 'Very Weak'
            elif score < 25:
                return 'Weak'
            elif score < 50:
                return 'Medium'
            elif score < 75:
                return 'High'
            elif score < 90:
                return 'Very High'
            elif score < 100:
                return 'Extremely High'
            else:
                raise SyntaxError

        def validatePassword(psw):
            def lowerAndUpper(string):
                if string != string.lower() and string != string.upper():
                    return True

            if len(psw) >= 8 and len(psw) <= 16 and lowerAndUpper(psw):
                return True
            else:
                return False

        # TODO
        passwordAccepted = False
        while not passwordAccepted:
            inputtedPasswordFirst = input('Please enter password.')
            inputtedPasswordSecond = input('Please enter password again.')

            if inputtedPasswordFirst == inputtedPasswordSecond:
                newPassword = inputtedPasswordFirst

                if validatePassword(newPassword):
                    print('Passwords match and are valid.')
                    print(
                        f'Estimated password strength {definePasswordStrength(newPassword)}')
                    passwordAccepted = True
                else:
                    print(
                        'Passwords match but are not valid. Must be longer than 8 characters and contain upper an lower case.')
                    print('Please try again.\n')
            else:
                print('Passwords do not match.')
                print('Please try again.\n')

        return
