import pytest
from sys import path
from datetime import datetime as Datetime

path.insert(1, '../')
from Code.Tools import Tools


class TestTools:
    @pytest.fixture
    def setUp(self):
        self.time1 = Datetime(2020, 5, 17)
        self.time2 = Datetime(2022, 10, 29)
        self.time3 = Datetime(2022, 12, 1)

    def test_add_time(self, setUp):
        assert Tools.add_time(self.time1, 13) == Datetime(2020, 5, 30)
        assert Tools.add_time(self.time2, 1) == Datetime(2022, 10, 30)
        assert Tools.add_time(self.time3, 0) == self.time3

    def test_find_delay(self, setUp):
        assert Tools.find_delay(self.time1, self.time2) == 895
        assert Tools.find_delay(self.time2, self.time3) == 33
        assert Tools.find_delay(self.time1, self.time3) == 928
