import os
import time
import sys
import colorama
import admin_operations_system


class Data:
  def save(file, data):
    trueFile = open(file)
    file.write(data)
  def load(file, data):
    trueFile = open(file)
    trueFile.readline(100)
class Console:
  def Type(words):
    punctuation = ['.', ',', '!', ';', ':']
    for char in words:
      if char in punctuation:
        time.sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.25)
      else:

        time.sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()

  def clear(isServer=True):
    os.system("clear")
  def commandPrompt(key, function):
    main = input(">")
    if main == key:
      function()
  def Commentary(text):
    print(colorama.Style.DIM+ text + colorama.Style.NORMAL)
  def Warn(text):
    print(colorama.Fore.RED + text + colorama.Fore.RESET)

class Misc:
  def Wait(interval):
    time.sleep(interval)
  def Help():
    type("Admin Operations System is a library created 10-21-2021 and was updated 11-26-2021. AOS exists to help make Python better, easier to use, and to help with the world!\n\n\n")