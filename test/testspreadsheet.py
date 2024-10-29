from unittest import TestCase
from spreadsheet import SpreadSheet


class TestSpreadSheet(TestCase):

    def test_evaluate_valid_integer(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1", "1")
        self.assertEqual(1, spreadsheet.evaluate("A1"))

    def test_evaluate_non_valid_integer(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1", "1.5")
        self.assertEqual("#Error", spreadsheet.evaluate("A1"))

    def test_evaluate_valid_string(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1", "'Apple'")
        self.assertEqual("Apple", spreadsheet.evaluate("A1"))

    def test_evaluate_non_valid_string(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1", "'Apple")
        self.assertEqual("#Error", spreadsheet.evaluate("A1"))

    def test_formula_evaluate_valid_string(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1", "='Apple'")
        self.assertEqual("Apple", spreadsheet.evaluate("A1"))

    def test_formula_evaluate_valid_integer(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1", "=5")
        self.assertEqual(5, spreadsheet.evaluate("A1"))

    def test_formula_evaluate_invalid_string(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1", "='Apple")
        self.assertEqual("#Error", spreadsheet.evaluate("A1"))

    def test_simple_formulas_with_references(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1", "=B2")
        spreadsheet.set("B2", "42")
        self.assertEqual(42, spreadsheet.evaluate("A1"))

    def test_simple_formulas_with_references_invalid_value(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1", "=B2")
        spreadsheet.set("B2", "42.5")
        self.assertEqual("#Error", spreadsheet.evaluate("A1"))

    def test_simple_formulas_with_references_circular_reference(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1", "=B2")
        spreadsheet.set("B2", "=A1")
        self.assertEqual("#Circular", spreadsheet.evaluate("A1"))

    def test_simple_formulas_with_calculations_sums(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1", "=1+3")
        self.assertEqual(4, spreadsheet.evaluate("A1"))

    def test_simple_formulas_with_calculations_invalid_sums(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1", "=1+3.5")
        self.assertEqual("#Error", spreadsheet.evaluate("A1"))

    def test_simple_formulas_with_calculations_division(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1", "=8/2")
        self.assertEqual(4, spreadsheet.evaluate("A1"))

    def test_simple_formulas_with_calculations_invalid_divide_by_Zero(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1", "=1/0")
        self.assertEqual("#Error", spreadsheet.evaluate("A1"))

    def test_simple_formulas_with_calculations_multiplication(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1", "=2*2")
        self.assertEqual(4, spreadsheet.evaluate("A1"))

    #def test_simple_formulas_with_calculations_sum_and_multiplication(self):
    #    spreadsheet = SpreadSheet()
    #    spreadsheet.set("A1", "=1+3*2")
    #    self.assertEqual(7, spreadsheet.evaluate("A1"))







