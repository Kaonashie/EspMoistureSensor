from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/sensor', methods=['POST'])
def sensor_data():
    data = request.get_json()
    print("Received sensor data:", data)
    return jsonify({"status": "ok"}), 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)


# import socket

# HOST = "0.0.0.0"  # Accept connections from any IP
# PORT = 5000

# server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server_socket.bind((HOST, PORT))
# server_socket.listen(5)

# print(f"Listening on {HOST}:{PORT}...")

# while True:
#     client_socket, client_addr = server_socket.accept()
#     print(f"Connection from {client_addr}")

#     data = client_socket.recv(1024)
#     print(f"Received: {data.decode()}")

#     client_socket.send(b"ACK")
#     client_socket.close()