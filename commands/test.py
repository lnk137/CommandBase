from typing import List
from manager.base import Command

class TestCommand(Command):
    def __init__(self):
        super().__init__()
        self.register_subcommand("test", Function())

    def execute(self, args: List[str]) -> None:
        print("test命令")
        print("子命令:")
        for name, subcmd in self.subcommands.items():
            print(f"  {name:8} - {subcmd.description}")

    @property
    def description(self) -> str:
        return "测试命令"

class Function(Command):
    def execute(self, args: List[str]) -> None:
        pass

    @property
    def description(self) -> str:
        return "创建一个新文件"

