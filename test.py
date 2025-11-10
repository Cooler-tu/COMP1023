import sys
print("Python 路径:", sys.executable)
print("Python 版本:", sys.version)

try:
    import numpy as np
    print("NumPy 版本:", np.__version__)
    print("NumPy 安装成功！")
except ImportError as e:
    print("导入 NumPy 失败:", e)