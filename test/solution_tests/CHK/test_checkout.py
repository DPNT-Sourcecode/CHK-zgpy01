from solutions.CHK import checkout_solution


class TestCheckout():
    def test_checkout(self):
        assert checkout_solution.checkout('ABC') == 100
        assert checkout_solution.checkout(123) == -1
        assert checkout_solution.checkout('ABCa') == -1
        assert checkout_solution.checkout('EEB') == 80
        assert checkout_solution.checkout('AAAAAA') == 250
        assert checkout_solution.checkout('FFF') == 20
        assert checkout_solution.checkout('AAABBCDFFF') == 230

