from collections.abc import Mapping

class ImmutableMap(Mapping):
    def __init__(self,data):
        self.data = dict(data)

    def __getitem__(self,key):
        return self.data[key]
    
    def __len__(self):
        return len(self.data)
    
    def __iter__(self):
        return iter(self.data)
    
    def __contains__(self, key):
        return key in self.data
    
    # Additional Methods (Optional):   
    def keys(self):
        return self.data.keys()

    def values(self):
        return self.data.values()

    def items(self):
        return self.data.items()
    

    # Immutable Design:
    def __setitem__(self, key, value):
        raise TypeError("This is a ImmutableMap and you can't assign item")

    def __delitem__(self,key):
        raise TypeError("This is a ImmutableMap and you can't delete item")


# Testing:
if __name__ == '__main__':
    di = {'a': 1, 'b': 2, 'c': 3}
    immutable_map = ImmutableMap(di)

    print(immutable_map.__len__())
    
    for key in immutable_map.__iter__():
        print(key, end = ' ')

    print()
    
    print(immutable_map.keys())
    print(immutable_map.values())
    print(immutable_map.items()) 
    print('b' in immutable_map)
    print('f' in immutable_map)
        
    #immutable_map.__setitem__('d', 4)
    #immutable_map.__delitem__('c')