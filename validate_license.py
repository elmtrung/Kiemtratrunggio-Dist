
import sys
import requests
import csv
import io

# Thay LINK_GOOGLE_SHEET_CSV o day
# Cach lay link: File -> Share -> Publish to web -> Chon CSV -> Copy link
LICENSE_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRshXH-ZwTwwOsSMZ8h8bNGm9w0RnuBABOWHtkQOyrAXZSCl8FDEXhK0HYk4R7_-09Zqgpr7X8dJX4z/pub?output=csv"

def check_license(code):
    try:
        # Fetch the valid licenses from Google Sheet (CSV format)
        print(f"Dang ket noi den Google Sheet...")
        response = requests.get(LICENSE_URL, timeout=10)
        response.raise_for_status()
        
        # Parse CSV data
        # Gia su ma ban quyen o cot dau tien (Column A)
        csv_file = io.StringIO(response.text)
        reader = csv.reader(csv_file)
        
        valid_codes = []
        for row in reader:
            if row: # Check neu dong khong rong
                valid_codes.append(row[0].strip())
        
        # Check if the entered code is in the list
        if code.strip() in valid_codes:
            print("[SUCCESS] Ma ban quyen hop le!")
            return True
        else:
            print("[ERROR] Ma ban quyen KHONG hop le hoac da bi khoa.")
            return False
            
    except requests.exceptions.RequestException as e:
        print(f"[ERROR] Khong the ket noi den Google Sheet: {e}")
        return False
    except Exception as e:
        print(f"[ERROR] Loi khong xac dinh: {e}")
        return False

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Vui long nhap ma ban quyen.")
        sys.exit(1)
        
    code = sys.argv[1]
    if check_license(code):
        sys.exit(0) # Success
    else:
        sys.exit(1) # Failure
