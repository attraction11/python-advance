import os

# 获取绝对路径
# print(os.path.abspath('..'))
# print(os.path.exists('/github'))
# print(os.path.isfile('/github'))
# print(os.path.isdir('/github'))
# print(os.path.join('/tmp/a', '/b/c'))


# pathlib 功能类似 os
from pathlib import Path
p = Path('.')
print(p.resolve())
p.is_dir()

# 创建目录，不存在的自动创建
q = Path('/tmp/a/b/c')
Path.mkdir(q, parents=True)