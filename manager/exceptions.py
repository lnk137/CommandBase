class CommandError(Exception):
    """命令相关异常的基类"""
    pass

class CommandNotFoundError(CommandError):
    """命令未找到异常"""
    pass