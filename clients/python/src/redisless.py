from cffi import FFI


class RedisLess(object):
    """
    RedisLess
    """

    def __init__(self):
        ffi = FFI()
        ffi.cdef("""
            typedef void* redisless;
            typedef void* server;
            
            redisless redisless_new();
            server redisless_server_new(redisless);
            void redisless_server_start(server);
            void redisless_server_stop(server);
        """)

        self._C = ffi.dlopen('../../../target/release/libredisless.dylib')
        self._redisless = self._C.redisless_new()
        self._redisless_server = self._C.redisless_server_new(self._redisless)

    def start(self):
        """
        Start local embedded RedisLess instance
        :return:
        """
        self._C.redisless_server_start(self._redisless_server)

    def stop(self):
        """
        Stop local embedded RedisLess instance
        :return:
        """
        self._C.redisless_server_stop(self._redisless_server)