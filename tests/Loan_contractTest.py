import unittest

from LoanContract import LoanContract


class MyTestCase(unittest.TestCase):
    def test_compute_monthly_payment(self):
        loan_contract = LoanContract()
        self.assertEqual(8606.64297070823, loan_contract.commute_monthly_payment())
    #end

    def test_compute_total_payment(self):
        loan_contract = LoanContract()
        self.assertEqual(103279.71564849876, loan_contract.compute_total_payment())


if __name__ == '__main__':
    unittest.main()
