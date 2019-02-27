from flask import jsonify, make_response
import psutil
import socket

from flask import Flask

app = Flask(__name__)
hostname = socket.gethostname()

def get_memory():
    memory_bt = psutil.virtual_memory()[3]
    memory_kbt = memory_bt / 1024
    memory_mbt = memory_kbt / 1024
    memory_gbt = memory_mbt / 1024
    return  int(memory_mbt)


def get_cpu():
    return psutil.cpu_percent()


@app.route('/resources/memory', methods=['GET'])
def get_mem():
    return jsonify({'memory': get_memory(),
                    'description':'Memory usage, MB'})

@app.route('/resources/cpu', methods=['GET'])
def get_cpu_usage():
    return jsonify({'cpu': get_cpu(),
                    'description':'CPU usage, %'})

@app.route('/resources/cpu_mem', methods=['GET'])
def get_cpu_mem_usage():
    return jsonify({'cpu': get_cpu(),
                    'memory': get_memory(),
                    'hostname': hostname})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='1234', debug=True)
