from adb_connector import run_adb_query
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='ignore')

def parse_sms_output(raw_output: str):
    messages = []
    for line in raw_output.split('\n'):
        msg = {}
        for part in line.split(', '):
            if '=' in part:
                key, value = part.split('=', 1)
                msg[key.strip()] = value.strip()
        if msg:
            body = msg.get('body', '').replace('\n', ' ')
            sender = msg.get('address', 'Unknown')
            date = msg.get('date', 'Unknown')
            messages.append(f"From: {sender}\nDate: {date}\nMessage: {body}\n")
    return messages

def main():
    try:
        raw_output = run_adb_query("content://sms/inbox")
        messages = parse_sms_output(raw_output)
        print("\n".join(messages))
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
