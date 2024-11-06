import os
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def generate_invitations(template, attendees):
    # Validate input types
    if not isinstance(template, str) or not isinstance(attendees, list):
        logging.error("Invalid input. Template should be a string and attendees should be a list of dictionaries.")
        return  # Log the error and stop execution

    # Check if template and attendees are provided
    if not template:
        logging.error("Template is empty, no output files generated.")
        return
    if not attendees:
        logging.error("No data provided, no output files generated.")
        return

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
                logging.warning(f"File {file_name} already exists, skipping...")
                continue  # Skip writing if file already exists

            # Write the personalized message to the file
            with open(file_name, 'w') as file:
                file.write(personalized_message)
            logging.info(f"Invitation written to {file_name}")
        
        except OSError as e:
            # Log the error if writing the file fails (e.g., permission issues)
            logging.error(f"Error writing to {file_name}: {e}")
