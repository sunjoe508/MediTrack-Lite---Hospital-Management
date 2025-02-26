try:
    import tkinter as tk
    from tkinter import messagebox
except ModuleNotFoundError:
    print("Error: Tkinter module is not installed or not supported in this environment.")
    raise SystemExit(1)

class HospitalApp:
    def __init__(self, root):
        self.root = root
        self.root.title("MediTrack Lite - Hospital Management")
        self.root.geometry("600x500")
        
        self.patients = []
        self.doctors = []
        self.appointments = []
        self.medicines = {}

        self.create_ui()

    def create_ui(self):
        tk.Label(self.root, text="MediTrack Lite", font=("Arial", 20, "bold")).pack(pady=10)
        
        tk.Button(self.root, text="Register Patient", command=self.register_patient, width=20).pack(pady=5)
        tk.Button(self.root, text="Add Doctor", command=self.add_doctor, width=20).pack(pady=5)
        tk.Button(self.root, text="Schedule Appointment", command=self.schedule_appointment, width=20).pack(pady=5)
        tk.Button(self.root, text="Add Medicine", command=self.add_medicine, width=20).pack(pady=5)
        tk.Button(self.root, text="View Records", command=self.view_records, width=20).pack(pady=5)
        tk.Button(self.root, text="Exit", command=self.root.quit, width=20, bg="red", fg="white").pack(pady=5)

    def register_patient(self):
        def save_patient():
            name = entry_name.get()
            age = entry_age.get()
            condition = entry_condition.get()
            if name and age and condition:
                self.patients.append((name, age, condition))
                messagebox.showinfo("Success", f"Patient {name} registered successfully!")
                add_window.destroy()
            else:
                messagebox.showwarning("Input Error", "All fields are required!")
        
        add_window = tk.Toplevel(self.root)
        add_window.title("Register Patient")
        tk.Label(add_window, text="Name:").pack()
        entry_name = tk.Entry(add_window)
        entry_name.pack()
        tk.Label(add_window, text="Age:").pack()
        entry_age = tk.Entry(add_window)
        entry_age.pack()
        tk.Label(add_window, text="Condition:").pack()
        entry_condition = tk.Entry(add_window)
        entry_condition.pack()
        tk.Button(add_window, text="Save", command=save_patient).pack()
    
    def add_doctor(self):
        def save_doctor():
            name = entry_name.get()
            specialty = entry_specialty.get()
            if name and specialty:
                self.doctors.append((name, specialty))
                messagebox.showinfo("Success", f"Doctor {name} ({specialty}) added successfully!")
                add_window.destroy()
            else:
                messagebox.showwarning("Input Error", "All fields are required!")
        
        add_window = tk.Toplevel(self.root)
        add_window.title("Add Doctor")
        tk.Label(add_window, text="Name:").pack()
        entry_name = tk.Entry(add_window)
        entry_name.pack()
        tk.Label(add_window, text="Specialty:").pack()
        entry_specialty = tk.Entry(add_window)
        entry_specialty.pack()
        tk.Button(add_window, text="Save", command=save_doctor).pack()
    
    def schedule_appointment(self):
        messagebox.showinfo("Info", "Appointment Scheduling is under development.")
    
    def add_medicine(self):
        messagebox.showinfo("Info", "Medicine Inventory Management is under development.")
    
    def view_records(self):
        records_window = tk.Toplevel(self.root)
        records_window.title("Hospital Records")
        tk.Label(records_window, text="Patients Registered:").pack()
        for patient in self.patients:
            tk.Label(records_window, text=f"{patient[0]} - {patient[1]} years - {patient[2]}").pack()
        tk.Label(records_window, text="\nDoctors Available:").pack()
        for doctor in self.doctors:
            tk.Label(records_window, text=f"Dr. {doctor[0]} ({doctor[1]})").pack()

if __name__ == "__main__":
    try:
        root = tk.Tk()
        app = HospitalApp(root)
        root.mainloop()
    except Exception as e:
        print(f"An error occurred: {e}")
