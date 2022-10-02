def success_response(message: str, data: dict|list):
    return {
        'success': True,
        'message': message,
        'data': data,
    }