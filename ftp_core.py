from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

def ftp_core(user, password, path, port):
    # 实例化虚拟用户，这是用于验证用户登录信息的类
    authorizer = DummyAuthorizer()
    # 添加用户权限和路径：用户名，密码，路径，具有读写权限
    authorizer.add_user(user, password, path, perm='elradfmwMT')
    # 初始化FTP处理器
    handler = FTPHandler
    handler.authorizer = authorizer
    # 监听IP和端口
    server = FTPServer(('0.0.0.0', port), handler)
    # 开始服务
    server.serve_forever()

if __name__ == '__main__':
    ftp_core('user', '123123', 'C:\\', 21)