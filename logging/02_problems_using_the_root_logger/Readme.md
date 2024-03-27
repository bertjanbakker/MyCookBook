This example demonstrates using the root logger can cause problems.

It demonstrates
- the first module to call basicConfig determines the root logger config
- subsequent calls to basicConfig are without effect which can be confusing
- per module log formatting is not possible when sharing a logger
- per module log file is not possible when sharing a logger