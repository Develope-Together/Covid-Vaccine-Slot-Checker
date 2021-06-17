import requests
import time

### DataCollecter Class ###########################################################################
class DataCollecter:
    # __counter = 0
    # __callable = True
    __main_api_location = "https://cdn-api.co-vin.in/api/"
    __header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    
    @staticmethod
    def find_states():
        """
        # this is a method for finding the state names and their
          including districts name and id's from the cowin public api.
        
        # returns state_dic a dictionary 
          where key is the state name and the value is another dictionary
          which containt all districts name and theirs id of thate state.
        """
        # this is a dictionary in which all states name 
        # and including districts details will be stored 
        state_dic = {}

        # the url of the api for fetching the states name and id 
        url = DataCollecter.__main_api_location + "v2/admin/location/states"
        
        # request for date and capturing the response
        response = requests.get(url, headers=DataCollecter.__header).json()
        
        # from the response selecting the state name and including districts details
        for state in response['states']:
            state_dic[state['state_name']] = DataCollecter.find_districts(state['state_id'])

        # return the dictionary
        return state_dic
    
        
    @staticmethod
    def find_districts(state_id):
        """
        # this is a method for finding the district names and id's of a
          specific state from the cowin public api.
          
        # 'state_id' variable refers to the state.
        
        # returns the district_dic a dictionary 
          where keys are district name and values are that districts id.
        """
        # this is a dictionary in which all districts name and id will be stored 
        district_dic = {}
        
        # the url of the api for fetching the districts name and id 
        url = DataCollecter.__main_api_location + "v2/admin/location/districts/" + str(state_id)
         
        # request for date and capturing the response
        response = requests.get(url, headers=DataCollecter.__header).json()
        
        # from the response selecting the districts name and id
        for district in response['districts']:
            district_dic[district['district_name']] = district['district_id']
        
        # return the dictionary
        return district_dic
    
    @staticmethod
    def slot7_by_districts(district_id,date):
        """
        # this is a method to find the slots of given district and date.
        
        # district_id: is needed for the url params which determine the district.
          date: is also used for url params, it's help to get details of center's sessions
          		upto 7 days from the given date.
        
        # this returns the center details of provided district and the date
        """      
        # payload for the url
        payload = {'district_id':str(district_id),
                   'date':str(date)}

        # the url of the api for fetching the center details
        url = DataCollecter.__main_api_location + "v2/appointment/sessions/public/findByDistrict"
        
        # request for date and capturing the response
        response = requests.get(url=url,
                                headers=DataCollecter.__header,
                                params=payload).json()
        
        return response		
        

### Runs from here ###########################################################################
if __name__ == "__main__":
    r = DataCollecter().find_states()
    print(r)