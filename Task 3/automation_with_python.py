import os
import shutil
import re
import requests
from datetime import datetime

def log_event(action, details):
    """Logs automation actions with a timestamp to a log file."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] {action}: {details}\n"
    with open("automation_history.log", "a", encoding="utf-8") as log_file:
        log_file.write(log_entry)

def move_jpg_files():
    """Moves all .jpg files from a source directory to a target directory."""
    print("\n--- [1] JPG Image Organizer ---")
    src_dir = input("Enter source folder path (default: 'demo_source'): ").strip() or "demo_source"
    dst_dir = input("Enter destination folder path (default: 'organized_jpgs'): ").strip() or "organized_jpgs"

    if not os.path.exists(src_dir):
        print(f"[!] Error: Source directory '{src_dir}' does not exist. Run Option 4 first to generate demo files!")
        return

    os.makedirs(dst_dir, exist_ok=True)
    moved_files = []

    for item in os.listdir(src_dir):
        if item.lower().endswith(".jpg"):
            src_path = os.path.join(src_dir, item)
            dst_path = os.path.join(dst_dir, item)
            
            if os.path.exists(dst_path):
                base, ext = os.path.splitext(item)
                dst_path = os.path.join(dst_dir, f"{base}_copy{ext}")
                
            shutil.move(src_path, dst_path)
            moved_files.append(item)

    print(f"[+] Success! Moved {len(moved_files)} .jpg file(s) to '{dst_dir}'.")
    if moved_files:
        print(f"    Files: {', '.join(moved_files)}")
    log_event("JPG_ORGANIZER", f"Moved {len(moved_files)} files from '{src_dir}' to '{dst_dir}'")

def extract_emails():
    """Extracts all unique email addresses from a .txt file and saves them."""
    print("\n--- [2] Email Address Extractor ---")
    input_path = input("Enter source .txt file (default: 'sample_data.txt'): ").strip() or "sample_data.txt"
    output_path = input("Enter output file (default: 'extracted_emails.txt'): ").strip() or "extracted_emails.txt"

    if not os.path.exists(input_path):
        print(f"[!] Error: File '{input_path}' not found. Run Option 4 first to generate demo files!")
        return

    with open(input_path, "r", encoding="utf-8") as file:
        content = file.read()

    email_regex = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    found_emails = re.findall(email_regex, content)
    unique_emails = sorted(set(email.lower() for email in found_emails))

    with open(output_path, "w", encoding="utf-8") as file:
        file.write(f"# Extracted Emails from {input_path}\n")
        file.write(f"# Total Unique Emails: {len(unique_emails)}\n\n")
        for email in unique_emails:
            file.write(f"{email}\n")

    print(f"[+] Extracted {len(unique_emails)} unique email(s) -> saved to '{output_path}'.")
    log_event("EMAIL_EXTRACTOR", f"Extracted {len(unique_emails)} emails from '{input_path}' to '{output_path}'")

def scrape_webpage_title():
    """Scrapes the <title> of a webpage and saves metadata to a report file."""
    print("\n--- [3] Webpage Title Scraper ---")
    url = input("Enter full URL (default: 'https://www.python.org'): ").strip() or "https://www.python.org"
    output_path = input("Enter output file (default: 'scraped_titles.txt'): ").strip() or "scraped_titles.txt"

    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    try:
        headers = {"User-Agent": "Mozilla/5.0 (CodeAlpha-Automation-Bot/1.0)"}
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        match = re.search(r"<title[^>]*>(.*?)</title>", response.text, re.IGNORECASE | re.DOTALL)
        title = re.sub(r"\s+", " ", match.group(1)).strip() if match else "No <title> tag found"

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        record = (
            f"Timestamp : {timestamp}\n"
            f"Target URL: {url}\n"
            f"HTTP Code : {response.status_code}\n"
            f"Page Title: {title}\n"
            f"{'-'*45}\n"
        )

        with open(output_path, "a", encoding="utf-8") as file:
            file.write(record)

        print(f"[+] Scraped Title: '{title}'")
        print(f"[+] Saved report to '{output_path}'.")
        log_event("WEB_SCRAPER", f"Scraped '{title}' from {url}")

    except requests.RequestException as err:
        print(f"[!] Network/HTTP Error: {err}")

def setup_demo_environment():
    """Creates sample files and folders so you can test the script immediately."""
    print("\n--- [4] Setting Up Demo Environment ---")
    
    os.makedirs("demo_source", exist_ok=True)
    sample_files = ["sunset_photo.jpg", "profile_pic.JPG", "architecture.jpg", "notes.txt"]
    for fname in sample_files:
        with open(os.path.join("demo_source", fname), "w", encoding="utf-8") as f:
            f.write("Dummy file content for CodeAlpha Task 3 testing.")

    sample_text = """
    Hello team, please reach out to services@codealpha.tech or hr.department@company.org.
    For technical support, contact dev_lead99@python.org or support@github.com.
    Duplicate test: SERVICES@codealpha.tech.
    """
    with open("sample_data.txt", "w", encoding="utf-8") as f:
        f.write(sample_text.strip())

    print("[+] Created folder 'demo_source/' with 3 .jpg files and 1 .txt file.")
    print("[+] Created 'sample_data.txt' with sample emails.")
    print("[+] You can now test Options 1, 2, and 3 by just pressing Enter on default prompts!")
    log_event("DEMO_SETUP", "Initialized demo files and directories")

def main():
    while True:
        print("\n================================================")
        print("   🚀 CodeAlpha Task 3: Automation Suite CLI    ")
        print("================================================")
        print("  1. Move all .jpg files to a new folder")
        print("  2. Extract email addresses from a .txt file")
        print("  3. Scrape the title of a webpage")
        print("  4. [Demo Setup] Generate test files & folders")
        print("  5. Exit")
        print("================================================")

        choice = input("Select an option (1-5): ").strip()

        if choice == "1":
            move_jpg_files()
        elif choice == "2":
            extract_emails()
        elif choice == "3":
            scrape_webpage_title()
        elif choice == "4":
            setup_demo_environment()
        elif choice == "5":
            print("Exiting Automation Suite. Goodbye!")
            break
        else:
            print("[!] Invalid option. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()