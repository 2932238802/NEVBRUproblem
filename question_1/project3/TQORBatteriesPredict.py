import pandas as pd

def TQORBatteriesPredict():
    
    """
    1. 读取退役数据
    2. 形成四个表 
    """
    
    """
    ————————————————————————————————————————————————————————————————————————
    默认值
    """
    data_path = './data.xls'
    tl_col_name = "搭载三元锂电池汽车销量"
    lf_col_name = '搭载磷酸铁锂电池汽车销量'
    
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
    # average_service_life_of_ternary_lithium_batteries_in_the_South = 5
    average_service_life_of_ternary_lithium_batteries_in_the_South:int
    
    # average_service_life_of_ternary_lithium_batteries_in_the_North = 7
    average_service_life_of_ternary_lithium_batteries_in_the_North:int
    
    # average_service_life_of_LFP_batteries_in_the_South = 9
    average_service_life_of_LFP_batteries_in_the_South:int
    
    # average_service_life_of_LFP_batteries_in_the_North = 6
    average_service_life_of_LFP_batteries_in_the_North:int
    
    # 南北比例
    proportion_of_the_South:float
    proportion_of_the_North = 1 - proportion_of_the_South
    
    # 北方三元锂元素
    
    # 搭载三元锂电池汽车销量
    
    # 搭载磷酸铁锂 电池汽车销量

    
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
    1. 对应年份
    2. 
    """
    
    # 打印输出 各个年份废弃的电池
    for year in range(2024,2031):
        
        # 南方三元锂电池平均使用年份
        # 北方三元锂电池平均使用年份
        # 南方磷电池平均使用年份
        # 北方方磷电池平均使用年份
        # tl 就是 三元锂
        # lf 就是 磷酸铁锂
        
        b_s_tl_year = year -  average_service_life_of_ternary_lithium_batteries_in_the_South + 1
        b_n_tl_year = year - average_service_life_of_ternary_lithium_batteries_in_the_North + 1
        b_s_lf_year = year - average_service_life_of_LFP_batteries_in_the_South + 1
        b_n_lf_year = year - average_service_life_of_LFP_batteries_in_the_North + 1
        
        data_b_s_tl_year = df.loc[df['年份']==b_s_tl_year,tl_col_name].iloc[0] * proportion_of_the_South # 这个布尔 Series 被用作 .loc 的 row_indexer 时，Pandas 会选择那些对应值为 True 的所有行。在上面的例子中，它会选择索引为 2 的那一行。
        data_b_n_tl_year = df.loc[df['年份']==b_n_tl_year,tl_col_name].iloc[0] * proportion_of_the_North
        data_b_s_lf_year = df.loc[df['年份']==b_s_lf_year,lf_col_name].iloc[0] * proportion_of_the_South
        data_b_n_lf_year = df.loc[df['年份']==b_n_lf_year,lf_col_name].iloc[0] * proportion_of_the_North
        
        sum = (data_b_s_tl_year + data_b_n_tl_year + data_b_s_lf_year + data_b_n_lf_year)
        print(f"按照模型推算出来：{year}年共有{sum}退役电池")
    
    """
    ————————————————————————————————————————————————————————————————————————
    """

def main():
    TQORBatteriesPredict()

if __name__ == '__main__':
    main()