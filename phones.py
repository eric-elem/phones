class Phone:
    def __init__(self,manufucturer,width,height,color,serial,battery_rating):
        self.manufucturer=manufucturer
        self.width=width
        self.height=height
        self.color=color
        """ Private property __serial only directly accessible within
            the class. Can be accessed externally using name mangling as
            phone._Phone__serial. This and example of encapsulation 
            in python.
        """
        self.__serial=serial
        self.battery_rating=battery_rating
        """ Private method __update_software can only be called
            from within the class and not directly from an object but
            indirectly through name mangling such as 
            phone._Phone__update_software()
        """
        self.__update_software()

    def dial(self,number):
        print 'Dialing '+number
    def send_text(self,number):
        print 'Texting '+number
    def receive_call(self):
        print 'Ringing'
    # Private method defined using __ before method name
    def __update_software(self):
        print 'Updating software'
