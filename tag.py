#! /usr/bin/python
# -*- coding: utf-8 -*-
import os
import re
import time
import sys


def run_bash(command):
    output = os.popen(command, 'r')
    return output.read()


def current_branch():
    out = run_bash('git branch')
    for line in out.splitlines():
        if '*' in line:
            branch_name = line.replace('*', '').strip()
            return branch_name


def now_day():
    return time.strftime("%Y%m%d", time.localtime())


def last_tag(filters):
    out = run_bash('git tag')

    tags = out.splitlines()
    map(lambda tag: tag.strip(), tags)

    for f in filters:
        # tags = [tag for tag in tags if filter]
        tags = list(filter(f, tags))
    tags.sort(reverse=True)
    for i in tags:
        print(i)
    if len(tags):
        return tags[0]


def get_version(tag_name):
    regex = r"v(?P<version>\d+).(?P<miner_version>\d+).(?P<bug_version>\d+)"
    matches = re.search(regex, tag_name, re.MULTILINE)

    if matches:
        version = int(matches.group('version')
                      ) if matches.group('version') else 1
        miner_version = int(matches.group('miner_version')
                            ) if matches.group('miner_version') else 0
        bug_version = int(matches.group('bug_version')
                          ) if matches.group('bug_version') else 0
        return [version, miner_version, bug_version]


def build_next_version(version):
    if not version:
        return [1, 0, 0]
    if version[2] == 9:
        version[1] = version[1] + 1
        version[2] = 0
    else:
        version[2] = version[2] + 1
    return version


def create_tag(tag_name):
    print("git tag %s" % tag_name)
    run_bash("git tag %s" % tag_name)


def push_tag(tag_name):
    print("git push origin %s" % tag_name)
    run_bash("git push origin %s" % tag_name)


def pull(branch_name):
    print("git pull  %s" % branch_name)
    run_bash("git pull")


if __name__ == "__main__":
    if(len(sys.argv) > 1 and sys.argv[1]):
        branch_name = sys.argv[1]
    else:
        branch_name = current_branch()
    day = now_day()
    print("current_branch:" + branch_name)
    tag = last_tag([lambda x: branch_name in x, lambda x: day in x])
    version = []
    if tag:
        version = get_version(tag)
        print("last_tag:" + tag)
    else:
        print("last_tag not exist ")
    next_version = build_next_version(version)
    new_tag = "%s-v%d.%d.%d-%s" % (branch_name,
                                   next_version[0], next_version[1], next_version[2], day)
    if(len(sys.argv) > 2 and sys.argv[2]):
        new_tag = new_tag+"-"+sys.argv[2]
    print("new_tag:" + new_tag)
    pull(current_branch())
    create_tag(new_tag)
    push_tag(new_tag)
pass
