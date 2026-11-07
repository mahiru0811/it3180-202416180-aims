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

    def test_discount_calculation(self):
        cart = Cart()
        cart.add_dvd(DigitalVideoDisc("Test", "Category", "Director", 100.0))
        # Giảm 20% trên 100$ phải còn lại 80$
        self.assertAlmostEqual(cart.total_cost_with_discount(20), 80.0)
        # Tỷ lệ chiết khấu > 100% hoặc < 0% phải văng lỗi ValueError
        with self.assertRaises(ValueError):
            cart.total_cost_with_discount(150)
        with self.assertRaises(ValueError):
            cart.total_cost_with_discount(-10)

if __name__ == "__main__":
    unittest.main()
