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
# child class MobilePhone inherits from parent class Phone
class MobilePhone(Phone):
    def __init__(self,generation,num_of_sim_slots,
                    manufucturer,width,height,color,serial,battery_rating):
        """ Extra properties in addition to those inheritated from
            the parent class like width and height
        """
        self.generation=generation
        self.num_of_sim_slots=num_of_sim_slots
        self.manufucturer=manufucturer
        self.width=width
        self.height=height
        self.color=color
        self.__serial=serial
        self.battery_rating=battery_rating
    """ Extra methods in addition to those inheritated from
            the parent class like dial and sendText
    """
    def get_generation(self):
        return self.generation
    def get_num_of_sim_slots(self):
        return self.num_of_sim_slots
