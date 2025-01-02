import datetime
import requests
import sqlite3
import os
import importlib.util

def interpret_bruhscript(code):
    variables = {}
    plugins = {}
    lines = code.strip().splitlines()

    def parse_expression(expr):
        if expr.isdigit():
            return int(expr)
        if expr in variables:
            return variables[expr]
        if expr.startswith('"') and expr.endswith('"'):
            return expr.strip('"')
        raise ValueError(f"Unknown variable or value: {expr}")

    def load_plugin(plugin_path):
        module_name = os.path.splitext(os.path.basename(plugin_path))[0]
        spec = importlib.util.spec_from_file_location(module_name, plugin_path)
        plugin_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(plugin_module)
        plugins[module_name] = plugin_module

    for line in lines:
        line = line.strip()
        if line.startswith("bruh start"):
            print("👊 BruhScript: Starting the program...")
        elif line.startswith("bruh end"):
            print("👊 BruhScript: Ending the program...")
        elif line.startswith("yeet"):
            message = line.replace("yeet", "").strip().strip('"')
            message = message.format(**variables)
            print(message)
        elif line.startswith("set"):
            _, var, value = line.split(maxsplit=2)
            variables[var] = parse_expression(value)
        elif line.startswith("load_plugin"):
            _, plugin_path = line.split(maxsplit=1)
            load_plugin(parse_expression(plugin_path))
        elif any(line.startswith(f"{plugin_command} ") for plugin_name in plugins for plugin_command in dir(plugins[plugin_name])):
            command_parts = line.split()
            plugin_command = command_parts[0]
            plugin_args = command_parts[1:]
            for plugin_name, plugin_module in plugins.items():
                if hasattr(plugin_module, plugin_command):
                    result = getattr(plugin_module, plugin_command)(*map(parse_expression, plugin_args), variables)
                    if isinstance(result, dict):
                        variables.update(result)
                    break
        else:
            print(f"❓ Bruh? Unknown command: {line}")
