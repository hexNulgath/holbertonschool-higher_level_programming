import os

def generate_invitations(template, attendees):
    # Validate input types
    if not isinstance(template, str) or not isinstance(attendees, list):
        raise TypeError("Invalid input. Template should be a string and attendees should be a list of dictionaries.")

    # Check if template and attendees are provided
    if not template:
        raise ValueError("Template is empty, no output files generated.")
    if not attendees:
        raise ValueError("No data provided, no output files generated.")

    # Generate invitations for each attendee
    for index, attendee in enumerate(attendees, start=1):
        # Replace placeholders with actual values
        personalized_message = template.replace("{name}", attendee.get("name", "N/A")) \
                                       .replace("{event_title}", attendee.get("event_title", "N/A")) \
                                       .replace("{event_date}", attendee.get("event_date", "N/A")) \
                                       .replace("{event_location}", attendee.get("event_location", "N/A"))

        # Create the file name for each attendee
        file_name = f"output_{index}.txt"

        try:
            # Check if the file already exists
            if os.path.exists(file_name):
                print(f"File {file_name} already exists, skipping...")
                continue  # Skip writing if file already exists

            # Write the personalized message to the file
            with open(file_name, 'w') as file:
                file.write(personalized_message)
            print(f"Invitation written to {file_name}")
        
        except OSError as e:
            # Handle potential file errors (e.g., permissions issues)
            print(f"Error writing to {file_name}: {e}")
