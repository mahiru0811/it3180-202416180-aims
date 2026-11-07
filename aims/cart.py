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

    def remove_dvd(self, dvd):
        if dvd in self.items:
            self.items.remove(dvd)
            print("The disc has been removed")
            return True
        print("The disc is not in the cart")
        return False

    def total_cost(self):
        return sum(item.cost for item in self.items)
