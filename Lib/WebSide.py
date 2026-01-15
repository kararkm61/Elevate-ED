#Lib/WebSide.py | Web Side Server Tools
#install libarys
import re,sys,ssl,json,time
import hashlib as hash
import urllib.parse as parse
import urllib.request as request
import hashlib as hash
from pathlib import Path

#url class
class URL:
	def __init__(self,base):
		self.base = base.strip().rstrip("/")
	def __truediv__(self,other):
		new_path = str(other).strip('/')
		return URL(f"{self.base}/{new_path}")
	def add_query(self,**kwargs):
		query_string = parse.urlencode(kwargs)
		return URL(f"{self.base}?{query_string}")
	def __str__(self):
		return self.base
	def __repr__(self):
		return f"URL({self.base})"
#user class
class User:
	file = Path()
	id = None
	name = None
	date = None
	email = None
	password = None
	@classmethod
	def load(cls,path):
		pass
	@classmethod
	def get_json_data(cls):
		pass
#web manager class
class WebManager:
	pass