import subprocess
import sys

class Sandbox:
    def execute(self, python_code):
        try:
            allowed_modules = ['math', 'random']
            sandboxed_code = compile(python_code, '<string>', 'exec', dont_inherit=True)
            globals_dict = {}
            locals_dict = {}
            for module in allowed_modules:
                globals_dict[module] = __import__(module)
            exec(sandboxed_code, globals_dict, locals_dict)
            return locals_dict.get('__sandbox_result__', None)
        except Exception as e:
            return str(e)

