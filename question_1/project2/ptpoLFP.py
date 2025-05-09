# Predicting the proportion of LFP

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np
try:
    plt.rcParams['font.sans-serif'] = ['SimHei']  
    plt.rcParams['axes.unicode_minus'] = False   
except Exception as e:
    print(f"设置中文字体失败，可能需要手动安装或配置字体: {e}")


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

# 预测磷酸铁锂的占比
def ptpoLFP():
    
    """
    ——————————————————————————————————————————————————————————————————
    常量区
    """
    # 数据路径
    file_path = './data.xls' 
    outfile_path = './out_ptpoLFP.xls'
    
    # 列名称
    sales_name = "搭载磷酸铁锂电池汽车销量"
    
    year = "年"
    """
    ——————————————————————————————————————————————————————————————————
    """ 
    
    
       
    """
    ——————————————————————————————————————————————————————————————————
    数据导入区域
    """
    # df 是完整的数据
    df = pd.read_excel(file_path)
    print(df)
    """
    ——————————————————————————————————————————————————————————————————
    """ 
    
        
    
    """
    ——————————————————————————————————————————————————————————————————
    数据预处理
    """
    train_X = df[[year]]            # 当你用双重中括号 [[]] 和一个或多个列名从 DataFrame 中选择数据时，Pandas 会返回一个 DataFrame
    train_y = df[sales_name]        # 单个中括号 [] 和一个列名从 DataFrame 中选择数据时，Pandas 会返回一个 Series。
    """
    ——————————————————————————————————————————————————————————————————
    """ 
    
    
    """
    ——————————————————————————————————————————————————————————————————
    变量区区域
    """
 
    
    model = LinearRegression()
    
    forward_year = list(range(2025,2031))
    
    x_future = np.array(forward_year).reshape(-1,1)
    
    x_all_year = np.array(list(train_X[year])+forward_year).reshape(-1,1)
    
    # 配置绘画api
    drawer = pltconfig(
        title= '2025-2030搭载磷酸铁锂电池汽车销量的预测',
        xlabel= '年份/年',
        ylabel= '新能源汽车的常量/万辆',
        xlim=[2016,2030],
        ylim=[0,2000]
    )
    """
    ——————————————————————————————————————————————————————————————————
    """
    
    

    
    
    
    """
    ——————————————————————————————————————————————————————————————————
    数据训练
    """
    
    model.fit(train_X,train_y)
    y_future = model.predict(x_future)
    y_all_year = model.predict(x_all_year)
   
    
    """
    ——————————————————————————————————————————————————————————————————
    """ 
    
    
    
    """
    ——————————————————————————————————————————————————————————————————
    数据存储
    """
    store_data = pd.DataFrame(
        {
            '年份':x_future.flatten(),
            '磷酸铁锂电池汽车的年销量':y_future
        }
    )
    
    try:
        store_data.to_excel(
            outfile_path,
            index=False,
            engine = 'openpyxl'
        )
        print(f"数据已经保存在了文件{outfile_path}里面...")
    except Exception as e:
        print(f"发生了错误{e}")
    
    
    """
    ——————————————————————————————————————————————————————————————————
    """ 
    
    
    
    """
    ——————————————————————————————————————————————————————————————————
    形成图形
    """ 
    drawer.scatter(
        train_X[year].values,
        train_y.values,
        color = 'blue',
        label = '历年磷酸铁锂电池汽车销量的预测',
        s=30
    )
    
    drawer.scatter(
        x_future,
        y_future,
        color='red', 
        label='预测销量',
        marker='*',
        s=40
        )
    
    drawer.plot(
        x_all_year,
        y_all_year,
        color = 'black',
        linestyle = '-',
        label = '线性回归趋势线'
    )
    
    """
    ——————————————————————————————————————————————————————————————————
    """ 
    
    
    drawer.legend()
    plt.show()
    
    
