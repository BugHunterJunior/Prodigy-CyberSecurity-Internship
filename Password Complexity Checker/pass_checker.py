import re
import os
import sys
import getpass
import urllib.request
import gzip
import shutil
import ssl
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, DownloadColumn, TransferSpeedColumn

console = Console()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def ensure_rockyou_exists(txt_path="rockyou.txt", gz_path="rockyou.txt.gz"):
    """
    Ensures rockyou.txt exists. Downloads .gz with a progress bar and extracts it.
    """
    url = "https://github.com/BugHunterJunior/Prodigy-CyberSecurity-Internship/releases/download/PRODIGY_CS_02/rockyou.txt.gz"
    
    if os.path.exists(txt_path):
        return True

    console.print(f"\n[bold yellow][*] {txt_path} not found in the current directory.[/]")
    
    # 1. Download with rich progress bar and SSL bypass
    if not os.path.exists(gz_path):
        # Bypass SSL verification for this download
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE

        try:
            with urllib.request.urlopen(url, context=ctx) as response:
                total_size = int(response.info().get("Content-Length", 0))
                
                with Progress(
                    SpinnerColumn("dots", style="cyan"),
                    TextColumn("[cyan]{task.description}"),
                    BarColumn(complete_style="green", finished_style="bold green"),
                    DownloadColumn(),
                    TransferSpeedColumn(),
                    console=console
                ) as progress:
                    task = progress.add_task("Downloading rockyou.txt.gz...", total=total_size)
                    
                    with open(gz_path, "wb") as f:
                        while chunk := response.read(8192):
                            f.write(chunk)
                            progress.update(task, advance=len(chunk))
                            
            console.print("[bold green][+] Download complete![/]")
        except Exception as e:
            console.print(f"[bold red]ERROR: Failed to download the file. {e}[/]")
            return False

    # 2. Extract
    console.print(f"[cyan][+] Extracting {gz_path}...[/]")
    try:
        with gzip.open(gz_path, 'rb') as f_in:
            with open(txt_path, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
        console.print("[bold green][+] Extraction complete![/]")
        
        # 3. Cleanup
        os.remove(gz_path)
        console.print("[dim][+] Deleted old rockyou.txt.gz file.[/dim]\n")
        return True
    except Exception as e:
        console.print(f"[bold red]ERROR: Failed to extract the file. {e}[/]")
        return False

def check_rockyou(password, filepath="rockyou.txt"):
    abs_path = os.path.abspath(filepath)
    
    if not os.path.exists(abs_path):
        console.print(f"\n[bold yellow]ERROR: File not found at {abs_path}[/]")
        console.print("[dim]If on Kali Linux, check /usr/share/wordlists/rockyou.txt[/]")
        return None

    clean_password = password.rstrip('\r\n')

    with open(abs_path, "r", encoding="latin-1", errors="ignore") as f:
        for line in f:
            if line.rstrip('\r\n') == clean_password:
                return True
    return False

def check_password(password):
    score = 0
    feedback = []

    if len(password) >= 8: score += 1
    else: feedback.append("Use at least 8 characters")

    if len(password) >= 12: score += 1

    if re.search(r"[A-Z]", password): score += 1
    else: feedback.append("Add uppercase letters")

    if re.search(r"[a-z]", password): score += 1
    else: feedback.append("Add lowercase letters")

    if re.search(r"[0-9]", password): score += 1
    else: feedback.append("Add numbers")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password): score += 1
    else: feedback.append("Add special characters")

    return score, feedback

def strength_label(score, is_compromised=False):
    if is_compromised:
        return "[bold white on red] COMPROMISED [/]"
    if score <= 2:
        return "[bold red]🔴 Weak[/]"
    elif score <= 4:
        return "[bold yellow]🟡 Medium[/]"
    else:
        return "[bold green]🟢 Strong[/]"

if __name__ == "__main__":
    clear_screen()
    console.print("\n[bold cyan]=== Password Strength Checker ===[/]\n")
    
    if not ensure_rockyou_exists():
        console.print("[bold red]Critical Error: Cannot proceed without the wordlist.[/]")
        sys.exit(1)
    
    password = ""
    while not password:
        password = getpass.getpass("Enter password: ")

        clear_screen()
        # Create a fresh console to prevent progress bar artifacts
        console = Console()
        console.print("\n[bold cyan]=== Password Strength Checker ===[/]\n")

        if not password:
            console.print("[bold red]Error: Password cannot be blank. Please try again.[/]\n")

    is_compromised = check_rockyou(password)

    if is_compromised is None:
        sys.exit(1) 
        
    if is_compromised:
        clear_screen()
        console.print("[bold red]-🚨 This password is in a known data breach (rockyou.txt). DO NOT USE IT![/]")
        sys.exit(0)

    score, feedback = check_password(password)
    
    console.print(f"Password: {password}\nStrength: {strength_label(score, is_compromised)} [dim](Score: {score}/6)[/]")

    if feedback:
        console.print("[magenta]Feedback:[/]")
        for f in feedback:
            console.print(f"- {f}")
    else:
        console.print("[bold green]\nPerfect password![/]")