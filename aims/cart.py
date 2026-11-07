MAX_NUMBERS_ORDERED = 20


class Cart:
    """Giỏ hàng chứa tối đa MAX_NUMBERS_ORDERED đĩa DVD."""

    def __init__(self):
        self.items = []

    def add_dvd(self, dvd):
        # Đổi từ > thành >= để chặn khi giỏ đã đủ số lượng tối đa
        if len(self.items) >= MAX_NUMBERS_ORDERED:
            print("The cart is almost full")
            return False
        self.items.append(dvd)
        return True
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
    def remove_dvd(self, dvd):
        if dvd in self.items:
            self.items.remove(dvd)
            print("The disc has been removed")
            return True
        print("The disc is not in the cart")
        return False

    def total_cost_with_discount(self, percent):
        if percent < 0 or percent > 100:
            raise ValueError("Discount percent must be between 0 and 100")
        return self.total_cost() * (100 - percent) / 100
    
    def total_cost(self):
        return sum(item.cost for item in self.items)
