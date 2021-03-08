from unittest import mock
import unittest
import degiro_query


class TestFundsClass(unittest.TestCase):

    def setUp(self) -> None:
        self.test_client = degiro_query.Funds('', '')

    @mock.patch.object(degiro_query.degiroapi.DeGiro, 'login', autospec=True)
    def testLoginSuccessNoOTP(self, client_mock):
        """Test login succeeds."""
        expected = {}
        client_mock.return_value = expected
        self.assertTrue(self.test_client.login())

    @mock.patch.object(degiro_query.degiroapi.DeGiro, 'login', autospec=True)
    def testLoginFails(self, client_mock):
        """Test login fails with bad credentials."""
        client_mock.side_effect = Exception('Bad credentials')
        self.assertFalse(self.test_client.login())

    @mock.patch.object(degiro_query.degiroapi.DeGiro, 'getdata', autospec=True)
    def test_fetch_cash_assets(self, getdata_mock):
        """Test successfully fetching cash fund assets."""
        expected = [{'amount': '17.01', 'currency': 'EUR'}]
        getdata_mock.return_value = ['EUR 17.01']
        self.assertEqual(expected, self.test_client.fetch_cash_assets())



if __name__ == '__main__':
    unittest.main()