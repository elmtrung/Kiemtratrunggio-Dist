
import sys
import os
from security_utils import encrypt_config

def main():
    print("===================================================")
    print("  CAU HINH DATABASE (ENCRYPTED)")
    print("===================================================")
    
    db_server = input("Nhap ten Server (VD: localhost, 192.168.1.10): ").strip()
    db_name = input("Nhap ten Database (VD: HIS_MISA): ").strip()
    db_user = input("Nhap User DB (VD: sa): ").strip()
    db_password = input("Nhap Password DB: ").strip()
    
    if not all([db_server, db_name, db_user, db_password]):
        print("[ERROR] Vui long nhap day du thong tin!")
        sys.exit(1)
        
    config = {
        "DB_SERVER": db_server,
        "DB_NAME": db_name,
        "DB_USER": db_user,
        "DB_PASSWORD": db_password,
        "APP_HOST": "0.0.0.0",
        "APP_PORT": 5000,
        "APP_DEBUG": False
    }
    
    try:
        output_path = os.path.join(os.getcwd(), 'config.enc')
        encrypt_config(config, output_path)
        print(f"\n[OK] Da luu va MA HOA cau hinh vao: {output_path}")
        
        # Cleanup .env if exists to prevent leak
        env_path = os.path.join(os.getcwd(), '.env')
        if os.path.exists(env_path):
            os.remove(env_path)
            print("[INFO] Da xoa file .env cu (neu co).")
            
    except Exception as e:
        print(f"[ERROR] Loi khi luu cau hinh: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
