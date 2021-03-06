
import subprocess
import sys
import setup_util
import os

def start(args):
  setup_util.replace_text("express/app.js", "mongodb:\/\/.*\/hello_world", "mongodb://" + args.database_host + "/hello_world")
  setup_util.replace_text("express/app.js", "localhost", args.database_host)

  try:
    subprocess.check_call("npm install", shell=True, cwd="express")
    subprocess.Popen("NODE_ENV=production node app", shell=True, cwd="express")
    return 0
  except subprocess.CalledProcessError:
    return 1
def stop():
  p = subprocess.Popen(['ps', 'aux'], stdout=subprocess.PIPE)
  out, err = p.communicate()
  for line in out.splitlines():
    if 'node app' in line:
      pid = int(line.split(None, 2)[1])
      try:
        os.kill(pid, 9)
      except OSError:
        pass
  return 0
