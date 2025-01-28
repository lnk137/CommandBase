from typing import List

from manager.base import Command

class MathCommand(Command):
    def __init__(self):
        super().__init__()
        self.register_subcommand("add", AddCommand())
        self.register_subcommand("subtract", SubtractCommand())

    def execute(self, args: List[str]) -> None:
        print("数学命令")
        print("子命令:")
        for name, subcmd in self.subcommands.items():
            print(f"  {name:8} - {subcmd.description}")

    @property
    def description(self) -> str:
        return "数学相关操作"

class AddCommand(Command):
    def execute(self, args: List[str]) -> None:
        if len(args) != 2:
            print("用法: math add <num1> <num2>")
            return
        try:
            num1, num2 = map(float, args)
            print(f"结果: {num1 + num2}")
        except ValueError:
            print("请输入两个有效数字")

    @property
    def description(self) -> str:
        return "计算两个数的和"

class SubtractCommand(Command):
    def execute(self, args: List[str]) -> None:
        if len(args) != 2:
            print("用法: math subtract <num1> <num2>")
            return
        try:
            num1, num2 = map(float, args)
            print(f"结果: {num1 - num2}")
        except ValueError:
            print("请输入两个有效数字")

    @property
    def description(self) -> str:
        return "计算两个数的差"