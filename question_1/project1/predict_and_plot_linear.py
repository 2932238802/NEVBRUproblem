import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt


    
def pltconfig(title="预测图", xlabel="X轴", ylabel="Y轴", xlim=None, ylim=None): 
    plt.figure(figsize=(10, 6)) 
    plt.title(title)
    
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    
    
    if xlim:
        plt.xlim(xlim) 
    if ylim:
        plt.ylim(ylim) 
    plt.grid(True)
    return plt
 


def predict_and_plot_linear(df_input, year_col, value_col, future_years_list, plot_title=""):
    """
    ——————————————————————————————————————————————————————————————————————————————————————————————————————
    对给定列进行线性回归预测并绘图

    Args:
        df_input (pd.DataFrame): 包含历史数据的DataFrame，年份应为索引
        year_col (str): 实际用作特征的年份列名 (在reset_index后得到，通常就是 '年')
        value_col (str): 需要预测的销量列名 (例如 '该年的全国新能源汽车的总销量（万辆）')
        future_years_list (list): 需要预测的未来年份列表 (例如 [2025, 2026, 2027, 2028, 2029, 2030])
        title_prefix (str): 图表标题的前缀 (例如 "全国总销量: ")，用于区分不同预测的图表
    预测未来 2-25 - 2030 的销量
    """
    
    
    
    
    
    
    
    
    
    """
    ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
    一. 训练模型  线性训练
    """
    # 数据准备
    train_X = df_input[[year_col]]
    train_y = df_input[value_col]
    
    # 训练模型
    model = LinearRegression()
    model.fit(train_X,train_y)
    
    # # 打印模型系数和截距 (可选，用于理解模型)
    # print("—————————————————— 初步计算结果 ——————————————————")
    # print(f"\n模型 '{plot_title}':")
    # print(f"  斜率 (Coefficient): {model.coef_[0]:.2f}")
    # print(f"  截距 (Intercept): {model.intercept_:.2f}")
    
    plt_instance = pltconfig(
        title= '2025-2030新能源汽车的预测',
        xlabel='年份/年',
        ylabel= "新能源汽车的常量/万辆",
        xlim=[2016,2030],
        ylim=[0,2500]
    )
    
    # 形成列表 2025-2030  x_future= np.array(future_years_list).reshape(-1,1)
    # 预测对应年份   y_future = model.predict(x_future)  
    x_future= np.array(future_years_list).reshape(-1,1)
    y_future = model.predict(x_future)  
    
    """
    ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
    """
    
    
    
    
    
    
    
    
    
    
    
    
    
    """
    ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
    二. 存储训练结果
    """
    predict_data = pd.DataFrame(
        {
            '年份':future_years_list,
            f'预测_{value_col}':y_future
        }
    )
    
    out_excel_name = './outpredict.xls'
    
    try:
        predict_data.to_excel(
            out_excel_name,
            index=False,                     # 不写入索引
            engine='openpyxl'
        )
        print(f"2025-2030的数据,已经保存到文件{out_excel_name}")
    except Exception as e:
        print(f"发生{e}意外错误")
    """
    ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
    """
    
    
    
    
    
    
    
    
    
    
    
    
    """
    ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
    二. 打印训练结果
    """
    print("\n———————————————————— 预测结果:————————————————————")
    for year, pred_value in zip(future_years_list, y_future):
        print(f"  年份: {year}, 预测{value_col}: {pred_value:.2f} 万辆")
      
    # 加上预测的年份
    all_years_for_line = np.array(                              
        list(train_X[year_col]) + future_years_list
        ).reshape(-1, 1)                                        # -1 表示的意思是 自己推断横
    
    # 预测一整个年份 all   
    line_predictions = model.predict(all_years_for_line) 
    
    # 形成销售散点图                                                        
    plt_instance.scatter(            
        train_X,                # 横坐标 是 train_X
        train_y,                # 纵坐标 是 train_y
        color='blue',           # 颜色是 蓝色
        label='历史销量', 
        s=50                    # s 是 面积大小
        ) 
    
    # 形成预测散点图                                                        
    plt_instance.scatter(
        x_future,
        y_future,
        color='red', 
        label='预测销量',
        marker='*',
        s=50
        )
    
    # 线性历史线
    plt_instance.plot(
        train_X,
        train_y,
        color='red',
        linestyle='-',
        label='历史线性曲线'
        )
    
    # 线性预测线
    plt_instance.plot(
        all_years_for_line,
        line_predictions, 
        color='black', 
        linestyle='-', 
        label='线性回归趋势线'
        )
    
    # 打上标记
    plt_instance.legend()
    
    # 显示
    plt_instance.show()
