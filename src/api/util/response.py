from flask import jsonify


class Response:

    def ok(result, status=None):
        errors = None
        data = result
        status = 200 if status is None else status
        return jsonify({'status': 'success', 'data': data, 'errors': errors}), status

    def bad_request(errors, data=None):
        return jsonify({'status': 'error', 'data': data, 'errors': errors}), 400

    def not_found():
        return '', 404

    def no_content():
        return '', 204
