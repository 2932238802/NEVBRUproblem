class Battery:
    north_x = 5
    south_x = 7

    def __init__(self, year_n: int, year_t: int):
        """
        Battery类用于计算电池的循环和日历衰减速率。

        Args:
            year_n (int): 循环寿命
            year_t (int): 日历寿命
        """
        self._year_n = year_n
        self._year_t = year_t

    @property
    def year_n(self) -> int:
        return self._year_n

    @property
    def year_t(self) -> int:
        return self._year_t

    def cycle_degradation_rate(self) -> float:
        """计算循环衰减速率。

        Returns:
            float: 循环衰减速率
        """
        return 0.2 / self.year_n

    def calendar_degradation_rate(self) -> float:
        """计算日历衰减速率。

        Returns:
            float: 日历衰减速率
        """
        return 0.2 / self.year_t

    def get_lifetime(self, region: str = 'n') -> float:
        """根据地区计算电池的使用寿命。

        Args:
            region (str): 'n'表示南方，'s'表示北方

        Returns:
            float: 计算得到的电池寿命
        """
        if region == 'n':
            print("----------南方的电池寿命----------")
            return 0.2 / (self.cycle_degradation_rate() * self.north_x + self.calendar_degradation_rate())
        else:
            print("----------北方的电池寿命----------")
            return 0.2 / (self.cycle_degradation_rate() * self.south_x + self.calendar_degradation_rate())
