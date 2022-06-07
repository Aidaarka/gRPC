import os
from pydoc import resolve
from urllib import response
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

        response_data = stub.data(test_pb2.TestRequest
                (filename = input("Name of file: "),
                nrows=int(input("Inter quantity of rows: "))))

        #struct_client = struct_pb2.Struct() 
        #struct_client.ParseFromString(response.message) #serialize to struct
        msgjson = MessageToJson(response_data.message)
        msgdict = json.loads(msgjson)
        dfmsg_client = pd.DataFrame(msgdict['data'], map(int, msgdict['index']),
                    msgdict['columns'])

        print(dfmsg_client)

        print("Choose one of the options: \n \
            1. Data information \n \
                2. Data output \n \
                    3. Find maximum in the column \n \
                        4. Choose dataset")

        n_option = stub.test(test_pb2.TestRequest(option = int(input("Inter the number of option: "))))

        if n_option == 1:
            response_info = stub.df_info(test_pb2.TestRequest())
            return response_info.message

        elif n_option == 2: 
            response_nrows = stub.n_rows(test_pb2.TestRequest
                (nrows=int(input("Inter quantity of rows: "))))
            return response_nrows.message

        elif n_option == 3:
            print(msgdict['columns'])
            response_max = stub.max_by_col(test_pb2.TestRequest
                (column_name = input("Name of column: ")))
            return response_max.message


        # print(dfmsg_client)


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