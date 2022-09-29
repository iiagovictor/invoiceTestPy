import unittest
from TestExercise.Invoice import Invoice

class TestInvoice(unittest.TestCase):

    def test_invoice_values(self):
       with self.assertRaises(Exception):
           Invoice(None, None, None, 5)

    def test_getInvoiceAmount(self):
        fatura = Invoice(1, 'Teste 1', 4, 2.50)
        self.assertEqual(fatura.getInvoiceAmount(), 10)
    
    def teste_price(self):
       with self.assertRaises(Exception):
           Invoice(1, 'Teste 2', -5, 5)

if __name__ == '__name__':
    unittest.main()