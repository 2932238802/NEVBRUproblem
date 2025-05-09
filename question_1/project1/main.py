import predict_and_plot_linear
import pandas as pd
import matplotlib.pyplot as plt

try:
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体为黑体
    plt.rcParams['axes.unicode_minus'] = False   # 解决保存图像是负号'-'显示为方块的问题
except Exception as e:
    print(f"设置中文字体失败，可能需要手动安装或配置字体: {e}")
    

def main():
    
    """
    ——————————————————————————————————————————————————————————————————————————————————————————————————————
    预测未来 2-25 - 2030 的销量
    """
    # 文件路径 
    file_path = './data.xls' 
    
    # 预测的名字列
    df = pd.read_excel(file_path)
    
    sales_name = '该年的全国新能源汽车的总销量（万辆）'
    future_years = list(range(2025, 2030 + 1))
    
    try:
        print("\n ———————————————————— Full DataFrame: ————————————————————")
        print(df)
        predict_and_plot_linear.predict_and_plot_linear(
            df_input= df,
            year_col= '年',
            value_col =  sales_name,
            future_years_list =  future_years, 
            plot_title = "全国新能源汽车销量预测"
            )

    except FileNotFoundError:
        print(f"文件 '{file_path}' 未找到。请确保文件路径正确。")
        
    except ImportError as e:
        if "xlrd" in str(e).lower():
            print("缺少读取 .xls 文件的库")
            
        elif "openpyxl" in str(e).lower():
            print("缺少读取 .xlsx 文件的库")
        else:
            print(f"导入错误: {e}")
            
    except Exception as e:
        print(f"读取文件时发生错误: {e}")

    """
    ——————————————————————————————————————————————————————————————————————————————————————————————————————
    """
    
    
if __name__ == '__main__':
    main()