#!/usr/bin/env python
import subprocess
import argparse
import sys

p = argparse.ArgumentParser()

if len(sys.argv) == 3:
    p.add_argument("stg", help = "specs for stage")
    p.add_argument("commit_message", help = "CommitMessage <message should be in triple dual-quotes.>")
elif len(sys.argv) == 2:
    p.add_argument("commit_message", help = "CommitMessage <message should be in triple dual-quotes.>")


a = p.parse_args()


subprocess.call("git status", shell = True)

if len(sys.argv) == 3:
    subprocess.call("git add -" + a.stg, shell = True)
    t = a.commit_message
else:
    subprocess.call("git add .", shell = True)
    t = list(str(subprocess.check_output("git status --porcelain", shell = True)))
    if len(sys.argv) > 1 and a.commit_message != "":
        t = a.commit_message


m = 0
cmsg = ""

for a in t:
    if a == '\\':
        m = 1
        a = ''
    elif m ==1:
        a = '; '
        m = 0
    if a == '\'':
        a = ''
    cmsg += str(a)


subprocess.call("git commit -m " + "\"" + cmsg + "\"" + " && git push origin master", shell = True)