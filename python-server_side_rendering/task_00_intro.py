
def generate_invitations(template, attendees):
    if not isinstance(template, str) and not isinstance(attendees, list[dict]):
        raise TypeError("invalid input")
        return
    if not template or template == "":
        raise ValueError("Template is empty, no output files generated.")
    if not attendees or attendees == "":
        raise ValueError("No data provided, no output files generated.")
    
    f = open(template, "w")

    for index, attendee in enumerate(attendees, start=1):
        personalized_message = template.format(
        name=attendee.get("name", "N/A"),
        event_title=attendee.get("event_title", "N/A"),
        event_date=attendee.get("event_date", "N/A"),
        event_location=attendee.get("event_location", "N/A")
        )
    file_name = f"output_{index}.txt"
    with open(file_name, 'w') as file:
        file.write(personalized_message)
