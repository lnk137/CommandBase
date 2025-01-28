from typing import Dict
from manager.base import Command
from manager.exceptions import CommandNotFoundError

class CommandHandler:
    def __init__(self):
        self._commands: Dict[str, Command] = {}

    def register_command(self, name: str, command: Command) -> None:
        self._commands[name.lower()] = command

    def execute_command(self, input_str: str) -> None:
        parts = input_str.strip().split()
        if not parts:
            return

        cmd_name = parts[0].lower()
        args = parts[1:] if len(parts) > 1 else []

        if cmd_name not in self._commands:
            raise CommandNotFoundError(f"命令不存在: {cmd_name}")

        command = self._commands[cmd_name]
        if args and args[0] in command.subcommands:
            subcommand_name = args[0]
            sub_args = args[1:]
            command.execute_subcommand(subcommand_name, sub_args)
        else:
            command.execute(args)

    def get_all_commands(self) -> Dict[str, Command]:
        return self._commands.copy()