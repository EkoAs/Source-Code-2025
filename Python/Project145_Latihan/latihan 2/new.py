

class TYPES:
    def __init__(self=None):
        pass
 
    def list_User(self=None): # kalo ada yg duplikat gakan di panggil 2 kali
        list_user = [40,55,60,70,80,90,55]
        # print(f"List User: {list_user[0]}")
        # print(f"List User: {list_user[1:4]}")
        # print(f"List User: {list_user[-1]}")
        # print(f"List User: {list_user}")
        
        def add_user(list_user):
            print(f"List User Awal: {list_user}")
            list_user.insert(2,50)
            print(f"List User setelah di tambah: {list_user}")
            del list_user[2]
            print(f"List User setelah dihapus: {list_user}")
        
        
    listLat = [1,2,3,4,5,6,7,8,9,10]
    def call(listLat):
        for item in listLat:
            print(f"User: {item} ", end="")     
            if ((item % 2) == 0):
                print(f" => 0")    
        
    
                
    call(listLat)
        
    
    def tuple_User(self=None):
        pass
    
    
if __name__=="__main__":
    TYPES.list_User(self=None)