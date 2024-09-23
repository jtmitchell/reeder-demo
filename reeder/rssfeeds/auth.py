from ninja.security import APIKeyCookie, APIKeyHeader


class ApiHeaderKey(APIKeyHeader):
    param_name = "X-API-Key"

    def authenticate(self, request, key):
        if key == "1234":
            return key


class ApiCookieKey(APIKeyCookie):
    def authenticate(self, request, key):
        if key == "1234":
            return key
