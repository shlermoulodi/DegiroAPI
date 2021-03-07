from unittest import mock
import unittest
import degiro_query


class TestFundsClass(unittest.TestCase):

    @mock.patch.object(degiro_query.degiroapi.DeGiro, 'login', autospec=True)
    def testLoginSuccessNoOTP(self, client_mock):
        """Test login succeeds."""
        expected = {}
        client_mock.return_value = expected
        client = degiro_query.Funds('', '', 3)
        self.assertTrue(client.login())

    @mock.patch.object(degiro_query.degiroapi.DeGiro, 'login', autospec=True)
    def testLoginFails(self, client_mock):
        """Test login fails with bad credentials."""
        client_mock.side_effect = Exception('Bad credentials')
        client = degiro_query.Funds('', '')
        self.assertFalse(client.login())


if __name__ == '__main__':
    unittest.main()
