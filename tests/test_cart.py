import unittest
from aims.cart import Cart, MAX_NUMBERS_ORDERED
from aims.dvd import DigitalVideoDisc

class TestCart(unittest.TestCase):
    def test_add_dvd_until_full(self):
        cart = Cart()
        # Thêm đủ 20 đĩa vào giỏ
        for i in range(MAX_NUMBERS_ORDERED):
            added = cart.add_dvd(DigitalVideoDisc(f"DVD {i}", "Category", "Director", 10.0))
            self.assertTrue(added)
        
        # Thử thêm đĩa thứ 21 -> phải trả về False
        extra_dvd = DigitalVideoDisc("Overflow DVD", "Category", "Director", 10.0)
        added_extra = cart.add_dvd(extra_dvd)
        self.assertFalse(added_extra)

if __name__ == "__main__":
    unittest.main()
