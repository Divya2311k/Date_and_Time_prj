from scheduler import Scheduler
from utils import format_timedelta
from notifier import notify
from rich.console import Console
from rich.table import Table
import time

console = Console()
scheduler = Scheduler()

def display_events():
    events = scheduler.get_upcoming_events()
    table = Table(title="Upcoming Events")
    table.add_column("Event", style="cyan")
    table.add_column("Date & Time", style="green")
    table.add_column("Countdown", style="magenta")

    for e in events:
        countdown = format_timedelta(e.time_remaining())
        table.add_row(e.name, e.date_time.strftime("%Y-%m-%d %H:%M"), countdown)

    console.print(table)

def main_menu():
    while True:
        console.print("\n[bold yellow]Countdown & Scheduler App[/bold yellow]")
        console.print("1. Add Event\n2. View Events\n3. Start Notification Loop\n4. Exit")

        choice = input("Choose an option: ")
        if choice == "1":
            name = input("Event name: ")
            dt = input("Date & Time (YYYY-MM-DD HH:MM): ")
            try:
                scheduler.add_event(name, dt)
                console.print("[green]Event added successfully![/green]")
            except Exception as e:
                console.print(f"[red]Error: {e}[/red]")
        elif choice == "2":
            display_events()
        elif choice == "3":
            start_notifier_loop()
        elif choice == "4":
            break
        else:
            console.print("[red]Invalid option.[/red]")

def start_notifier_loop():
    console.print("[blue]Notifier started. Press Ctrl+C to stop.[/blue]")
    try:
        while True:
            for event in scheduler.get_upcoming_events():
                remaining = event.time_remaining()
                if 0 < remaining.total_seconds() <= 60:
                    notify("Event Reminder", f"{event.name} starts soon!")
            time.sleep(30)
    except KeyboardInterrupt:
        console.print("[red]Notifier stopped.[/red]")

if __name__ == "__main__":
    main_menu()
