from requests import certs, utils, adapters
import paths
import config
import requests.sessions
orig_session_init=requests.sessions.Session.__init__

def patched_where():
 return paths.app_path(u"cacert.pem")

def fix():
 certs.where=patched_where
 utils.DEFAULT_CA_BUNDLE_PATH=patched_where()
 adapters.DEFAULT_CA_BUNDLE_PATH=patched_where()
 requests.sessions.Session.__init__=patched_session_init

def patched_session_init(self):
 orig_session_init(self)
 if config.app["proxy"]["server"] != "" and config.app["proxy"]["port"] != "":
  self.proxies={"http":"http://{0}:{1}/".format(config.app["proxy"]["server"], config.app["proxy"]["port"]),
   "https": "https://{0}:{1}/".format(config.app["proxy"]["server"], config.app["proxy"]["port"]),
   "http": "socks5://{0}:{1}/".format(config.app["proxy"]["server"], config.app["proxy"]["port"]),
   "https": "socks5://{0}:{1}/".format(config.app["proxy"]["server"], config.app["proxy"]["port"])
   "http": "socks4://{0}:{1}/".format(config.app["proxy"]["server"], config.app["proxy"]["port"]),
   "https": "socks4://{0}:{1}/".format(config.app["proxy"]["server"], config.app["proxy"]["port"])}
  if config.app["proxy"]["user"] != "" and config.app["proxy"]["password"] != "":
   self.proxies={"http": "http://{0}:{1}@{2}:{3}/".format(config.app["proxy"]["user"], config.app["proxy"]["password"], config.app["proxy"]["server"], config.app["proxy"]["port"]),
    "https": "https://{0}:{1}@{2}:{3}/".format(config.app["proxy"]["user"], config.app["proxy"]["password"], config.app["proxy"]["server"], config.app["proxy"]["port"])
    "http": "socks5://{0}:{1}@{2}:{3}/".format(config.app["proxy"]["user"], config.app["proxy"]["password"], config.app["proxy"]["server"], config.app["proxy"]["port"]),
    "https": "socks5://{0}:{1}@{2}:{3}/".format(config.app["proxy"]["user"], config.app["proxy"]["password"], config.app["proxy"]["server"], config.app["proxy"]["port"]),
    "http": "socks4://{0}:{1}@{2}:{3}/".format(config.app["proxy"]["user"], config.app["proxy"]["password"], config.app["proxy"]["server"], config.app["proxy"]["port"]),
    "https": "socks4://{0}:{1}@{2}:{3}/".format(config.app["proxy"]["user"], config.app["proxy"]["password"], config.app["proxy"]["server"], config.app["proxy"]["port"])}
