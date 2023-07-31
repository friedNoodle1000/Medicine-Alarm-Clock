#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import time
import datetime




def get_medicine_input():
    medicines = []
    print("Enter 'done' when you finish entering medicines.")
    print()
    while True:
        medicine_name = input("Enter medicine name >>> ").strip()
        if medicine_name.lower() == 'done':
            break
        dosage = input("Enter dosage for the medicine >>> ")
        time_input = input("Enter time to take the medicine (Ex: '10:OO AM') >>> ").strip()
        time_obj = datetime.datetime.strptime(time_input, "%I:%M %p").time()
        medicines.append((medicine_name, time_obj, dosage))
        print()

    return medicines

def set_alarm(medicine_name, alarm_time, dosage):
    while True:
        current_time = datetime.datetime.now().time()
        current_datetime = datetime.datetime.now()
        alarm_datetime = datetime.datetime.combine(current_datetime.date(), alarm_time)

        if alarm_time < current_time:
            alarm_datetime += datetime.timedelta(days=1)

        time_difference = (alarm_datetime - current_datetime).seconds
        print()
        print(f"Alarm set for {medicine_name} at {alarm_time.strftime('%I:%M %p')}. Dosage: {dosage}")
        time.sleep(time_difference)
        print(f"It's time to take {dosage} of {medicine_name}!")

        break

def main():
    print("Welcome to the Medicine Alarm Clock!")
    medicines = get_medicine_input()
    while True:
        current_datetime = datetime.datetime.now()
        sorted_medicines = sorted(medicines, key=lambda x: (datetime.datetime.combine(current_datetime.date(), x[1]) - current_datetime).seconds)
        for medicine_name, alarm_time, dosage in sorted_medicines:
            set_alarm(medicine_name, alarm_time, dosage)
        midnight = current_datetime.replace(hour=23, minute=59, second=59, microsecond=999999)
        time_difference = (midnight - current_datetime).seconds
        time.sleep(time_difference)
if __name__ == "__main__":
    main()

