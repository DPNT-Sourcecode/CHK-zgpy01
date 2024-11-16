from solutions.CHK import checkout_solution


class TestCheckout():
    def test_checkout(self):
        assert checkout_solution.checkout('HHHHH') == 45
        assert checkout_solution.checkout('VV') == 90
        assert checkout_solution.checkout('ABCDX') == 225
