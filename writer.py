from unicodedata import name
import grpc
import item_pb2
import item_pb2
import item_pb2_grpc

"""
Simple implemetation of writer gRPC client that can be used to write messages to gPRC server
"""

print("Sending sample payload")

channel = grpc.insecure_channel("localhost:5005")
stub = item_pb2_grpc.ItemServiceStub(channel)

# Update this with desired payload
item = item_pb2.ItemMessage(
    name="Non-Stick Frying Pan",
    brand_name="Chef Dreams",
    id=4,
    weight=4.5
)

response = stub.Create(item)