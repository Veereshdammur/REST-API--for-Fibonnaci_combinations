# import datetime
# from flask import Flask, request
# from flask_restful import Resource, Api, abort
# from fibonacci import fibonacci_combinations, MAX_FIBONACCI_VALUE

import datetime
from flask import Flask, request
from flask_restful import Resource, Api, abort
from source.fibonacci import fibonacci_combinations, MAX_FIBONACCI_VALUE




app = Flask(__name__)
api = Api(app)


def abort_if_parameter_exceeds_max_value(id):
    """
    The following method verify the input parameters passed as argument and
    returns the appropriate message
    """
    try:
        val = int(id)
    except:
        abort(500, message="The requested value is: {} please note that only "
                           "positive integers (greater than 3) are valid "
                           "fibonacci's "
                           "domain values ".format(id))
    if val < 4:
        abort(500, message="The value requested is {} but only positive "
                           "integers (greater than 3) are valid fibonacci's "
                           "domain values "
                           "".format(id))
    if val > MAX_FIBONACCI_VALUE:
        abort(500, message="The value of {} is exceeding the max value "
                           "allowed of {} ".format(id, MAX_FIBONACCI_VALUE))


class Heartbeat(Resource):
    """
    This class is responsible for the health status of the API. Here,
    it is assumed that FLASK API is not available to accept requests
    between 12 AM to 3 AM (everyday). Except this time window, users are
    allowed to make the requests.
    """

    def get(self):
        current_hour = datetime.datetime.now().hour
        if current_hour > 2:
            return {'health_status ': " Feel free to make the API requests to "
                                      "find the Fibonacci combinations"}
        return {'health_status': "API service is down and under maintenance. "
                                 "Please wait until 3 AM to make API request"}


class Fibonacci(Resource):
    def get(self, num):
        abort_if_parameter_exceeds_max_value(num)
        current_hour = datetime.datetime.now().hour
        if current_hour < 3:
            return {'result': "API is under maintenance window. Please wait "
                              "until 3 AM to make API request"}, 200
        result = fibonacci_combinations(num)
        return {'result': result}, 200


api.add_resource(Heartbeat, '/health/')
api.add_resource(Fibonacci, '/fib/<string:num>')

if __name__ == "__main__":
    app.run(debug=True, port=5001)  # host='0.0.0.0'