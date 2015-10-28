import unittest
from logger import logger, publish
import time
from logger.common import configWriter

class TestPublish(unittest.TestCase): 
  
  def setUp(self):
    configWriter.CreateConfigFile("pconfig.cfg", "Constants", "Socket", "tcp://127.0.0.1:4000")
    configWriter.CreateConfigFile("pconfig.cfg", "Constants", "LogDir", ".")
    configWriter.CreateConfigFile("pconfig.cfg", "Constants", "Filename", "metric.log")
    publish.setLogger("demo_publish", "pconfig.cfg")

  def test_ReportLatency(self):
    i = 10
    j = 2
    while i > 0:
      self.demo_log(j * 2, j)
      i = i - 1
      j = j * 2

  @publish.ReportLatency("demo", "demo")
  def demo_log(self, a, b):
    #logger.reportLatency("report latency", "demo-metric", demo_action, a, b)
    return self.demo_action(a, b)

  def demo_action(self, a, b):
    time.sleep(1)
    return a / b
  
if __name__ == '__main__':
  unittest.main()
