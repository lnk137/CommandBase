from abc import ABC, abstractmethod
from typing import Dict, List
from manager.exceptions import CommandNotFoundError


class Command(ABC):
    """命令模式抽象基类"""

    def __init__(self):
        self.subcommands: Dict[str, Command] = {}

    def register_subcommand(self, name: str, command: "Command") -> None:
        self.subcommands[name.lower()] = command

    def execute_subcommand(self, subcommand: str, args: List[str]) -> None:
        if subcommand in self.subcommands:
            self.subcommands[subcommand].execute(args)
        else:
            raise CommandNotFoundError(f"子命令不存在: {subcommand}")

    @abstractmethod
    def execute(self, args: List[str]) -> None:
        pass

    @property
    @abstractmethod
    def description(self) -> str:
        pass