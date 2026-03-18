from datetime import datetime

class Patient:
    def __init__(self, name):
        self.name = name
        self.time_added = datetime.now()

    def get_details(self):
        return f"{self.name} (Added at {self.time_added.strftime('%H:%M:%S')})"


class ClinicQueue:
    def __init__(self):
        self.queue = []
        self.total_served = 0

    def add_patient(self, patient):
        self.queue.append(patient)   # FIFO

    def serve_patient(self):
        if self.queue:
            served = self.queue.pop(0)  # remove first
            self.total_served += 1
            return served
        return None

    def get_all_patients(self):
        return self.queue