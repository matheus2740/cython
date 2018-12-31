import subprocess
import importlib
import json

def run(env):
  # Build the extension when installing the Cython in slapos
  # subprocess.call(['python3', 'nogil_extension.py', 'build_ext', '--inplace'], env=env)
  source = ''
  failure_count = 0
  try:
      nogil_extension = importlib.import_module('nogil_extension')
  except ImportError as e:
      source = str(e)
      failure_count = 1
  else:
      source = nogil_extension.bag()
      if source != '4.0\n42.0':
          failure_count = 1
  
  result_dict = {'failed':failure_count, 'stdout':source}
  return result_dict
  # print(json.dumps(result_dict))
