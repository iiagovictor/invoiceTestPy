import unittest
from TestExercise.Invoice import Invoice

class TestInvoice(unittest.TestCase):

    def test_getInvoiceAmount(self):
        fatura = Invoice(1, 'Produto 1', 4, 2.50)
        self.assertEqual(fatura.getInvoiceAmount(), 10)

    def test_invoice_item(self):
       with self.assertRaises(Exception):
           Invoice(None, 'Produto 2', 6, 5)

    def test_invoice_descricao(self):
        with self.assertRaises(Exception):
            Invoice(1, None, 6, 5)

    def test_invoice_qtd(self):
        with self.assertRaises(Exception):
            Invoice(1, 'Produto 5', None, 5)
    
    def teste_price(self):
       with self.assertRaises(Exception):
           Invoice(1, 'Produto 4', -5, 5)

if __name__ == '__name__':
    unittest.main()