from runner.Main import Main


if __name__ == '__main__':
    print("请选择一种模式(输入单词) 1：threading; 2:multiprocessing; 3:ordinary")
    n = input()
    Main().run(n)
