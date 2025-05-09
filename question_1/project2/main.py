
import ptpoLFP
import ptpoTernaryLithiumBatteries

def main():
    ptpoLFP.ptpoLFP()
    ptpoTernaryLithiumBatteries.ptpoTernaryLithiumBatteries()

if __name__ == '__main__':
    print("开始进行 电池销售预测")
    main()