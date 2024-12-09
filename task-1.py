from datetime import datetime

def get_days_from_today(date):
    try:
        # Сonvert the date string in the format 'YYYY-MM-DD' into a datetime object
        date_obj = datetime.strptime(date, "%Y-%m-%d")
        # Get the current date
        current_date = datetime.today()
        # Calculate the difference between the current date and the specified date
        difference = current_date - date_obj
        # Return the difference in days as an integer
        return difference.days
    except ValueError:
        return "Invalid date format. Enter date in 'YYYY-MM-DD' format."

print(get_days_from_today("2021-10-09"))
