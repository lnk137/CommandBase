import sys
from typing import List
from manager.base import Command

class HelpCommand(Command):
    def __init__(self, handler):
        super().__init__()
        self.handler = handler

    def execute(self, args: List[str]) -> None:
        print("\n可用命令：")
        for name, cmd in self.handler.get_all_commands().items():
            print(f"  {name:8} - {cmd.description}")
        print()

    @property
    def description(self) -> str:
        return "显示帮助信息"

class ExitCommand(Command):
    def execute(self, args: List[str]) -> None:
        print("再见！")
        sys.exit(0)

    @property
    def description(self) -> str:
        return "退出程序"