
# Total Quantity of Retired Batteries

class TQORBatteries:
    """
    1. 读取退役数据
    2. 形成四个表 
    3. 
    """
    
    # 南方三元锂电池平均使用年份
    # 北方三元锂电池平均使用年份
    # 南方磷电池平均使用年份
    # 北方方磷电池平均使用年份
    average_service_life_of_ternary_lithium_batteries_in_the_South = 5
    average_service_life_of_ternary_lithium_batteries_in_the_North = 7
    average_service_life_of_LFP_batteries_in_the_South = 9
    average_service_life_of_LFP_batteries_in_the_North = 6
    
    # 这个是推导的模型
    def derived_model(self):
        pass