# 这是一个示例 Python 脚本。

# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。
import os
from morningtalk_weekly import MorningTalkWeekly
# 设置工作目录
os.chdir("")

# 实例化MorningTalkWeekly类并生成报告
morningtalk_weekly = MorningTalkWeekly(
    start_date="20240603",
    end_date="20240607",
    yaml_path='mt_weekly.yaml',
    output_dir='.'
)
morningtalk_weekly.generate_word_report()
