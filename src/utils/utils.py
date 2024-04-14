# class or functions
class Util(object):
    def common_headers_json(self):
        headers = {
            "Content-Type": "application/json"
        }
        return headers
    def common_headers_xml(self):
        headers = {
            "Content-Type" : "application/xml"
        }
        return headers
    def common_headers_put_patch_delete_basic_auth(self,basic_auth_value):
        headers = {
            "Content-Type" : "application/json",
            "Authorization" : "Basic"+str(basic_auth_value)
        }
        return headers

    def common_headers_put_patch_delete_cookie(self,token):
        headers = {
            "Content-Type" : "application/json",
            "Cookie" : "token="+str(token)
        }
        return headers
    def read_csv_file(self):
        pass
    def read_env_file(self):
        pass
    def read_database_file(self):
        pass
# util =  Util().common_headers