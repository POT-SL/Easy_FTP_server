import platform


# 判断CPU架构
cpu_arch = platform.machine()
if cpu_arch == 'ARM64':
    pass
else:
    pass

if __name__ == '__main__':

    # 尝试读取配置文件
    try:
        with open('arch', 'rw') as f:
            pass
    except:
        pass