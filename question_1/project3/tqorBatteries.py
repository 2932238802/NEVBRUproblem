import pandas as pd
# Total Quantity of Retired Batteries

def TQORBatteries():
    """
    1. 读取退役数据
    2. 形成四个表 
    3. 
    """
    
    
    """
    ————————————————————————————————————————————————————————————————————————
    默认值
    """
    data_path = './data.xls'
    
    """
    ————————————————————————————————————————————————————————————————————————
    """
    
    
    
    
    """
    ————————————————————————————————————————————————————————————————————————
    参数
    """
    # 南方三元锂电池平均使用年份
    # 北方三元锂电池平均使用年份
    # 南方磷电池平均使用年份
    # 北方方磷电池平均使用年份
    average_service_life_of_ternary_lithium_batteries_in_the_South = 5
    average_service_life_of_ternary_lithium_batteries_in_the_North = 7
    average_service_life_of_LFP_batteries_in_the_South = 9
    average_service_life_of_LFP_batteries_in_the_North = 6
    
    """
    ————————————————————————————————————————————————————————————————————————
    """
    
    
    
    """
    ————————————————————————————————————————————————————————————————————————
    读出数据
    """
    
    # df 是完整的数据
    df = pd.read_excel(data_path)
    print(df)
    """
    ————————————————————————————————————————————————————————————————————————
    """
    
    
    
    """
    ————————————————————————————————————————————————————————————————————————
    主要业务函数
    """
    
    # 打印输出 各个年份废弃的电池
    for year in range(2024,2031):
        
        # 南方三元锂电池平均使用年份
        # 北方三元锂电池平均使用年份
        # 南方磷电池平均使用年份
        # 北方方磷电池平均使用年份
        b_s_tl_year = year -  average_service_life_of_ternary_lithium_batteries_in_the_South + 1
        b_n_tl_year = year - average_service_life_of_ternary_lithium_batteries_in_the_North + 1
        b_s_lf_year = year - average_service_life_of_LFP_batteries_in_the_South + 1
        b_n_lf_year = year - average_service_life_of_LFP_batteries_in_the_North + 1
        
        data_b_s_tl_year = df[df['年份']==b_s_tl_year][]
        data_b_n_tl_year = df[df['年份']==b_n_tl_year]
        data_b_s_lf_year = df[df['年份']==b_s_lf_year]
        data_b_n_lf_year = df[df['年份']==b_n_lf_year]
        
        sum = (data_b_s_tl_year + data_b_n_tl_year + data_b_s_lf_year + data_b_n_lf_year)
        print(f"按照模型推算出来：{year}年共有{sum}退役电池")
    
    """
    ————————————————————————————————————————————————————————————————————————
    """
    
    
    
    
    
    
    
def main():
    TQORBatteries()
    
    
if __name__ == '__main__':
    main()