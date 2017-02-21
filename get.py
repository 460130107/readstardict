# -*- coding:utf-8 -*-
import os
import sys
import re

from pystardict import Dictionary

def delkuohao(strin):
	tmp=strin
	lind=tmp.find(r"(")
	while lind>=0:
		rind=tmp.find(r")")
		if rind>lind:
			tmp=tmp[:lind]+tmp[rind+1:]
			lind=tmp.find(r"(")
		else:
			break
	lind=tmp.find(r"[")
	while lind>=0:
		rind=tmp.find(r"]")
		if rind>lind:
			tmp=tmp[:lind]+tmp[rind+1:]
			lind=tmp.find(r"[")
		else:
			break
	return tmp

def retrievefirst(strin):
	tmp=strin[2:]
	ind=tmp.find("\n")
	if ind>0:
		tmp=tmp[:ind]
	ind=tmp.find(";")
	if ind>0:
		tmp=tmp[:ind]
	return tmp

def resolveword(strin):
	return delkuohao(retrievefirst(strin)).strip()

def getrans(dicpath,rsf):

	zhPattern = re.compile(u'[\u4e00-\u9fa5]+')
	dicts_dir = os.path.join(os.path.dirname(__file__))
	print dicts_dir
	dict = Dictionary(dicpath,True)

	with open(rsf,"wb") as fwrt:
		for k,v in dict.iteritems():
			if zhPattern.search(k):
				tmp=k+"|||"+resolveword(v)+"\n"
				fwrt.write(tmp.encode("utf-8","ignore"))

if __name__ == '__main__':
	getrans(sys.argv[1].decode("gbk"),sys.argv[2].decode("gbk"))
