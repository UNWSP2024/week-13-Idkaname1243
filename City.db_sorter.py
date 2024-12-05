import sqlite3


def main():
    conn = sqlite3.connect('cities.db')
    cur = conn.cursor()
    setup_database(cur)
    while True:
        print("\nChoose an operation:")
        print("1. Display a list of cities sorted by population (ascending).")
        print("2. Display a list of cities sorted by population (descending).")
        print("3. Display a list of cities sorted by name.")
        print("4. Display the total population of all cities.")
        print("5. Display the average population of all cities.")
        print("6. Display the city with the highest population.")
        print("7. Display the city with the lowest population.")
        print("8. Exit.")
        choice = input("Enter your choice: ")
        if choice == '1':
            display_sorted_cities(cur, 'Population ASC')
        elif choice == '2':
            display_sorted_cities(cur, 'Population DESC')
        elif choice == '3':
            display_sorted_cities(cur, 'CityName ASC')
        elif choice == '4':
            display_total_population(cur)
        elif choice == '5':
            display_average_population(cur)
        elif choice == '6':
            display_highest_population_city(cur)
        elif choice == '7':
            display_lowest_population_city(cur)
        elif choice == '8':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
    conn.close()
def setup_database(cur):
    cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Cities'")
    if not cur.fetchone():
        print("Setting up database...")
        add_cities_table(cur)
        add_cities(cur)
def display_sorted_cities(cur, order_by):
    query = f"SELECT CityName, Population FROM Cities ORDER BY {order_by}"
    cur.execute(query)
    results = cur.fetchall()
    for city, population in results:
        print(f"{city:<20}{population:,.0f}")
def display_total_population(cur):
    cur.execute("SELECT SUM(Population) FROM Cities")
    total_population = cur.fetchone()[0]
    print(f"Total population of all cities: {total_population:,.0f}")
def display_average_population(cur):
    cur.execute("SELECT AVG(Population) FROM Cities")
    avg_population = cur.fetchone()[0]
    print(f"Average population of all cities: {avg_population:,.0f}")
def display_highest_population_city(cur):
    cur.execute("SELECT CityName, Population FROM Cities ORDER BY Population DESC LIMIT 1")
    city, population = cur.fetchone()
    print(f"City with the highest population: {city} ({population:,.0f})")
def display_lowest_population_city(cur):
    cur.execute("SELECT CityName, Population FROM Cities ORDER BY Population ASC LIMIT 1")
    city, population = cur.fetchone()
    print(f"City with the lowest population: {city} ({population:,.0f})")
if __name__ == '__main__':
    main()
