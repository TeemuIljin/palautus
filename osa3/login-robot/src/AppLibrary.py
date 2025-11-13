import sys
import os
import io
import importlib
import runpy
from contextlib import redirect_stdout

class AppLibrary:
    def __init__(self):
        base = os.path.dirname(__file__)
        if base not in sys.path:
            sys.path.insert(0, base)
        self._inputs = []
        self._output = ""

    # Robot calls "Input"
    def Input(self, text):
        self._inputs.append(str(text))

    # Robot calls "Run Application"
    def Run_Application(self):
        base = os.path.dirname(__file__)
        input_text = "\n".join(self._inputs) + ("\n" if self._inputs else "")
    # (debug prints removed)
        stdin = io.StringIO(input_text)
        stdout = io.StringIO()
        old_stdin = sys.stdin
        try:
            sys.stdin = stdin
            with redirect_stdout(stdout):
                tried = False

                # 1) try importing common module names and call main() if present
                for modname in ("index", "app", "main"):
                    try:
                        importlib.invalidate_caches()
                        mod = importlib.import_module(modname)
                        importlib.reload(mod)
                        # if module defines main(), call it so it produces output
                        if hasattr(mod, "main") and callable(getattr(mod, "main")):
                            mod.main()
                            tried = True
                            break
                        # if module has no main, don't treat import as success -> try running as script
                    except Exception:
                        continue

                # 2) try running common filenames in this src folder
                if not tried:
                    candidates = ["index.py", "app.py", "main.py"]
                    for fname in os.listdir(base):
                        if fname.endswith(".py") and fname not in candidates:
                            candidates.append(fname)
                    for fname in candidates:
                        path = os.path.join(base, fname)
                        if not os.path.isfile(path):
                            continue
                        try:
                            content = open(path, "r", encoding="utf-8").read()
                        except Exception:
                            content = ""
                        if "__name__ == \"__main__\"" in content or "def main(" in content or fname in ("index.py", "app.py", "main.py"):
                            try:
                                runpy.run_path(path, run_name="__main__")
                                tried = True
                                break
                            except Exception:
                                continue

                if not tried:
                    raise RuntimeError(f"Could not find application entry (index.py/app.py/main.py) in {base}")
        finally:
            sys.stdin = old_stdin
            self._output = stdout.getvalue()
            # captured output stored in self._output for assertions
            self._inputs = []

    # Robot calls "Application Output Should Contain"
    def Application_Output_Should_Contain(self, text):
        if str(text) not in self._output:
            raise AssertionError(f"Output did not contain '{text}'.\n\nCaptured output:\n{self._output}")