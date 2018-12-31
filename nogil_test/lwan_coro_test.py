import io
import subprocess
import importlib
import sys
import build_extension

def run(env, python_path):
  # build the extension
  # build_extension.build_ext(env)
  source = subprocess.check_output([python_path + " -c 'import wrapper; wrapper.main()'"],
          # cwd='./cython_lwan_coro/',
          env=env,
          shell=True,
          )
  failure_count = 0
  if len(source) != 30:
    failure_count = 1
  result_dict = {'failed': failure_count, 'stdout': source}
  return result_dict
