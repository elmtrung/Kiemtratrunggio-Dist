
import sys
import requests

LICENSE_URL = "https://raw.githubusercontent.com/elmtrung/Kiemtratrunggio-Dist/main/licenses.txt"

def check_license(code):
    try:
        # Fetch the valid licenses from the repository
        response = requests.get(LICENSE_URL, timeout=10)
        response.raise_for_status()
        
        # Parse the license codes (one per line)
        valid_codes = [line.strip() for line in response.text.splitlines() if line.strip()]
        
        # Check if the entered code is in the list
        if code.strip() in valid_codes:
            print("[SUCCESS] Ma ban quyen hop le!")
            return True
        else:
            print("[ERROR] Ma ban quyen KHONG hop le hoac da bi khoa.")
            return False
            
    except requests.exceptions.RequestException as e:
        print(f"[ERROR] Khong the ket noi den may chu kiem tra ban quyen: {e}")
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
