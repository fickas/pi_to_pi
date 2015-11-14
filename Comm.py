__author__ = 'Frankie'


import requests
import ast


class Comm:

    def __init__(self, ip):
        self.full_ip = "http://" + ip + ":5000"
        self.ip = ip


    def send(self, row):
        r = requests.post(self.full_ip, json=row)

    def get_table(self):
        try:
            f = open(self.ip + ".txt")
        except:
            return []
        _data = f.readlines()
        data = []
        for line in _data:
            data.append(ast.literal_eval(line))
        return data

    def get_size(self):
        try:
            f = open(self.ip + ".txt")
        except:
            return -1
        return len(f.readlines())

