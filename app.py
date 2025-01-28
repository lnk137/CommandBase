import json
import os

from commands.math import MathCommand
from commands.test import TestCommand
from manager.exceptions import CommandError
from manager.handler import CommandHandler
from manager.system import HelpCommand, ExitCommand


class App:
    def __init__(self):
        self._ensure_config_file()  # 检查或创建 config.json
        self.handler = CommandHandler()
        self._register_core_commands()

    def _ensure_config_file(self):
        """确保 config.json 文件存在，不存在则创建"""
        config_path = "config.json"
        if not os.path.exists(config_path):
            default_config = {}
            with open(config_path, "w") as config_file:
                json.dump(default_config, config_file, indent=4)
            print(f"默认配置文件 '{config_path}' 已创建")

    def _register_core_commands(self):
        self.handler.register_command("help", HelpCommand(self.handler))
        self.handler.register_command("exit", ExitCommand())
        self.handler.register_command("math", MathCommand())
        self.handler.register_command("test", TestCommand())

    def run(self):
        print("欢迎使用控制台应用")
        print("输入 'help' 查看可用命令\n")

        while True:
            try:
                user_input = input("> ").strip()
                self.handler.execute_command(user_input)
            except CommandError as e:
                print(f"错误: {str(e)}")
            except Exception as e:
                print(f"系统错误: {str(e)}")


if __name__ == "__main__":
    app = App()
    app.run()
