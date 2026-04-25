import os

def generate_invitations(template, attendees):
    # 1. Giriş tiplərinin yoxlanılması
    if not isinstance(template, str):
        print(f"Error: Template must be a string. Got {type(template).__name__}")
        return
    
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print(f"Error: Attendees must be a list of dictionaries. Got {type(attendees).__name__}")
        return

    # 2. Boş girişlərin yoxlanılması
    if not template.strip():
        print("Template is empty, no output files generated.")
        return
    
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # 3. Hər bir iştirakçı üçün emal (Process)
    for i, attendee in enumerate(attendees, start=1):
        personalized_template = template
        
        # Əvəz olunacaq placeholder-lərin siyahısı
        placeholders = ["name", "event_title", "event_date", "event_location"]
        
        for key in placeholders:
            # Əgər data yoxdursa və ya None-dırsa "N/A" ilə əvəz et
            value = attendee.get(key)
            if value is None:
                value = "N/A"
            
            # String daxilində {key} hissəsini tap və dəyiş
            personalized_template = personalized_template.replace(f"{{{key}}}", str(value))
        
        # 4. Fayla yazmaq
        filename = f"output_{i}.txt"
        
        try:
            with open(filename, 'w') as file:
                file.write(personalized_template)
            # print(f"File {filename} created successfully.") # Test üçün istifadə edilə bilər
        except Exception as e:
            print(f"An error occurred while writing to {filename}: {e}")

# Test mühiti (Verilən nümunə data ilə)
if __name__ == "__main__":
    # Nümunə template yaradaq (əgər fayl yoxdursa)
    sample_template = """Hello {name},

You are invited to the {event_title} on {event_date} at {event_location}.

We look forward to your presence.

Best regards,
Event Team"""

    attendees_list = [
        {"name": "Alice", "event_title": "Python Conference", "event_date": "2023-07-15", "event_location": "New York"},
        {"name": "Bob", "event_title": "Data Science Workshop", "event_date": "2023-08-20", "event_location": "San Francisco"},
        {"name": "Charlie", "event_title": "AI Summit", "event_date": None, "event_location": "Boston"}
    ]

    generate_invitations(sample_template, attendees_list)
