import grpc
import order_pb2
import order_pb2_grpc

print("Sending sample order payload")

channel = grpc.insecure_channel("localhost:5005")
stub = order_pb2_grpc.OrderServiceStub(channel)

order = order_pb2.OrderMessage(
    id="2222",
    created_by="USER_XEUS",
    status=order_pb2.OrderMessage.Status.QUEUED,
    created_at='2022-04-14',
    equipment=[order_pb2.OrderMessage.Equipment.KEYBOARD]
)

response = stub.Create(order)