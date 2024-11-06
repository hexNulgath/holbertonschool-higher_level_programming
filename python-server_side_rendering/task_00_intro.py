def generate_invitations(template, attendees):
    # Validate input types
    if not isinstance(template, str) or not isinstance(attendees, list):
        raise TypeError("invalid input")

    # Check if template and attendees are provided
    if not template:
        raise ValueError("Template is empty, no output files generated.")
        return
    if not attendees:
        raise ValueError("No data provided, no output files generated.")
        return
    
    # Generate invitations for each attendee
    for index, attendee in enumerate(attendees, start=1):
        # Format personalized message
        personalized_message = template.format(
            name=attendee.get("name", "N/A"),
            event_title=attendee.get("event_title", "N/A"),
            event_date=attendee.get("event_date", "N/A"),
            event_location=attendee.get("event_location", "N/A")
        )

        # Create a file for each attendee
        file_name = f"output_{index}.txt"
        with open(file_name, 'w') as file:
            file.write(personalized_message)
