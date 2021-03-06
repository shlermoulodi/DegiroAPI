"""This app implements the unofficial Degiro API from https://github.com/lolokraus/DegiroAPI.
The user can run this on the terminal by passing arguments.
Once the application is fully developed, the available functionalities will be:
- log in
- log out
- show cash assets in default currency
- show the user portfolio
- plot a line graph, based on previous transactions, that show how the portfolio has developed over time.
"""
from deps import degiroapi


class Funds():
    def __init__(self, user: str, pwd: str, otp: str = None) -> None:
        """Constructor for Funds.

        Arguments:
            user: username for DeGiro login.
            pwd: password for DeGiro login.
            otp: a OTP code from Google Authenticator app.
        """
        self.client = degiroapi.DeGiro()
        self.username = user
        self.password = pwd
        self.otp = otp

    def login(self) -> bool:
        """Function to login to DeGiro API.

        Returns:
            If login was successful (True) or not (False).
        """
        try:
            if self.otp:
                _ = self.client.login(self.username, self.password, self.otp)
            else:
                _ = self.client.login(self.username, self.password)
            return True
        # TODO(me): Should add more specific exception for login failed in degiroapi.DeGiro.login.
        except Exception:
            return False

    def fetch_cash_assets(self):
        """Function to show the user's cash assets.

        Returns:
             The available cash funds in the user account in the format 'CURRENCY: Value', e.g. EURO 5.5.
        """
        return [
            {"amount": balance.split()[1], "currency": balance.split()[0]}
            for balance in self.client.getdata(degiroapi.Data.Type.CASHFUNDS)
        ]