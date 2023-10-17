# common

#
def to_return(code: str = '200', data: dict = {}, message: str = 'success'):
    return {
        "code": code,
        "data": data,
        "message": message
    }