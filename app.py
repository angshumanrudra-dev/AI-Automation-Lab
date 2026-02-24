from rich import print
import requests

print("[bold green]AI Automation Lab Started 🚀[/bold green]")

response = requests.get("https://api.github.com")

if response.status_code == 200:
    print("[bold blue]GitHub API is reachable ✔[/bold blue]")
else:
    print("[bold red]Something went wrong ❌[/bold red]")

print("[yellow]Status Code:[/yellow]", response.status_code)