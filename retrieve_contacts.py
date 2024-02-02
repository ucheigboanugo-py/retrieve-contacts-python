import mysql.connector

def retrieve_contacts():
    # Database connection configuration
    db_config = {
        'host': 'localhost',
        'user': 'Nextier',
        'password': 'Farmgate45',
        'database': 'glory_plus_database'
    }

    # Connect to the database
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Query to retrieve contact information from the 'contacts' table
        query = "SELECT FullName, PhoneNumber, Email FROM contacts"

        # Execute the query
        cursor.execute(query)

        # Fetch all rows of the result set
        contacts = cursor.fetchall()

        return contacts

    except mysql.connector.Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None

    finally:
        # Close the cursor and database connection
        if 'cursor' in locals() and cursor:
            cursor.close()
        if 'conn' in locals() and conn:
            conn.close()

def main():
    contacts = retrieve_contacts()

    if contacts:
        print("Retrieved contacts:")
        for contact in contacts:
            print(contact)
    else:
        print("Failed to retrieve contacts.")

if __name__ == "__main__":
    main()
