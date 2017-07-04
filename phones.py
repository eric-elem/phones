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
        # protected property declared with a single leading underscore 
        # as _battery_rating
        self._battery_rating=battery_rating
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
""" SmartPhone class inherits from MobilePhone class
"""
class SmartPhone(MobilePhone):
    # Class property internet_conn has the same value for all instances
    # of the class and is accessed by Class.property like 
    # SmartPhone.internet_conn
    internet_conn=True
    def __init__(self,data_rate,camera_spec,screen_sensor_type
                    ,generation,num_of_sim_slots,
                     manufucturer,width,height,color,serial,battery_rating):
        """ Extra properties in addition to those inheritated from
            the parent/super class like width, height and generation
        """
        self.data_rate=data_rate
        self.camera_spec=camera_spec
        self.screen_sensor_type=screen_sensor_type
        self.generation=generation
        self.num_of_sim_slots=num_of_sim_slots
        self.manufucturer=manufucturer
        self.width=width
        self.height=height
        self.color=color
        self.__serial=serial
        self.battery_rating=battery_rating
    # Polymorphism, a modified definition of the dial method
    def dial(self,number,call_type):
        if call_type=='voice':
            print 'Voice call to '+number
        elif call_type=='video':
            print 'Video call to '+number
        elif call_type=='data':
            print 'Browsing'   
    
    def send_multimedia_msg(multimedia_msg,number):
        print 'Sending '+multimedia_msg+' to '+number

    def take_pictures():
        print 'Taking Pictures'
""" Creating objects of the above classes and accessing some methods
"""
desk_phone=Phone('Motorolla',20,25,'blue','6748332991',500)
desk_phone.dial('+256707677855')
print desk_phone.color

# Mobile_phone object is of both type MobilePhone and Phone
# This is polymorphism as the same object has more than one type
mobile_phone=MobilePhone('2G',1,manufucturer,width,height,color,
                            serial,battery_rating)
