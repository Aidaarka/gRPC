from concurrent import futures
import grpc
import test_pb2
import test_pb2_grpc
import time
import threading
from pyspark.sql.session import SparkSession
import pandas as pd
import json
import logging
from google.protobuf.message import Message 
#from google.protobuf import any
from google.protobuf import any_pb2
from google.protobuf import json_format
from google.protobuf.json_format import ParseDict
from google.protobuf import struct_pb2

class Listener(test_pb2_grpc.TestServiceServicer):
    
    # Start spark session
    spark = SparkSession.builder\
        .master("local[*]")\
        .appName('Test run for big DataFrame')\
        .getOrCreate()

    # Read data
    def data(self, request):
        path = f"/home/aidar/Desktop/SAS/{request.filename}.csv"
        dfspark = self.spark.read.csv(path, header = True)
        return dfspark

    # Upload data, transform to Struct type, send to Server
    def test(self, request, context):
        dfspark = self.data(request)
        dfpandas = dfspark.limit(request.nrows).toPandas()
        dfdict = dfpandas.to_dict(orient='split')
        dfstruct_server = ParseDict(dfdict, struct_pb2.Struct()) 
        
        # bstruct = dfstruct_server.SerializeToString() # serialization to byte
        
        return test_pb2.TestReply(message = dfstruct_server)
        

#def n_rows(): ...

#def max_by_col(): ...

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    test_pb2_grpc.add_TestServiceServicer_to_server(Listener(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()
    

if __name__ == "__main__":
    logging.basicConfig()
    serve()



        # datapd = pd.read_csv(f"/home/aidar/Desktop/SAS/{request.filename}.csv")
        # datacut = datapd.head(request.name)
        # datamid = datacut.to_json(orient = 'records')
        # parsed = json.loads(json_format.MessageToJson(datamid))
        # datajson = json.dumps(parsed)
        # some_any = any_pb2.Any()

        # fd = some_any.Pack(df2)
        # serialized = some_any.SerializeToString(deterministic=True)

        #any_message.Pack(message)
        #datajson = json.dumps(parsed)


    """
    def __init__(self, *args, **kwargs):
        self.counter = 0
        self.lastPrintTime = time.time()

    def test(self, request, context):
        self.counter += 1
        if(self.counter > 10000):
            print("10000 calls in %3f seconds" % (time.time() - self.lastPrintTime))
            self.lastPrintTime = time.time()
            self.counter = 0
        return test_pb2.Test2(count = request.count + 1)"""


"""try:
        while True:
            print("server on: threads %i" % (threading.active_count()))
            time.sleep(1)
    except KeyboardInterrupt:
        print("KeyboardInterrupt")
        server.stop(0)"""


"""   dataPath = "/home/aidar/Desktop/SAS/data.csv"

    def test(self, request, context):
        
        file = open(self.dataPath, 'r')
        dataFrame = file.read()
        testdata = dataFrame.split("\n")
        
        for i in testdata:
        return test_pb2.TestReply(message = dataFrame)"""