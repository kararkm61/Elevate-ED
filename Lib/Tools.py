#Lib/Tools.py | Program Tools
#install libarys
import os,sys,json,time
import datetime as dt
import tomllib as toml
from pathlib import Path

#Setting class
class Setting:
	data = {}
	file = Path()
	@classmethod
	def load(cls,path):
		pass
	@classmethod
	def save(cls):
		pass
	@classmethod
	def set(cls,key,value):
		pass
	@classmethod
	def get(cls,key):
		pass
#(i/o,lang,logger) class
class Console:
	#lang class
	class Lang:
		data = {}
		folder = Path()
		@classmethod
		def load(cls,path):
			pass
		@classmethod
		def set_lang(cls):
			pass
		@classmethod
		def get(cls,section,key):
			pass
	#logger class
	class Logger:
		folder = Path()
		info_file = Path()
		program_file = Path()
		@classmethod
		def load(cls,path):
			pass
		@classmethod
		def log(cls,text):
			pass
		@classmethod
		def info(cls,text):
			pass
	@classmethod
	def write(cls,text):
		pass
	@classmethod
	def entry(cls):
		pass
	@classmethod
	def page(cls,key):
		pass
	@classmethod
	def word(cls,key):
		pass
	@classmethod
	def mess(cls,key):
		pass
	@classmethod
	def warn(cls,key):
		pass
	@classmethod
	def error(cls,key):
		pass
	@staticmethod
	def clear():
		pass
	@staticmethod
	def color(text,type):
		pass
#if code is running
if __name__ == "__main__":
	print(" Run (Main.py) file")