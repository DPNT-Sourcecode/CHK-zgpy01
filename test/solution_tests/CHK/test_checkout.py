from solutions.CHK import checkout_solution


class TestCheckout():
    def test_checkout(self):
        assert checkout_solution.checkout('AAABBCD') == 210
        assert checkout_solution.checkout('ABC') == 100
        assert checkout_solution.checkout(123) == -1
