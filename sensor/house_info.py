import date
from datetime import date


class HouseInfo(self,data):
    def get_data_by_area(self,field,rec_area):
        rec_area = 0
        field_data = []
        for record in self.data:
            if rec_area == 0:
                record[field] = field_data.append
            else:
                rec_area = int(record['area'])
        return field_data
    
    def get_data_by_date(self,field,rec_date):
        field_data = []
        for record in self.data:
            if date == rec_date:
                record[field] = field_data.append
        return field_data

    





