import os
from pydoc import resolve
import test_pb2
import test_pb2_grpc
import time
import json
import grpc
from flask import Flask, make_response
import logging
import pandas as pd
from google.protobuf import struct_pb2
from google.protobuf.json_format import MessageToJson


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = test_pb2_grpc.TestServiceStub(channel)
        response = stub.test(test_pb2.TestRequest
                (filename = input("Name of file: "),
                nrows=int(input("Inter quantity of rows: "))))
        

        #struct_client = struct_pb2.Struct() 
        #struct_client.ParseFromString(response.message) #serialize to struct
        msgjson = MessageToJson(response.message)
        msgdict = json.loads(msgjson)
        dfmsg_client = pd.DataFrame(msgdict['data'], map(int, msgdict['index']),
                    msgdict['columns'])
        
        print(dfmsg_client)
        

def close(channel):
    channel.close()

if __name__ == "__main__":
    logging.basicConfig()
    run()


        # data = response.message
        # with open("./serializedFile", "rb") as fd:
        #     data.ParseFromString(fd.read())
        # body_json = struct_pb2.Struct()
        # body_json.ParseFromString(response.message)
        # bodydict = dict(body_json)


        # bodydf = pd.DataFrame.from_dict(bodydict, orient='index')
        # bodydf

        # some_any1 = any_pb2.Any()
        # fd1 = some_any1.Unpack(response.message)


"""counter = response.count
                if counter % 1000 == 0:
                    print("%4f : reso=%s : procid=%i" % 
                    (time.time() - start, response.count, pid))"""




"""def get_data(stub):
    response = stub.test(test_pb2.TestRequest())
    return response.message

def convert_to_json(input_data):
    data = input_data.split('\n')[1:-1]
    json_response = []

    for line in data:
        components = line.split(',')
        json_response.append(components)
    
    return json.dumps(json_response)

def run():
    with grpc.insecure_channel("localhost:9999") as channel:
        stub = test_pb2_grpc.TestServiceStub(channel)
        input_data = get_data(stub)
        resp = make_response(convert_to_json(input_data))
        return resp"""