from src.dynamicprogramming.canplaceflowers import CanPlaceFlowers

class TestCanPlaceFlowers:
    def test_case_2_available_spots_1_flowers(self):
        obj = CanPlaceFlowers()
        assert obj.canPlaceFlowers([1,0,0,0,1], 1) == True

    def test_case_1_available_spots_2_flowers(self):
        obj = CanPlaceFlowers()
        assert obj.canPlaceFlowers([1,0,0,0,1], 2) == False

    def test_empty_bed(self):
        obj = CanPlaceFlowers()
        assert obj.canPlaceFlowers([], 0) is True
        assert obj.canPlaceFlowers([], 1) is False

    def test_single_slot_available(self):
        obj = CanPlaceFlowers()
        assert obj.canPlaceFlowers([0], 1) is True
        assert obj.canPlaceFlowers([0], 2) is False

    def test_single_slot_occupied(self):
        obj = CanPlaceFlowers()
        assert obj.canPlaceFlowers([1], 0) is True
        assert obj.canPlaceFlowers([1], 1) is False

    def test_all_zeroes_capacity(self):
        obj = CanPlaceFlowers()
        assert obj.canPlaceFlowers([0,0,0,0,0], 3) is True
        assert obj.canPlaceFlowers([0,0,0,0,0], 4) is False

    def test_all_ones(self):
        obj = CanPlaceFlowers()
        assert obj.canPlaceFlowers([1,1,1], 0) is True
        assert obj.canPlaceFlowers([1,1,1], 1) is False

    def test_alternating_patterns(self):
        obj = CanPlaceFlowers()
        assert obj.canPlaceFlowers([1,0,1,0,1], 1) is False
        assert obj.canPlaceFlowers([0,0,1,0,0], 2) is True

    def test_zero_flowers_always_true(self):
        obj = CanPlaceFlowers()
        assert obj.canPlaceFlowers([1,0,1], 0) is True

    def test_negative_flowers_treated_as_true(self):
        obj = CanPlaceFlowers()
        assert obj.canPlaceFlowers([0,0,0], -1) is True
