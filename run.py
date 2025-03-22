from app import create_app
import os
from waitress import serve
from rich.console import Console
from rich import print as rprint
from rich.progress import track, Progress, TextColumn, SpinnerColumn
import threading
import signal
import sys
import time
import itertools

console = Console()

app = create_app()

def signal_handler(sig, frame):
    """Handle Ctrl+C to show a clean exit message"""
    console.line()
    rprint("\n[bold red]Server shutdown requested. Stopping BookWorm...[/bold red]")
    sys.exit(0)

def animate_progress():
    """Show an animated progress bar while the server is running"""
    with Progress(
        SpinnerColumn(),
        TextColumn("[bold green]BookWorm server is running...[/bold green]"),
        console=console,
        transient=False,
    ) as progress:
        task = progress.add_task("", total=None)
        while True:
            progress.update(task)
            time.sleep(0.1)

if __name__ == '__main__':
    # Register signal handler for Ctrl+C
    signal.signal(signal.SIGINT, signal_handler)
    
    host = os.getenv('FLASK_RUN_HOST', '0.0.0.0')
    port = int(os.getenv('FLASK_RUN_PORT', 8080))
    
    # Display server startup information
    console.rule("[bold green]BookWorm Server Starting[/bold green]")
    rprint(f"[green]🚀 Server starting at:[/green] [bold cyan]http://{host}:{port}[/bold cyan]")
    rprint("[yellow]👉 Press [bold red]CTRL+C[/bold red] to stop the server[yellow]")
    console.rule()
    
    # Start the progress animation in a separate thread
    progress_thread = threading.Thread(target=animate_progress, daemon=True)
    progress_thread.start()
    
    # Start the Flask application using Waitress
    serve(app, host=host, port=port)