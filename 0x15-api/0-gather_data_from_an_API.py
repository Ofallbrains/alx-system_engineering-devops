import sys
import requests

def get_employee_todo_progress(employee_id):
        # URL for the API
            url = f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos'

                # Send GET request to the API
                    response = requests.get(url)

                        # Check if request was successful
                            if response.status_code != 200:
                                        print("Error: Unable to fetch data from the API")
                                                return

                                                # Parse JSON response
                                                    todos = response.json()

                                                        # Filter completed tasks
                                                            completed_tasks = [todo for todo in todos if todo['completed']]

                                                                # Calculate progress
                                                                    total_tasks = len(todos)
                                                                        done_tasks = len(completed_tasks)

                                                                            # Print employee progress
                                                                                print(f"Employee {todos[0]['name']} is done with tasks({done_tasks}/{total_tasks}):")
                                                                                    for task in completed_tasks:
                                                                                                print(f"\t{task['title']}")

                                                                                                if __name__ == "__main__":
                                                                                                        # Check if an employee ID is provided as argument
                                                                                                            if len(sys.argv) != 2:
                                                                                                                        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
                                                                                                                                sys.exit(1)

                                                                                                                                    # Get employee ID from command line argument
                                                                                                                                        employee_id = sys.argv[1]

                                                                                                                                            # Call function to get employee todo progress
                                                                                                                                                get_employee_todo_progress(employee_id)

