class Patient:
    def _init_(self, name, age, gender, email, phone):
        self.name = name
        self.age = age
        self.gender = gender
        self.email = email
        self.phone = phone
class Appointment:
    def _init_(self, patient, date, time):
        self.patient = patient
        self.date = date
        self.time = time
class AppointmentScheduler:
    def _init_(self):
        self.appointments = []
    def schedule_appointment(self, appointment):
        self.appointments.append(appointment)
    def get_daily_schedule(self, date):
        daily_schedule = [appt for appt in self.appointments if appt.date == date]
        return daily_schedule
if _name=="main_":
     schedul = AppointmentScheduler()
     patient1 = Patient("Aasni", 30, "Female", "aasni13@gmail.com", "764-456-7060")
     patient2 = Patient("Ajai", 25, "Male", "ajai1012@gmail.com", "942-482-8530")
     patient3 = Patient("Sruthi",23,"Female","sruthisri25@gmail.com","422-764-9042")
     appointment1 = Appointment(patient1, "2024-02-21", "10:00 AM")
     appointment2 = Appointment(patient2, "2024-02-21", "11:00 AM")
     appointment3 = Appointment(patient3, "2024-02-22", "09:00 AM")
     schedul.schedule_appointment(appointment1)
     schedul.schedule_appointment(appointment2)
     schedul.schedule_appointment(appointment3)
     schedule_date = "2024-02-22"
     daily_schedule = schedul.get_daily_schedule(schedule_date)
     print(f"Daily Schedule for {schedule_date}:")
     for app in daily_schedule:
         print(f"Patient: {app.patient.name}, Time: {app.time}")
