from solutions.CHK import checkout_solution


class TestCheckout():
    def test_checkout(self):
        assert checkout_solution.checkout('STXYZ') == 82
        assert checkout_solution.checkout('SSSXXXYYYZZZ') == 180
        assert checkout_solution.checkout('') == 0

