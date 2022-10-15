import io
from unittest import mock, TestCase

from calculator import tip_calculator

class TestTipCalculator(TestCase):

    @mock.patch('builtins.input', side_effect=['15', '1', 'yes', '20', 'no', 'no'])
    @mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_tip_calculator01(self, mock_stdout, mock_input):
        tip_calculator()

        self.assertEqual("Total bill: $19.5\n", mock_stdout.getvalue())

    @mock.patch('builtins.input', side_effect=['25000000', '3', 'yes', '31', 'no', 'no'])
    @mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_tip_calculator02(self, mock_stdout, mock_input):
        tip_calculator()

        self.assertEqual("Total bill: $35250000.0\nEach person should pay $11750000.0\n", mock_stdout.getvalue())

    @mock.patch('builtins.input', side_effect=['78.99', '6', 'no', 'no'])
    @mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_tip_calculator03(self, mock_stdout, mock_input):
        tip_calculator()

        self.assertEqual("Total bill: $86.89\nEach person should pay $14.48\n", mock_stdout.getvalue())

    @mock.patch('builtins.input', side_effect=['5000', '876', 'yes', '12', 'no', 'no'])
    @mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_tip_calculator04(self, mock_stdout, mock_input):
        tip_calculator()

        self.assertEqual("Total bill: $6100.0\nEach person should pay $6.96\n", mock_stdout.getvalue())