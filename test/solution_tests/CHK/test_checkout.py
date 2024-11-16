from solutions.CHK import checkout_solution


class TestCheckout():
    def test_checkout(self):
        assert checkout_solution.checkout('ABC') == 100
        assert checkout_solution.checkout(123) == -1
        assert checkout_solution.checkout('ABCa') == -1
        assert checkout_solution.checkout('EEB') == 110
        assert checkout_solution.checkout('AAAAAAA') == 250


