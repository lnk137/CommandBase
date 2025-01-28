from typing import List

from manager.base import Command

class FileCommand(Command):
    def __init__(self):
        super().__init__()
        self.register_subcommand("create", CreateFileCommand())
        self.register_subcommand("delete", DeleteFileCommand())

    def execute(self, args: List[str]) -> None:
        print("文件命令：使用子命令 'create' 或 'delete'")
        print("子命令:")
        for name, subcmd in self.subcommands.items():
            print(f"  {name:8} - {subcmd.description}")

    @property
    def description(self) -> str:
        return "文件操作命令"

class CreateFileCommand(Command):
    def execute(self, args: List[str]) -> None:
        if len(args) != 1:
            print("用法: file create <filename>")
            return
        filename = args[0]
        try:
            with open(filename, "w") as f:
                f.write("")
            print(f"文件 '{filename}' 创建成功！")
        except Exception as e:
            print(f"文件创建失败: {e}")

    @property
    def description(self) -> str:
        return "创建一个新文件"

class DeleteFileCommand(Command):
    def execute(self, args: List[str]) -> None:
        if len(args) != 1:
            print("用法: file delete <filename>")
            return
        filename = args[0]
        try:
            import os
            os.remove(filename)
            print(f"文件 '{filename}' 删除成功！")
        except FileNotFoundError:
            print(f"文件 '{filename}' 不存在")
        except Exception as e:
            print(f"文件删除失败: {e}")

    @property
    def description(self) -> str:
        return "删除指定文件"